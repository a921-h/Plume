# Generador de Sitios Estáticos

Este proyecto es un generador de sitios estáticos escrito en Python. Permite convertir contenido Markdown en páginas HTML utilizando plantillas personalizables.

## Características
- Convierte archivos Markdown en HTML.
- Utiliza plantillas HTML con Flask y Jinja2.
- Genera un sitio completo en la carpeta dist.

## Requisitos
- Python 3.7 o superior.
- Bibliotecas: `Jinja2`, `Markdown`, `flask`, `setuptools`.

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/makinatetanos/Generador-de-sitios-estaticos.git
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
   python app.py
   ```
4. Encuentra el sitio generado en la carpeta `dist`.

## Contribuciones
¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request.

[Puedes invitarme a un Café](https://checkout.revolut.com/pay/c631503d-1293-41b2-bd1b-7dac308f00ce)

## Licencia
Este proyecto está licenciado bajo la Licencia GPL. Consulta el archivo `LICENSE` para más detalles.
