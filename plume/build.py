"""
Build system for Plume.

Handles:
- Site building
- Incremental builds
- Asset copying
- Output optimization
"""

from __future__ import annotations

import os
import shutil
import hashlib
import json
from pathlib import Path
from typing import Any
from datetime import datetime


class BuildConfig:
    """Configuration for the build process."""
    
    def __init__(
        self,
        output_dir: str = "dist",
        static_dir: str = "static",
        pages_dir: str = "pages",
        content_dir: str = "content",
        templates_dir: str = "templates",
        minify_html: bool = True,
        minify_css: bool = True,
        minify_js: bool = True,
        site_name: str = "Mi Sitio",
    ) -> None:
        self.output_dir = Path(output_dir)
        self.static_dir = Path(static_dir)
        self.pages_dir = Path(pages_dir)
        self.content_dir = Path(content_dir)
        self.templates_dir = Path(templates_dir)
        self.minify_html = minify_html
        self.minify_css = minify_css
        self.minify_js = minify_js
        self.site_name = site_name


class BuildResult:
    """Result of a build operation."""
    
    def __init__(
        self,
        success: bool,
        pages_built: int = 0,
        pages_skipped: int = 0,
        errors: list[str] | None = None,
        duration: float = 0.0,
    ) -> None:
        self.success = success
        self.pages_built = pages_built
        self.pages_skipped = pages_skipped
        self.errors = errors or []
        self.duration = duration
    
    @property
    def total_pages(self) -> int:
        return self.pages_built + self.pages_skipped


class BuildCache:
    """Cache for incremental builds."""
    
    def __init__(self, cache_dir: str = ".plume") -> None:
        self.cache_dir = Path(cache_dir)
        self.cache_file = self.cache_dir / "build.cache"
        self._cache: dict[str, Any] = {}
    
    def load(self) -> dict[str, str]:
        """Load cache from disk."""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        return {}
    
    def save(self, cache: dict[str, Any]) -> None:
        """Save cache to disk."""
        self.cache_dir.mkdir(exist_ok=True)
        with open(self.cache_file, "w") as f:
            json.dump(cache, f)
    
    def get_file_hash(self, path: Path) -> str:
        """Get hash of a file."""
        if not path.exists():
            return ""
        
        hasher = hashlib.sha256()
        with open(path, "rb") as f:
            hasher.update(f.read())
        return hasher.hexdigest()
    
    def needs_rebuild(
        self, 
        source: Path, 
        output: Path,
    ) -> bool:
        """Check if a file needs to be rebuilt."""
        if not output.exists():
            return True
        
        source_mtime = source.stat().st_mtime
        output_mtime = output.stat().st_mtime
        
        return source_mtime > output_mtime


def build(config: BuildConfig | None = None) -> BuildResult:
    """Build the static site."""
    start_time = datetime.now()
    
    if config is None:
        config = BuildConfig()
    
    cache = BuildCache()
    cached_hashes = cache.load()
    
    pages_built = 0
    pages_skipped = 0
    errors = []
    
    config.output_dir.mkdir(exist_ok=True)
    
    _copy_static_assets(config)
    
    from plume.routing import PageBuilder
    from plume.markdown import render_markdown
    
    builder = PageBuilder(
        content_dir=str(config.content_dir),
        pages_dir=str(config.pages_dir),
    )
    
    pages = builder.build_pages()
    
    content_pages = [p for p in pages if p.source_file.endswith(".md")]
    py_pages = [p for p in pages if p.source_file.endswith(".py")]
    
    for page in py_pages:
        if page.draft:
            continue
        
        output_path = _get_output_path(page.path, config.output_dir)
        
        if config.minify_html and page.html:
            page.html = _minify_html(page.html)
        
        _write_file(output_path, page.html)
        pages_built += 1
    
    for cp in content_pages:
        if cp.draft:
            continue
        
        output_path = _get_output_path(cp.path, config.output_dir)
        
        if config.minify_html and cp.html:
            cp.html = _minify_html(cp.html)
        
        _write_file(output_path, cp.html)
        pages_built += 1
    
    new_hashes = {}
    for page in pages:
        source = Path(page.source_file)
        if source.exists():
            new_hashes[str(source)] = cache.get_file_hash(source)
    
    cache.save(new_hashes)
    
    duration = (datetime.now() - start_time).total_seconds()
    
    return BuildResult(
        success=len(errors) == 0,
        pages_built=pages_built,
        pages_skipped=pages_skipped,
        errors=errors,
        duration=duration,
    )


def _copy_static_assets(config: BuildConfig) -> None:
    """Copy static assets to output directory."""
    if not config.static_dir.exists():
        return
    
    output_static = config.output_dir / "static"
    
    if output_static.exists():
        shutil.rmtree(output_static)
    
    shutil.copytree(config.static_dir, output_static)


def _get_output_path(route: str, output_dir: Path) -> Path:
    """Get output file path for a route."""
    if route == "/":
        return output_dir / "index.html"
    
    path = route.strip("/")
    return output_dir / path / "index.html"


def _write_file(path: Path, content: str) -> None:
    """Write content to file, creating directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def _minify_html(html: str) -> str:
    """Minify HTML content."""
    import re
    
    html = re.sub(r"\s+", " ", html)
    html = re.sub(r">\s+<", "><", html)
    
    return html.strip()


def _minify_css(css: str) -> str:
    """Minify CSS content."""
    import re
    
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.DOTALL)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*[:;]\s*", lambda m: m.group(0).strip(), css)
    
    return css.strip()


def _minify_js(js: str) -> str:
    """Minify JavaScript content."""
    return js


def serve(
    host: str = "127.0.0.1",
    port: int = 8000,
    output_dir: str = "dist",
) -> None:
    """Serve the built site."""
    import http.server
    import socketserver
    
    os.chdir(output_dir)
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self) -> None:
            self.send_header("Cache-Control", "no-cache")
            super().end_headers()
    
    with socketserver.TCPServer((host, port), Handler) as httpd:
        print(f"Serving at http://{host}:{port}")
        httpd.serve_forever()


def clean(output_dir: str = "dist") -> None:
    """Clean the output directory."""
    path = Path(output_dir)
    if path.exists():
        shutil.rmtree(path)
        print(f"Cleaned {output_dir}/")


def preview(output_dir: str = "dist") -> None:
    """Preview the built site."""
    serve(output_dir=output_dir)