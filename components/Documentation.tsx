
import React from 'react';

const Documentation: React.FC = () => {
  const sections = [
    { title: 'Primeros Pasos', items: ['Instalación', 'Configuración', 'Arquitectura'] },
    { title: 'Componentes', items: ['Navegación', 'Layouts', 'UI Elements', 'Formularios'] },
    { title: 'Estilos', items: ['Tailwind CSS', 'Temas', 'Animaciones'] },
    { title: 'Avanzado', items: ['Integración API', 'Webhooks', 'Deployment'] },
  ];

  return (
    <div className="flex flex-col lg:flex-row gap-8 animate-in fade-in slide-in-from-left-4 duration-500">
      <aside className="w-full lg:w-64 flex-shrink-0">
        <div className="sticky top-24 space-y-8">
          {sections.map(section => (
            <div key={section.title} className="space-y-3">
              <h5 className="text-xs font-bold uppercase tracking-wider text-slate-400 px-4">{section.title}</h5>
              <ul className="space-y-1">
                {section.items.map(item => (
                  <li key={item}>
                    <button className="w-full text-left px-4 py-2 text-sm text-slate-600 hover:text-indigo-600 hover:bg-indigo-50 rounded-lg transition-colors font-medium">
                      {item}
                    </button>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </aside>

      <div className="flex-1 bg-white rounded-3xl p-8 md:p-12 border border-slate-100 shadow-sm prose prose-slate max-w-none">
        <h2 className="text-3xl font-bold mb-6">Guía de Inicio Rápido</h2>
        <p className="text-slate-600 text-lg leading-relaxed">
          Bienvenido a la documentación oficial de ForgePro. Este proyecto está diseñado para proporcionar a los desarrolladores
          herramientas de vanguardia para crear aplicaciones web escalables y estéticamente impecables.
        </p>
        
        <div className="my-8 p-6 bg-slate-50 border-l-4 border-indigo-500 rounded-r-2xl">
          <p className="text-sm text-slate-700 italic m-0">
            "Nuestra misión es reducir el tiempo de 'boilerplate' y permitirte enfocarte en lo que realmente importa: la lógica de tu negocio."
          </p>
        </div>

        <h3 className="text-xl font-bold mt-10 mb-4">Estructura del Proyecto</h3>
        <p className="text-slate-600">
          Todas nuestras plantillas siguen una estructura modular estandarizada:
        </p>
        <div className="bg-slate-900 text-slate-300 p-6 rounded-2xl font-mono text-sm overflow-x-auto my-6 shadow-inner">
          <pre className="m-0">{`project-root/
├── src/
│   ├── components/    # Componentes UI reutilizables
│   ├── hooks/         # Custom hooks de React
│   ├── layouts/       # Esquemas de página
│   ├── services/      # Llamadas a API y servicios
│   ├── types/         # Definiciones TypeScript
│   └── utils/         # Funciones de utilidad
├── public/            # Assets estáticos
└── tailwind.config.js # Configuración de estilos`}</pre>
        </div>

        <h3 className="text-xl font-bold mt-10 mb-4">Requisitos Previos</h3>
        <ul className="list-disc pl-5 space-y-2 text-slate-600">
          <li>Node.js 18.x o superior</li>
          <li>Conocimientos sólidos de React y TypeScript</li>
          <li>Familiaridad con Tailwind CSS</li>
        </ul>

        <div className="mt-12 pt-12 border-t border-slate-100 flex justify-between items-center text-sm text-slate-400">
          <span>Última actualización: 20 de Mayo, 2024</span>
          <button className="text-indigo-600 font-semibold hover:underline">¿Te ha resultado útil?</button>
        </div>
      </div>
    </div>
  );
};

export default Documentation;
