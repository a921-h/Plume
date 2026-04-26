"""
Routing system for Plume.

Handles:
- File-based routing
- Dynamic routes with [slug] syntax
- Page layouts
- Frontmatter metadata
"""

from __future__ import annotations

import os
import re
import hashlib
from pathlib import Path
from typing import Any, Callable, TypeVar, Generic
from dataclasses import dataclass, field
from datetime import datetime


T = TypeVar("T")


@dataclass
class Page:
    """
    Represents a single page in the site.
    
    Attributes:
        path: URL path (e.g., "/blog/my-post")
        slug: URL-safe identifier
        title: Page title
        content: HTML content
        meta: Frontmatter metadata
        layout: Layout function to use
        component: Optional component renderer
    """
    path: str
    html: str = ""
    slug: str = ""
    title: str = ""
    meta: dict[str, Any] = field(default_factory=dict)
    content: str = ""
    layout: Callable | None = None
    source_file: str = ""
    excerpt: str = ""
    date: datetime | None = None
    author: str = ""
    tags: list[str] = field(default_factory=list)
    draft: bool = False
    
    def __post_init__(self) -> None:
        if not self.slug:
            self.slug = self._generate_slug()
        if not self.title and self.meta:
            self.title = self.meta.get("title", "")
    
    def _generate_slug(self) -> str:
        """Generate URL-safe slug from path."""
        if self.path == "/":
            return "index"
        
        slug = self.path.rstrip("/")
        if slug.startswith("/"):
            slug = slug[1:]
        
        slug = re.sub(r"[^\w\-]", "-", slug)
        slug = re.sub(r"-+", "-", slug)
        return slug or "index"
    
    def render(self) -> str:
        """Render page with its layout."""
        if self.layout:
            return self.layout({"content": self.html, **self.meta})
        return self.html


@dataclass 
class Route:
    """Represents a route in the routing system."""
    path: str
    file: Path
    pattern: str = ""
    handler: Callable | None = None
    
    @property
    def is_dynamic(self) -> bool:
        """Check if route has dynamic parameters."""
        return "[" in self.path and "]" in self.path
    
    @property
    def param_names(self) -> list[str]:
        """Extract parameter names from dynamic route."""
        if not self.is_dynamic:
            return []
        return re.findall(r"\[(\w+)\]", self.path)


class Router:
    """File-based router for Plume."""
    
    def __init__(
        self, 
        pages_dir: str = "pages",
        content_dir: str = "content",
    ) -> None:
        self.pages_dir = Path(pages_dir)
        self.content_dir = Path(content_dir)
        self._routes: dict[str, Route] = {}
        self._pages: dict[str, Page] = {}
    
    def discover_routes(self) -> list[Route]:
        """Discover all routes from pages directory."""
        routes = []
        
        if not self.pages_dir.exists():
            return routes
        
        for file in self.pages_dir.rglob("*.py"):
            if file.name.startswith("_"):
                continue
            
            route_path = self._file_to_route(file)
            route = Route(
                path=route_path,
                file=file,
                pattern=route_path,
            )
            routes.append(route)
        
        return routes
    
    def _file_to_route(self, file: Path) -> str:
        """Convert file path to route path."""
        parts = file.relative_to(self.pages_dir).parts
        
        if file.stem == "index":
            route = "/" + "/".join(parts[:-1])
        else:
            route = "/".join(parts).replace(".py", "")
        
        return "/" + route  # Ensure leading slash
    
    def get_page(self, path: str) -> Page | None:
        """Get page by path."""
        return self._pages.get(path)
    
    def add_page(self, page: Page) -> None:
        """Add a page to the router."""
        self._pages[page.path] = page
    
    def list_routes(self) -> list[str]:
        """List all registered routes."""
        return list(self._pages.keys())


# =============================================================================
# Layout System
# =============================================================================

_layouts: dict[str, Callable] = {}


def layout(name: str = "default") -> Callable:
    """
    Decorator to register a layout function.
    
    Usage:
        @layout("base")
        def base(data):
            return Html(
                Head(Title(data.get("title", "My Site"))),
                Body(data.get("content", ""))
            )
    """
    def decorator(fn: Callable) -> Callable:
        _layouts[name] = fn
        return fn
    return decorator


def get_layout(name: str = "default") -> Callable | None:
    """Get a layout by name."""
    return _layouts.get(name)


def render_with_layout(content: str, layout_name: str, data: dict) -> str:
    """Render content with a specific layout."""
    layout_fn = get_layout(layout_name)
    if layout_fn:
        return layout_fn({**data, "content": content})
    return content


# =============================================================================
# Page Builder
# =============================================================================

def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")


def format_date(date: str | datetime, format: str = "%Y-%m-%d") -> str:
    """Format a date string."""
    if isinstance(date, datetime):
        return date.strftime(format)
    
    try:
        dt = datetime.strptime(date, "%Y-%m-%d")
        return dt.strftime(format)
    except ValueError:
        return date


class PageBuilder:
    """Build pages from content files."""
    
    def __init__(
        self,
        content_dir: str = "content",
        pages_dir: str = "pages",
    ) -> None:
        self.content_dir = Path(content_dir)
        self.pages_dir = Path(pages_dir)
        self._posts: list[Page] = []
    
    def build_pages(self) -> list[Page]:
        """Build all pages from content and pages directories."""
        pages = []
        
        pages.extend(self._build_from_directory(self.pages_dir))
        pages.extend(self._build_from_directory(self.content_dir, is_content=True))
        
        self._posts.sort(key=lambda p: p.date or datetime.min, reverse=True)
        
        return pages
    
    def _build_from_directory(
        self, 
        directory: Path, 
        is_content: bool = False
    ) -> list[Page]:
        """Build pages from a directory."""
        pages = []
        
        if not directory.exists():
            return pages
        
        for file in directory.rglob("*.md"):
            page = self._build_page(file, is_content=is_content)
            pages.append(page)
        
        for file in directory.rglob("*.py"):
            if file.name.startswith("_"):
                continue
            page = self._build_page(file, is_content=is_content)
            pages.append(page)
        
        return pages
    
    def _build_page(
        self, 
        file: Path,
        is_content: bool = False,
    ) -> Page:
        """Build a single page from a file."""
        from plume.markdown import render_markdown
        
        path = self._file_to_path(file, is_content)
        
        if file.suffix == ".py":
            content, meta = self._execute_py_page(file)
        else:
            with open(file, "r", encoding="utf-8") as f:
                content, meta = render_markdown(f.read())
        
        return Page(
            path=path,
            html=content,
            title=meta.get("title", file.stem),
            meta=meta,
            source_file=str(file),
            slug=slugify(meta.get("title", file.stem)),
            date=self._parse_date(meta.get("date", "")),
            author=meta.get("author", ""),
            tags=meta.get("tags", []),
            draft=meta.get("draft", False),
        )
    
    def _file_to_path(self, file: Path, is_content: bool) -> str:
        """Convert file path to URL path."""
        if is_content:
            rel = file.relative_to(self.content_dir)
        else:
            rel = file.relative_to(self.pages_dir)
        
        parts = list(rel.parts)
        
        if file.stem == "index":
            parts = parts[:-1]
        else:
            parts[-1] = file.stem
        
        path = "/" + "/".join(parts)
        
        if file.suffix == ".md":
            path = path.replace(".md", "")
        
        return path
    
    def _execute_py_page(self, file: Path) -> tuple[str, dict]:
        """Execute a Python page file and return its content."""
        import importlib.util
        import sys
        from plume.components import (
            Component, Html, Head, Body, Title, Meta, Link, Script,
            Div, Span, H1, H2, H3, P, A, Img, UL, OL, LI, Blockquote,
            Pre, Code, Nav, Footer, Main, Section, Article, Header,
            Button, Input, Table, Thead, Tbody, Tr, Th, Td, Hr, Br,
        )
        
        component_names = [
            "Component", "Html", "Head", "Body", "Title", "Meta", "Link", "Script",
            "Div", "Span", "H1", "H2", "H3", "P", "A", "Img", "UL", "OL", "LI",
            "Blockquote", "Pre", "Code", "Nav", "Footer", "Main", "Section",
            "Article", "Header", "Button", "Input", "Table", "Thead", "Tbody",
            "Tr", "Th", "Td", "Hr", "Br",
        ]
        
        components_dict = {
            "Component": Component, "Html": Html, "Head": Head, "Body": Body,
            "Title": Title, "Meta": Meta, "Link": Link, "Script": Script,
            "Div": Div, "Span": Span, "H1": H1, "H2": H2, "H3": H3, "P": P,
            "A": A, "Img": Img, "UL": UL, "OL": OL, "LI": LI,
            "Blockquote": Blockquote, "Pre": Pre, "Code": Code, "Nav": Nav,
            "Footer": Footer, "Main": Main, "Section": Section,
            "Article": Article, "Header": Header, "Button": Button,
            "Input": Input, "Table": Table, "Thead": Thead, "Tbody": Tbody,
            "Tr": Tr, "Th": Th, "Td": Td, "Hr": Hr, "Br": Br,
        }
        
        spec = importlib.util.spec_from_file_location("page", file)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            
            for name, comp in components_dict.items():
                setattr(module, name, comp)
            
            sys.modules["page"] = module
            spec.loader.exec_module(module)
            
            if hasattr(module, "render"):
                try:
                    result = module.render({})
                except TypeError:
                    result = module.render()
                if isinstance(result, str):
                    return result, {"title": "Page"}
                elif hasattr(result, "render"):
                    return result.render(), {"title": "Page"}
                elif isinstance(result, tuple):
                    return result
                else:
                    return str(result), {"title": "Page"}
            elif hasattr(module, "render_with_data"):
                data = {"title": "Page", "posts": []}
                result = module.render_with_data(data)
                if isinstance(result, str):
                    return result, {"title": "Page"}
                elif hasattr(result, "render"):
                    return result.render(), {"title": "Page"}
                else:
                    return str(result), {"title": "Page"}
            elif hasattr(module, "Page"):
                page = module.Page
                return page.html, page.meta
        
        return "", {}
    
    def _parse_date(self, date_str: str) -> datetime | None:
        """Parse date string to datetime."""
        if not date_str:
            return None
        
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            return None
    
    @property
    def posts(self) -> list[Page]:
        """Get all posts sorted by date."""
        return self._posts