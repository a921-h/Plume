# Plume - Modern Python Static Site Generator

<p align="center">
  <img src="https://img.shields.io/pypi/v/plume" alt="PyPI version">
  <img src="https://img.shields.io/pypi/pyversions/plume" alt="Python versions">
  <img src="https://img.shields.io/github/license/a921-h/plume" alt="License">
  <img src="https://img.shields.io/pypi/dm/plume" alt="Downloads">
</p>

Plume es un generador de sitios estáticos moderno escrito en Python. Construye sitios web rápidos y hermosos usando componentes Python y Markdown. Olvídate de los lenguajes de plantillas complicados - usa Python puro.

## Por qué Plume?

- **Python puro** - Sin lenguajes de plantillas como Jinja2 otemplate literals
- **Componentes reutilizables** - Crea tu propia biblioteca de componentes
- **Type hints** - Mejor tooling con tu IDE favorito
- **Extensible** - Fácil de extender con plugins y hooks
- **Minimalista** - Solo lo esencial, sin dependencias innecesarias

## Instalación

### Desde PyPI (recomendado)
```bash
pip install plume
```

### Desde GitHub (últimaversión)
```bash
pip install git+https://github.com/a921-h/plume.git
```

### Desarrollo
```bash
git clone https://github.com/a921-h/plume.git
cd plume
pip install -e .
```

## Inicio Rápido

```bash
# Crear nuevo proyecto
plume new mi-sitio
cd mi-sitio

# Servidor de desarrollo
plume dev

# Build para producción
plume build
```

## Estructura del Proyecto

```
mi-sitio/
├── pages/              # Archivos de páginas Python
│   ├── _layout.py    # Layout base
│   └── index.py      # Página principal
├── content/           # Contenido Markdown
│   └── hello.md     # Artículos/blog
├── static/            # CSS, imágenes, JS
│   └── styles.css   # Estilos
├── dist/              # Output generado (gitignore)
├── plume.config.py  # Configuración
└── .gitignore       # Git ignore
```

## Creando Páginas

### Páginas Python (`pages/index.py`)

```python
from plume import Html, Head, Body, Title, Meta, Link, Main, Div, H1, P, Nav, A, Footer

def render():
    return Html(
        Head(
            Title("Mi Sitio"),
            Meta(name="description", content="Bienvenido a mi sitio"),
            Link(rel="stylesheet", href="/static/styles.css"),
        ),
        Body(
            Div(
                Nav(
                    A("Inicio", href="/"),
                    A("GitHub", href="https://github.com", target="_blank"),
                    cls="nav-links"
                ),
                Main(
                    H1("¡Hola Mundo!"),
                    P("Bienvenido a mi sitio construido con Plume."),
                    cls="content"
                ),
                Footer(
                    P("Construido con Plume"),
                    cls="footer"
                ),
                cls="app"
            ),
            cls="container"
        )
    )
```

### Contenido Markdown (`content/post.md`)

```markdown
---
title: Mi Primer Post
date: 2026-04-26
author: Tu Nombre
tags: python, markdown, plume
description: Una descripción breve del artículo.
---

# Hola

¡Este es mi primer post!

## Subtítulo

Aquí hay más contenido con **negrita** y *cursiva*.

- Elemento 1
- Elemento 2
- Elemento 3

```python
# Código de ejemplo
def hello():
    return "¡Hola!"
```
```

## Componentes Disponibles

Todos los tags HTML están disponibles como componentes Python:

### Estructurales
| Componente | Descripción |
|------------|-------------|
| `Html` | Elemento HTML raíz |
| `Head` | Sección head |
| `Body` | Sección body |
| `Main` | Contenido principal |
| `Section` | Sección |
| `Article` | Artículo |
| `Header` | Encabezado |
| `Footer` | Pie de página |
| `Nav` | Navegación |
| `Div` | Contenedor genérico |

### Texto
| Componente | Descripción |
|------------|-------------|
| `H1` - `H6` | Encabezados |
| `P` | Párrafo |
| `Span` | Texto inline |
| `Blockquote` |Cita |

### Enlaces y Media
| Componente | Descripción |
|------------|-------------|
| `A` | Enlace |
| `Img` | Imagen |

### Listas
| Componente | Descripción |
|------------|-------------|
| `UL` | Lista sin orden |
| `OL` | Lista ordenada |
| `LI` | Elemento de lista |

### Código
| Componente | Descripción |
|------------|-------------|
| `Pre` | Bloque de código |
| `Code` | Código inline |

### Formularios
| Componente | Descripción |
|------------|-------------|
| `Input` | Campo de entrada |
| `Button` | Botón |
| `Textarea` | Área de texto |
| `Select` | Selector |
| `Option` | Opción |

### Atributos

Usa argumentos de keyword para atributos:

```python
# Clase CSS
Div(..., cls="mi-clase")

# ID
Div(..., id="mi-id")

# Atributos personalizados
A(..., href="/pagina", target="_blank", rel="noopener")

# Atributos booleanos
Input(..., disabled=True, checked=False)
```

## Comandos CLI

| Comando | Descripción |
|---------|-------------|
| `plume new <nombre>` | Crear nuevo proyecto |
| `plume dev` | Iniciar servidor con hot reload |
| `plume build` | Generar sitio estático |
| `plume serve` | Servir sitio construído |
| `plume clean` | Limpiar directorio output |
| `plume routes` | Listar todas las rutas |

### Opciones de Build

```bash
plume build --output dist        # Directorio de salida
plume build --minify         # Minificar HTML
plume build --no-minify      # Sin minificar
plume build --incremental  # Builds incrementales
```

### Opciones de Dev Server

```bash
plume dev --host 0.0.0.0    # Host
plume dev --port 8000       # Puerto
plume dev --output dist     # Directorio output
plume dev --watch          # Watch enabled
plume dev --no-watch     # Watch disabled
```

## Configuración

Crea `plume.config.py`:

```python
config = {
    "title": "Mi Sitio",
    "description": "Descripción del sitio",
    "author": "Tu Nombre",
    "base_url": "/",
    "output_dir": "dist",
    "static_dir": "static",
    "pages_dir": "pages",
    "content_dir": "content",
    "templates_dir": "templates",
}

def setup(app):
    """Función llamada antes del build."""
    pass
```

## Frontmatter

Los archivos Markdown soportan frontmatter YAML:

```markdown
---
title: Título del post
date: 2026-04-26
author: Autor
tags: tag1, tag2
description: Descripción SEO
draft: false
---
```

### Campos disponibles

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `title` | string | Título de la página |
| `date` | date | Fecha (YYYY-MM-DD) |
| `author` | string | Autor del contenido |
| `tags` | list | Etiquetas separadas por coma |
| `description` | string | Descripción SEO |
| `draft` | bool | Si es un borrador |

## Despliegue

El directorio `dist/` contiene archivos HTML estáticos listos para desplegar:

### GitHub Pages

```bash
# Build
plume build

# Commit y push
git add dist/
git commit -m "Build"
git push
```

### Netlify

Arrastra el directorio `dist/` a Netlify o conecta tu repositorio GitHub.

### Vercel

```bash
vercel --prod
```

### Cualquier servidor estático

Simplemente sube el contenido de `dist/` a tu servidor.

## Licencia

GPL-3.0 - Ver [LICENSE](LICENSE)

---

## Comparación con otras herramientas

| Característica | Plume | Pelican | MkDocs | Hugo |
|----------------|-------|--------|-------|-------|------|
| Lenguaje | Python | Python | Python | Go |
| Componentes | Python | Jinja2 | Jinja2 | Go |
| Templates | Codificación | Jinja2 | Jinja2 | Markdown |
| Curva de aprendizaje | Baja | Media | Baja | Alta |
| Velocidad | Alta | Media | Alta | Muy alta |

## Demo

```bash
# Crea un proyecto de ejemplo
plume new mi-blog
cd mi-blog

# Añade contenido
echo '---
title: Hola Mundo
---
# Bienvenido
Este es mi primer post.' > content/hello.md

# Build
plume build

# Sirve localmente
plume serve
```

## Estado del Proyecto

Plume está en desarrollo activo. La API puede cambiar en versiones futuras.

## Links

- [ GitHub](https://github.com/a921-h/plume)
- [ Reportar issues](https://github.com/a921-h/plume/issues)
- [ Changelog](https://github.com/a921-h/plume/releases)