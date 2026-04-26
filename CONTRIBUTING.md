# Contribuir a Plume

¡Gracias por tu interés en contribuir a Plume! Este documento te ayudará a empezar.

## Código de Conducta

Al participar en este proyecto, te comprometees a respetar nuestro [Código de Conducta](https://github.com/a921-h/plume/blob/master/CODE_OF_CONDUCT.md).

## ¿Cómo contribuir?

### 1. Reportar Bugs

Si encuentras un bug, por favor abre un issue en [GitHub](https://github.com/a921-h/plume/issues).

Incluye:
- Descripción clara del problema
- Pasos para reproducir
- Comportamiento esperado vs actual
- Versión de Python y Plume

### 2. Sugerir Features

¿Tienes una idea para mejorar Plume? Abre un issue con:
- Descripción de la feature
- Casos de uso
- Posibles implementaciones

### 3. Pull Requests

1. **Fork** el repo
2. Crea tu branch: `git checkout -b feature/mi-feature`
3. Hacelcommit de tus cambios: `git commit -m 'Add mi feature'`
4. Push a tu fork: `git push origin feature/mi-feature`
5. Abre un **Pull Request**

### Requirements

- Código en Python 3.10+
- Sigue el estilo del proyecto
- Añade tests si es posible
- Actualiza documentación si es necesario

### Estilo de código

```bash
# Verifica el código
ruff check plume/

# Formatea
ruff format plume/
```

### Tests

```bash
# Ejecutar tests
pytest

# Coverage
pytest --cov=plume
```

## Desarrollo local

```bash
# Clonar
git clone https://github.com/a921-h/plume.git
cd plume

# Instalar dependencias
pip install -e ".[dev]"

# Instalar pre-commit hooks
pre-commit install

# Build del paquete
python -m build

# Probar CLI
python -m plume --version
```

## Commits

Usamos [Conventional Commits](https://conventionalcommits.org):

```
feat: nueva feature
fix: corrección de bug
docs: documentación
style: formato de código
refactor: refactorización
test: tests
chore: mantenimiento
```

Ejemplos:
```
feat: Add new Button component
fix: Fix markdown parsing error
docs: Update installation guide
```

## Reconocimiento

Todos los contribuidores serán listados en el README y en las releases.

---

## Preguntas?

- Abre un issue para preguntas generales
- Para discussions, usa GitHub Discussions

¡esperamos tu contribución!