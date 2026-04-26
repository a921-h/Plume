"""
Plume CLI - Command line interface for Plume.

Commands:
    new <name>  - Create a new Plume project
    dev         - Start development server with hot reload
    build       - Build the static site
    serve       - Serve the built site
    clean       - Clean the output directory
"""

from __future__ import annotations

import os
import sys
import shutil
from pathlib import Path

import click


@click.group()
@click.version_option("0.1.0")
def cli():
    """Plume - A modern Python static site generator."""
    pass


@cli.command()
@click.argument("name")
@click.option("--template", "-t", default="basic", help="Template to use")
def new(name: str, template: str):
    """Create a new Plume project."""
    project_dir = Path(name)
    
    if project_dir.exists():
        click.echo(f"Error: Directory '{name}' already exists", err=True)
        sys.exit(1)
    
    project_dir.mkdir()
    
    (project_dir / "pages").mkdir()
    (project_dir / "content").mkdir()
    (project_dir / "static").mkdir()
    (project_dir / "templates").mkdir()
    (project_dir / ".plume").mkdir()
    
    _create_file(
        project_dir / "plume.config.py",
        _plume_config_template(),
    )
    
    _create_file(
        project_dir / "pages" / "index.py",
        _index_page_template(),
    )
    
    _create_file(
        project_dir / "pages" / "_layout.py",
        _layout_template(),
    )
    
    _create_file(
        project_dir / "static" / "styles.css",
        _default_css(),
    )
    
    _create_file(
        project_dir / "content" / "welcome.md",
        _welcome_content(),
    )
    
    _create_file(
        project_dir / ".gitignore",
        _gitignore(),
    )
    
    _create_file(
        project_dir / "README.md",
        _readme_template(name),
    )
    
    click.echo(f"Created new Plume project: {name}")
    click.echo(f"\nTo get started:")
    click.echo(f"  cd {name}")
    click.echo(f"  plume dev")


@cli.command()
@click.option("--host", default="127.0.0.1", help="Host to bind to")
@click.option("--port", default=8000, help="Port to bind to")
@click.option("--output", default="dist", help="Output directory")
@click.option("--watch/--no-watch", default=True, help="Watch for changes")
def dev(host: str, port: int, output: str, watch: bool):
    """Start development server with hot reload."""
    click.echo("Building site...")
    
    from plume.build import BuildConfig, build
    from plume.build import serve as serve_http
    
    config = BuildConfig(output_dir=output)
    result = build(config)
    
    if not result.success:
        click.echo("Build failed:", err=True)
        for error in result.errors:
            click.echo(f"  - {error}", err=True)
        sys.exit(1)
    
    click.echo("Built {0} pages in {1:.2f}s".format(result.pages_built, result.duration))
    click.echo(f"\nStarting dev server at http://{host}:{port}")
    
    if watch:
        click.echo("Watching for changes...")
        _watch_and_reload(host, port, output)
    else:
        serve_http(host=host, port=port, output_dir=output)


@cli.command()
@click.option("--output", "-o", default="dist", help="Output directory")
@click.option("--minify/--no-minify", default=True, help="Minify output")
@click.option("--incremental/--no-incremental", default=True, help="Use incremental builds")
def build(output: str, minify: bool, incremental: bool):
    """Build the static site."""
    from plume.build import BuildConfig, build as _build
    
    config = BuildConfig(
        output_dir=output,
        minify_html=minify,
        minify_css=minify,
        minify_js=minify,
    )
    
    result = _build(config)
    
    if result.success:
        click.echo("Built {0} pages in {1:.2f}s".format(result.pages_built, result.duration))
        
        if result.pages_skipped > 0:
            click.echo(f"  ({result.pages_skipped} pages skipped)")
    else:
        click.echo("Build failed:", err=True)
        for error in result.errors:
            click.echo(f"  - {error}", err=True)
        sys.exit(1)


@cli.command()
@click.option("--host", default="127.0.0.1", help="Host to bind to")
@click.option("--port", default=8000, help="Port to bind to")
@click.option("--output", default="dist", help="Directory to serve")
def serve(host: str, port: int, output: str):
    """Serve the built site."""
    from plume.build import serve as _serve
    
    click.echo(f"Serving at http://{host}:{port}")
    _serve(host=host, port=port, output_dir=output)


@cli.command()
@click.option("--output", "-o", default="dist", help="Output directory")
def clean(output: str):
    """Clean the output directory."""
    from plume.build import clean as _clean
    
    _clean(output)
    click.echo(f"Cleaned {output}/")


@cli.command()
def routes():
    """List all routes."""
    from plume.routing import Router
    
    router = Router()
    routes = router.discover_routes()
    
    click.echo("Routes:")
    for route in routes:
        click.echo(f"  {route.path}")


# =============================================================================
# Helper functions
# =============================================================================

def _create_file(path: Path, content: str) -> None:
    """Create a file with content."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def _watch_and_reload(host: str, port: int, output: str) -> None:
    """Watch for changes and rebuild."""
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
        
        class RebuildHandler(FileSystemEventHandler):
            def __init__(self):
                self.rebuild_count = 0
            
            def on_modified(self, event):
                if event.is_directory:
                    return
                
                if event.src_path.endswith((".py", ".md", ".css", ".html")):
                    self.rebuild_count += 1
                    click.echo(f"\nChanged: {event.src_path}")
                    click.echo("Rebuilding...")
                    
                    from plume.build import BuildConfig, build
                    config = BuildConfig(output_dir=output)
                    result = build(config)
                    
                    if result.success:
                        click.echo("Built {0} pages".format(result.pages_built))
                    else:
                        click.echo("Build failed:", err=True)
        
        handler = RebuildHandler()
        observer = Observer()
        observer.schedule(handler, ".", recursive=True)
        observer.start()
        
        try:
            import http.server
            import socketserver
            
            os.chdir(output)
            
            class Handler(http.server.SimpleHTTPRequestHandler):
                def log_message(self, format, *args):
                    pass
            
            with socketserver.TCPServer((host, port), Handler) as httpd:
                httpd.serve_forever()
        except KeyboardInterrupt:
            observer.stop()
    
    except ImportError:
        click.echo("watchdog not installed, using simple server")
        from plume.build import serve as _serve
        _serve(host=host, port=port, output_dir=output)


# =============================================================================
# Templates
# =============================================================================

def _plume_config_template() -> str:
    return '''"""Plume configuration."""

config = {
    "title": "My Site",
    "description": "A site built with Plume",
    "author": "Your Name",
    "base_url": "/",
    "output_dir": "dist",
    "static_dir": "static",
    "pages_dir": "pages",
    "content_dir": "content",
    "templates_dir": "templates",
}


def setup(app):
    """Setup function called before build."""
    pass
'''


def _index_page_template() -> str:
    return '''"""Home page."""

from plume import Html, Head, Body, Title, Meta, Link, Div, H1, P, Main

def render():
    return Html(
        Head(
            Title("Welcome to Plume"),
            Meta(name="description", content="A modern static site"),
            Link(rel="stylesheet", href="/static/styles.css"),
        ),
        Body(
            Main(
                Div(
                    H1("Hello, World!"),
                    P("Welcome to my Plume site."),
                    cls="hero",
                ),
            ),
        ),
    )
'''


def _layout_template() -> str:
    return '''"""Default layout."""

from plume import Html, Head, Body, Title, Meta, Main, Footer, P


def render(data):
    content = data.get("content", "")
    
    return Html(
        Head(
            Title(data.get("title", "My Site")),
        ),
        Body(
            Main(content),
            Footer(
                P("Built with Plume"),
            ),
        ),
    )
'''


def _default_css() -> str:
    return '''/* Plume default styles */

:root {
    --bg: #0f1117;
    --surface: #181c27;
    --text: #e2e8f0;
    --accent: #7c6af7;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    background: var(--bg);
    color: var(--text);
    font-family: system-ui, sans-serif;
    line-height: 1.6;
}

main {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
}

.hero {
    text-align: center;
    padding: 4rem 0;
}

h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

a {
    color: var(--accent);
}
'''


def _welcome_content() -> str:
    return '''---
title: Welcome to Plume
date: 2026-04-26
author: Abel
tags: getting-started, plume
description: Welcome to your new Plume site!
---

# Welcome to Plume

This is your first post built with **Plume**!

## Getting Started

1. Edit this file in `content/welcome.md`
2. Run `plume dev` to start development
3. Run `plume build` to build for production

## Next Steps

Check out the documentation to learn more about:
- Creating custom pages with Python components
- Using layouts and templates
- Adding interactive islands
'''


def _gitignore() -> str:
    return '''# Plume
dist/
.plume/
*.pyc
__pycache__/
.env

# Python
venv/
.venv/
*.egg-info/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
'''


def _readme_template(name: str) -> str:
    return f'''# {name}

A site built with [Plume](https://github.com/a921-h/plume) - A modern Python static site generator.

## Getting Started

```bash
# Install Plume
pip install plume

# Start development server
plume dev

# Build for production
plume build
```

## Project Structure

```
{name}/
├── pages/           # Python pages
├── content/        # Markdown content
├── static/        # Static assets (CSS, JS, images)
├── templates/     # HTML templates
└── dist/         # Built output
```
'''


def main():
    """Main entry point."""
    cli()


if __name__ == "__main__":
    main()