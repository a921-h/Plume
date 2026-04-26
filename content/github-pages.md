---
title: Cómo publicar tu sitio en GitHub Pages
date: 2026-04-20
author: Abel
tags: GitHub, despliegue, CI/CD
description: Guía paso a paso para publicar el sitio generado en GitHub Pages de forma gratuita.
---

## Introducción

Una vez que hayas generado tu sitio con el comando `flask --app app build`, tendrás una carpeta `dist/` con HTML, CSS y assets listos para publicar.

GitHub Pages te permite hospedar sitios estáticos de forma **gratuita** directamente desde un repositorio.

## Paso 1: Inicializar el repositorio

```bash
git init
git add .
git commit -m "primer commit"
git remote add origin https://github.com/tu-usuario/mi-sitio.git
git push -u origin main
```

## Paso 2: Publicar la carpeta `dist/`

Tienes dos opciones:

### Opción A – Subir `dist/` como rama `gh-pages`

```bash
git subtree push --prefix dist origin gh-pages
```

### Opción B – Configurar GitHub Actions

Crea el archivo `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: flask --app app build
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

## Paso 3: Activar GitHub Pages

1. Ve a **Settings → Pages** en tu repositorio.
2. Selecciona la rama `gh-pages` (o la rama configurada en Actions).
3. ¡Tu sitio estará en `https://tu-usuario.github.io/mi-sitio/`!

> 💡 Con GitHub Actions el sitio se actualiza automáticamente cada vez que haces `push`.
