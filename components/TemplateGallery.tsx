
import React, { useState } from 'react';
import { Template } from '../types';

const TemplateGallery: React.FC = () => {
  const [filter, setFilter] = useState<string>('Todos');
  const [search, setSearch] = useState<string>('');

  const templates: Template[] = [
    {
      id: '1',
      name: 'Nexus Dashboard',
      description: 'Panel de administración premium con gráficos complejos y CRM integrado.',
      category: 'SaaS',
      image: 'https://images.unsplash.com/photo-1551288049-bbbda536639a?auto=format&fit=crop&q=80&w=800',
      features: ['Chart.js', 'Framer Motion', 'Auth Ready']
    },
    {
      id: '2',
      name: 'Zenith Portfolio',
      description: 'Para creativos que buscan un impacto visual minimalista y tipografía elegante.',
      category: 'Portfolio',
      image: 'https://images.unsplash.com/photo-1545235617-9465d2a55698?auto=format&fit=crop&q=80&w=800',
      features: ['GSAP Animations', 'Dark Mode', 'Responsive']
    },
    {
      id: '3',
      name: 'Aura Market',
      description: 'E-commerce completo con carrito, filtros dinámicos y pasarela de pago.',
      category: 'E-commerce',
      image: 'https://images.unsplash.com/photo-1472851294608-062f824d29cc?auto=format&fit=crop&q=80&w=800',
      features: ['Stripe Integration', 'Wishlist', 'Analytics']
    },
    {
      id: '4',
      name: 'Lumina Landing',
      description: 'Landing page optimizada para conversión con tests A/B pre-configurados.',
      category: 'Landing',
      image: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=800',
      features: ['SEO Optimized', 'Tailwind', 'Lead Gen']
    }
  ];

  const filteredTemplates = templates.filter(t => 
    (filter === 'Todos' || t.category === filter) &&
    (t.name.toLowerCase().includes(search.toLowerCase()) || t.description.toLowerCase().includes(search.toLowerCase()))
  );

  return (
    <div className="space-y-8 animate-in slide-in-from-bottom-4 duration-500">
      <header className="flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <h2 className="text-3xl font-bold tracking-tight">Galería de Plantillas</h2>
          <p className="text-slate-500 mt-2">Plantillas de alta fidelidad para acelerar tu desarrollo.</p>
        </div>
        <div className="relative">
          <input 
            type="text" 
            placeholder="Buscar plantillas..." 
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="pl-10 pr-4 py-2 rounded-xl bg-white border border-slate-200 focus:ring-2 focus:ring-indigo-500 focus:outline-none w-full md:w-64 shadow-sm"
          />
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-5 h-5 absolute left-3 top-2.5 text-slate-400">
            <path strokeLinecap="round" strokeLinejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
          </svg>
        </div>
      </header>

      <div className="flex gap-2 overflow-x-auto pb-2 scrollbar-hide">
        {['Todos', 'SaaS', 'Landing', 'E-commerce', 'Portfolio'].map((cat) => (
          <button
            key={cat}
            onClick={() => setFilter(cat)}
            className={`px-5 py-2 rounded-full text-sm font-semibold transition-all whitespace-nowrap ${
              filter === cat ? 'bg-slate-900 text-white shadow-md' : 'bg-white text-slate-600 hover:bg-slate-50 border border-slate-200'
            }`}
          >
            {cat}
          </button>
        ))}
      </div>

      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        {filteredTemplates.map((template) => (
          <div key={template.id} className="bg-white rounded-3xl overflow-hidden border border-slate-100 shadow-sm hover:shadow-xl transition-all duration-300 group flex flex-col">
            <div className="h-48 overflow-hidden relative">
              <img src={template.image} alt={template.name} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
              <div className="absolute top-4 left-4">
                <span className="bg-white/90 backdrop-blur px-3 py-1 rounded-full text-[10px] font-bold uppercase text-slate-800 shadow-sm">
                  {template.category}
                </span>
              </div>
            </div>
            <div className="p-6 flex-1 flex flex-col">
              <h4 className="text-xl font-bold text-slate-800">{template.name}</h4>
              <p className="text-slate-500 text-sm mt-2 flex-1">{template.description}</p>
              
              <div className="mt-4 flex flex-wrap gap-2">
                {template.features.map(f => (
                  <span key={f} className="text-[10px] bg-slate-50 text-slate-500 px-2 py-1 rounded border border-slate-100">{f}</span>
                ))}
              </div>

              <div className="mt-6 flex gap-3">
                <button className="flex-1 bg-indigo-600 text-white py-2.5 rounded-xl text-sm font-semibold hover:bg-indigo-700 transition-colors">
                  Vista Previa
                </button>
                <button className="px-3 bg-slate-100 text-slate-700 rounded-xl hover:bg-slate-200 transition-colors">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-5 h-5">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
      
      {filteredTemplates.length === 0 && (
        <div className="py-20 text-center space-y-4">
          <div className="bg-slate-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto text-slate-400">
             <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-8 h-8">
              <path strokeLinecap="round" strokeLinejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
            </svg>
          </div>
          <p className="text-slate-500 font-medium">No se encontraron plantillas que coincidan con tu búsqueda.</p>
        </div>
      )}
    </div>
  );
};

export default TemplateGallery;
