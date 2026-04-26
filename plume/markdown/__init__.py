"""
Markdown parsing and rendering for Plume.

Supports:
- Standard Markdown
- Frontmatter YAML metadata
- Code syntax highlighting
- Tables, task lists, footnotes
"""

from __future__ import annotations

import re
from datetime import datetime
from typing import Any
import markdown


class MarkdownRenderer:
    """Markdown to HTML converter."""
    
    def __init__(
        self,
        extensions: list[str] | None = None,
        extension_configs: dict | None = None,
    ) -> None:
        self.extensions = extensions or [
            "extra",
            "codehilite",
            "tables",
            "nl2br",
        ]
        self.extension_configs = extension_configs or {}
        self._md = markdown.Markdown(
            extensions=self.extensions,
            extension_configs=self.extension_configs,
        )
    
    def render(self, text: str) -> str:
        """Convert Markdown text to HTML."""
        return self._md.convert(text)
    
    def reset(self) -> None:
        """Reset the internal state for reuse."""
        self._md.reset()


def parse_frontmatter(raw: str) -> tuple[dict[str, Any], str]:
    """
    Extract YAML-style frontmatter between '---' delimiters.
    
    Returns:
        Tuple of (metadata dict, body text)
    """
    meta: dict = {}
    body = raw

    if raw.lstrip().startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            fm_block = parts[1]
            body = parts[2].lstrip("\n")
            
            for line in fm_block.splitlines():
                if ":" in line:
                    key, _, value = line.partition(":")
                    meta[key.strip()] = value.strip()

    body = body.strip()
    
    return meta, body


def render_markdown(
    text: str,
    with_frontmatter: bool = True,
) -> tuple[str, dict[str, Any]]:
    """
    Render Markdown to HTML with optional frontmatter parsing.
    
    Args:
        text: Markdown text
        with_frontmatter: Whether to parse frontmatter
        
    Returns:
        Tuple of (html, metadata)
    """
    renderer = MarkdownRenderer()
    
    if with_frontmatter:
        meta, body = parse_frontmatter(text)
    else:
        meta = {}
        body = text
    
    html = renderer.render(body)
    return html, meta


def markdown_to_html(text: str) -> str:
    """Simple convenience function to convert Markdown to HTML."""
    renderer = MarkdownRenderer()
    return renderer.render(text)


class PlumeMarkdown(MarkdownRenderer):
    """Markdown renderer configured for Plume projects."""
    
    def __init__(self) -> None:
        super().__init__(
            extensions=[
                "extra",
                "codehilite",
                "tables",
                "nl2br",
            ],
            extension_configs={
                "codehilite": {
                    "css_class": "highlight",
                    "linenums": False,
                },
            },
        )


def smart_quotes(text: str) -> str:
    """Convert straight quotes to curly quotes."""
    replacements = [
        (r'"([^"]*)"', r'"\1"'),
        (r"'([^']*)'", r"'\1'"),
    ]
    
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text)
    
    return text


def smart_dashes(text: str) -> str:
    """Convert -- to em-dashes and --- to en-dashes."""
    text = re.sub(r"---", "—", text)
    text = re.sub(r"(?<!-)-(?!-)", "–", text)
    return text


class AdmonitionExtension(markdown.Extension):
    """Add admonition blocks (note, warning, tip, etc.)."""
    
    def extend(self, md: markdown.Markdown) -> None:
        md.preprocessors.register(
            AdmonitionPreprocessor(),
            "admonition",
            175,
        )


class AdmonitionPreprocessor(markdown.preprocessors.Preprocessor):
    """Process admonition blocks."""
    
    ADMONITIONS = {
        "note": "💡 Note",
        "warning": "⚠️ Warning",
        "tip": "🚀 Tip",
        "danger": "❌ Danger", 
        "info": "ℹ️ Info",
        "hint": "💡 Hint",
    }
    
    def run(self, lines: list[str]) -> list[str]:
        new_lines = []
        in_admonition = False
        admonition_type = ""
        
        for line in lines:
            match = re.match(r"^:::\s*(\w+)", line)
            
            if match:
                in_admonition = True
                admonition_type = match.group(1)
                title = self.ADMONITIONS.get(admonition_type, admonition_type)
                new_lines.append(
                    f'<div class="admonition {admonition_type}">'
                )
                if title:
                    new_lines.append(
                        f'<div class="admonition-title">{title}</div>'
                    )
            elif in_admonition and line.strip() == "::":
                in_admonition = False
                new_lines.append("</div>")
            else:
                new_lines.append(line)
        
        return new_lines


def create_markdown_processor(
    *extensions: str
) -> MarkdownRenderer:
    """Create a custom Markdown processor with given extensions."""
    return MarkdownRenderer(list(extensions))