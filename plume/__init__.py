"""
Plume - A modern Python static site generator with components.

Quick start:
    from plume import Page, Component, layout
    
    @layout
    def base(data):
        return Html(
            Head(Title(data.title)),
            Body(data.content)
        )
"""

__version__ = "0.1.0"

from plume.components import (
    Component,
    Html,
    Head,
    Body,
    Title,
    Meta,
    Link,
    Script,
    Div,
    Span,
    H1,
    H2,
    H3,
    P,
    A,
    Img,
    UL,
    OL,
    LI,
    Blockquote,
    Pre,
    Code,
    Nav,
    Footer,
    Main,
    Section,
    Article,
    Header,
)
from plume.routing import Page, layout
from plume.build import build, serve

__all__ = [
    "Component",
    "Page",
    "layout",
    "build",
    "serve",
    "Html",
    "Head",
    "Body",
    "Title",
    "Meta",
    "Link",
    "Script",
    "Div",
    "Span",
    "H1",
    "H2",
    "H3",
    "P",
    "A",
    "Img",
    "UL",
    "OL",
    "LI",
    "Blockquote",
    "Pre",
    "Code",
    "Nav",
    "Footer",
    "Main",
    "Section",
    "Article",
    "Header",
]