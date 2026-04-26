# Changelog

Todos los cambios notables de este proyecto se documentarán en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).

---

## [0.1.0] - 2026-04-26

### Added

- **Framework Plume**: Generador de sitios estáticos moderno
- **Componentes Python**: Todos los tags HTML disponibles como componentes
  - Estructurales: Html, Head, Body, Main, Section, Article, etc.
  - Texto: H1-H6, P, Span, Blockquote
  - Enlaces: A, Img
  - Listas: UL, OL, LI
  - Código: Pre, Code
  - Formularios: Input, Button, Textarea, Select

- **Sistema Markdown**:
  - Rendering a HTML
  - Frontmatter YAML (title, date, author, tags, description, draft)
  - Extensiones: codehilite, tables, extra, nl2br

- **CLI commands**:
  - `plume new <nombre>` - Crear proyecto
  - `plume dev` - Servidor desarrollo
  - `plume build` - Build estático
  - `plume serve` - Servir sitio
  - `plume clean` - Limpiar dist/
  - `plume routes` - Listar rutas

- **Routing**: Sistema basado en archivos
- **Build system**: Builds incrementales con cache
- **PyPI**: Paquete publicado

---

## [0.0.0] - 2026-04-23

### Added

- Versión inicial (proyecto original: Generador de Sitios Estáticos)
- Flask + Jinja2 + Markdown
- Templates Jinja2
- Servidor desarrollo

---

## Upcoming

### Planned

- [ ] Tests unitarios
- [ ] Islands architecture
- [ ] Live reload
- [ ] TypeScript islands
- [ ] Plugins system
- [ ] Temas/plantillas
- [ ] RSS feeds
- [ ] Sitemap
- [ ] SEO optimizations

---

## Formato de versiones

Usamos [Semantic Versioning](https://semver.org/):

- **MAJOR** incompatible API changes
- **MINOR** nuevas funcionalidades compatibles
- **PATCH** correcciones compatibles

---

Para el formato de fechas usamos [ISO 8601](https://es.wikipedia.org/wiki/ISO_8601): YYYY-MM-DD