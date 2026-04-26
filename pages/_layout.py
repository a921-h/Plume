"""Base layout for all pages."""

from plume import Html, Head, Body, Title, Meta, Link, Main, Footer, P, Nav, Div, A, Section


def render(data):
    content = data.get("content", "")
    posts = data.get("posts", [])
    site_title = data.get("title", "Mi Blog Estatico")
    
    return Html(
        Head(
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Title(site_title),
            Meta(name="description", content="Bienvenido a mi sitio estatico generado con Python, Flask y Markdown."),
            Link(rel="preconnect", href="https://fonts.googleapis.com"),
            Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin="true"),
            Link(href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap", rel="stylesheet"),
            Link(rel="stylesheet", href="/static/styles.css"),
        ),
        Body(
            Div(
                Div(
                    Div(
                        A("Mi Sitio", href="/", cls="nav-brand"),
                        Nav(
                            A("Inicio", href="/"),
                            A("GitHub", href="https://github.com/", target="_blank", rel="noopener"),
                            cls="nav-links"
                        ),
                        cls="wrapper nav-inner"
                    ),
                    cls="site-header"
                ),
                content if content else "No content",
                Div(
                    P("Generado con Python - Flask - Markdown - Plume"),
                    cls="wrapper"
                ),
                cls="site-footer"
            ),
            cls="app-container"
        ),
    )