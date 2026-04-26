"""Home page - displays list of blog posts."""

from plume import Html, Head, Body, Title, Meta, Link, Main, Footer, P, Nav, Div, A, Section, H1, Span


def render():
    return Html(
        Head(
            Title("Mi Blog Estatico"),
            Meta(name="description", content="Bienvenido a mi sitio estatico generado con Python, Flask y Markdown."),
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
                Section(
                    Div(
                        Span("Generador de sitios estaticos - Python", cls="hero-badge"),
                        H1("Ideas que merecen ser compartidas"),
                        P("Articulos escritos en Markdown, convertidos automaticamente en paginas web modernas."),
                        cls="wrapper hero"
                    ),
                    cls="hero-section"
                ),
                Section(
                    Div(
                        P("Publicaciones", cls="section-title"),
                        Div(
                            A("Bienvenido al Generador de Sitios Estaticos", href="/post/bienvenido-al-generador-de-sitios-estaticos", cls="post-link")
                        ),
                        cls="wrapper posts-section"
                    ),
                    cls="posts-section"
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