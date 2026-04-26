"""
Core components system for Plume.

All HTML elements are available as Python components that render to HTML strings.
"""

from __future__ import annotations

import json
from typing import Any, Callable, Iterable


class Component:
    """
    Base class for all Plume components.
    
    Components are Python objects that render themselves to HTML strings.
    """
    
    __slots__ = ("_children", "_attrs", "_tag")
    
    def __init__(
        self, 
        *children: Any, 
        tag: str | None = None,
        **attrs: Any
    ) -> None:
        self._children = children
        self._attrs = attrs
        self._tag = tag
    
    def render(self) -> str:
        """Render component to HTML string."""
        parts = []
        
        for child in self._children:
            if isinstance(child, Component):
                parts.append(child.render())
            elif child is not None and child != "":
                parts.append(str(child))
        
        inner = "".join(parts)
        
        if self._tag:
            attrs = self._render_attrs()
            if self._children:
                return f"<{self._tag}{attrs}>{inner}</{self._tag}>"
            else:
                return f"<{self._tag}{attrs} />"
        
        return inner
    
    def _render_attrs(self) -> str:
        """Render attributes to HTML string."""
        if not self._attrs:
            return ""
        
        attrs = []
        for key, value in self._attrs.items():
            if value is True:
                attrs.append(key)
            elif value is not None and value != "":
                if key == "cls":
                    key = "class"
                elif key == "_for":
                    key = "for"
                attrs.append(f'{key}="{self._escape(str(value))}"')
        
        return " " + " ".join(attrs) if attrs else ""
    
    @staticmethod
    def _escape(text: str) -> str:
        """Escape HTML special characters."""
        return (
            text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;")
        )
    
    def __str__(self) -> str:
        return self.render()
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


def render(*components: Component) -> str:
    """Render multiple components to a single HTML string."""
    return "".join(c.render() for c in components)


# =============================================================================
# HTML Elements
# =============================================================================

class Html(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="html", **attrs)


class Head(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="head", **attrs)


class Body(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="body", **attrs)


class Title(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="title", **attrs)


class Meta(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="meta", **attrs)


class Link(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="link", **attrs)


class Script(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="script", **attrs)


class Div(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="div", **attrs)


class Span(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="span", **attrs)


class H1(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="h1", **attrs)


class H2(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="h2", **attrs)


class H3(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="h3", **attrs)


class H4(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="h4", **attrs)


class P(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="p", **attrs)


class A(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="a", **attrs)


class Img(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="img", **attrs)


class UL(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="ul", **attrs)


class OL(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="ol", **attrs)


class LI(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="li", **attrs)


class Blockquote(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="blockquote", **attrs)


class Pre(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="pre", **attrs)


class Code(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="code", **attrs)


class Nav(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="nav", **attrs)


class Footer(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="footer", **attrs)


class Main(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="main", **attrs)


class Section(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="section", **attrs)


class Article(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="article", **attrs)


class Header(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="header", **attrs)


class Button(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="button", **attrs)


class Input(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="input", **attrs)


class Textarea(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="textarea", **attrs)


class Select(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="select", **attrs)


class Option(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="option", **attrs)


class Table(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="table", **attrs)


class Thead(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="thead", **attrs)


class Tbody(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="tbody", **attrs)


class Tr(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="tr", **attrs)


class Th(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="th", **attrs)


class Td(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="td", **attrs)


class Hr(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="hr", **attrs)


class Br(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="br", **attrs)


class Details(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="details", **attrs)


class Summary(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="summary", **attrs)


class Dialog(Component):
    __slots__ = ()
    
    def __init__(self, *children: Any, **attrs: Any) -> None:
        super().__init__(*children, tag="dialog", **attrs)


# =============================================================================
# Island Component (for interactive components)
# =============================================================================

class Island(Component):
    """
    An interactive island component that renders client-side.
    
    Usage:
        island = Island(
            component="Counter",  # JavaScript component name
            props={"initial": 0},  # Props passed to the component
        )
    """
    
    __slots__ = ()
    
    def __init__(
        self, 
        component: str,
        props: dict | None = None,
        **attrs: Any
    ) -> None:
        self._children = ()
        self._attrs = {"data-island": component, **(props or {})}
        self._tag = "plume-island"
    
    def render(self) -> str:
        """Render island as a script tag with data."""
        props_json = json.dumps(self._attrs)
        return f'<script type="application/json" data-island="{self._attrs.get("data-island")}">{props_json}</script>'


# =============================================================================
# Conditional Components
# =============================================================================

class If(Component):
    """Conditional rendering based on a condition."""
    
    __slots__ = ()
    
    def __init__(self, condition: bool, *children: Any) -> None:
        self._condition = condition
        self._children = children
        self._attrs = {}
        self._tag = None
    
    def render(self) -> str:
        if self._condition:
            return render(*self._children)
        return ""


class For(Component):
    """Loop over an iterable and render for each item."""
    
    __slots__ = ()
    
    def __init__(
        self, 
        iterable: Iterable, 
        render_fn: Callable,
        **attrs: Any
    ) -> None:
        self._iterable = iterable
        self._render_fn = render_fn
        self._attrs = attrs
        self._tag = None
    
    def render(self) -> str:
        parts = []
        for item in self._iterable:
            child = self._render_fn(item)
            if isinstance(child, Component):
                parts.append(child.render())
            elif child is not None:
                parts.append(str(child))
        return "".join(parts)


# =============================================================================
# Slot System for Layouts
# =============================================================================

class Slot(Component):
    """A placeholder for content in a layout."""
    
    __slots__ = ()
    
    def __init__(self, name: str = "default") -> None:
        self._children = ()
        self._attrs = {"data-slot": name}
        self._tag = None
    
    def render(self) -> str:
        return ""


class Children(Component):
    """Render children passed to a component."""
    
    __slots__ = ()
    
    def __init__(self) -> None:
        self._children = ()
        self._attrs = {}
        self._tag = None
    
    def render(self) -> str:
        return ""