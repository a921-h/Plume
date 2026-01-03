<<<<<<< HEAD
<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />
</div>

# Run and deploy your AI Studio app

This contains everything you need to run your app locally.

View your app in AI Studio: https://ai.studio/apps/drive/1sg5lTld033L46dML91vvaP7KfM46ISGT

## Run Locally

**Prerequisites:**  Node.js


1. Install dependencies:
   `npm install`
2. Set the `GEMINI_API_KEY` in [.env.local](.env.local) to your Gemini API key
3. Run the app:
   `npm run dev`
=======
# Generador de Sitios Estáticos

Este proyecto es un generador de sitios web estáticos escrito en Python. Permite convertir contenido Markdown en páginas HTML utilizando plantillas personalizables.

## Características
- Convierte archivos Markdown en HTML.
- Utiliza plantillas HTML con Jinja2.
- Genera un sitio completo en la carpeta `dist`.

## Requisitos
- Python 3.7 o superior.
- Bibliotecas: `Jinja2`, `Markdown`.

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/generador-sitios-estaticos.git
   cd generador-sitios-estaticos
   ```
2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
1. Agrega tus archivos Markdown en la carpeta `content`.
2. Personaliza las plantillas en la carpeta `templates`.
3. Ejecuta el script principal:
   ```bash
   python main.py
   ```
4. Encuentra el sitio generado en la carpeta `dist`.

## Contribuciones
¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
>>>>>>> 678ee3a199cc87b7949d29e392a0efddaebacf1f
