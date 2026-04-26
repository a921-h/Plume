"""Individual post page view."""

from plume import Html, Head, Body, Title, Meta, Link, Main, Footer, P, Nav, Div, A, Section, H1, Span


def render(data):
    post = data.get("post", {})
    site_title = data.get("title", "Mi Blog Estatico")
    
    post_title = post.get("meta", {}).get("title", "Post")
    post_html = post.get("html", "")
    post_date = post.get("meta", {}).get("date", "")
    post_author = post.get("meta", {}).get("author", "")
    post_tags = post.get("meta", {}).get("tags", [])
    
    return Html(
        Head(
            Title(post_title + " - " + site_title),
            Meta(name="description", content=post.get("meta", {}).get("description", "")),
            Link(rel="stylesheet", href="/static/styles.css"),
            Link(rel="preconnect", href="https://fonts.googleapis.com"),
            Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin="true"),
            Link(href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap", rel="stylesheet"),
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
                Div(
                    Div(
                        A("Volver al inicio", href="/", cls="back-link"),
                        H1(post_title),
                        Div(
                            Span((post_date + " - " + post_author) if post_author else post_date),
                            cls="post-meta"
                        ),
                        Div(
                            Span(post_html),
                            cls="prose"
                        ),
                        cls="post-content"
                    ),
                    cls="post-detail"
                ),
                Footer(
                    Div(
                        P("Generado con Python - Flask - Markdown - Plume"),
                        cls="wrapper"
                    ),
                    cls="site-footer"
                ),
                cls="app"
            ),
            cls="main-container"
        ),
        cls="page-wrapper"
    )