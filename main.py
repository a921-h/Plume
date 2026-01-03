import os
from jinja2 import Environment, FileSystemLoader

# Configuración inicial
def main():
    print("Generador de sitios estáticos en Python")
    generate_site()

def render_template(template_name, context, output_path):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    output = template.render(context)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)

def generate_site():
    # Crear carpeta de salida si no existe
    os.makedirs('dist', exist_ok=True)

    # Leer contenido Markdown
    content_path = 'content'
    for filename in os.listdir(content_path):
        if filename.endswith('.md'):
            with open(os.path.join(content_path, filename), 'r', encoding='utf-8') as f:
                content = f.read()

            # Renderizar plantilla
            context = {'content': content}
            output_file = os.path.join('dist', filename.replace('.md', '.html'))
            render_template('base.html', context, output_file)

    print("Sitio generado en la carpeta 'dist'.")

if __name__ == "__main__":
    main()
