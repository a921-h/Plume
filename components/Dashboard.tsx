
import React from 'react';
import { AppView } from '../types';

interface DashboardProps {
  onViewChange: (view: AppView) => void;
}

const Dashboard: React.FC<DashboardProps> = ({ onViewChange }) => {
  const stats = [
    { label: 'Plantillas', value: '24+', color: 'bg-indigo-500' },
    { label: 'Componentes', value: '150+', color: 'bg-emerald-500' },
    { label: 'Colaboradores', value: '12', color: 'bg-orange-500' },
    { label: 'Descargas', value: '1.2k', color: 'bg-blue-500' },
  ];

  return (
    <div className="space-y-8 animate-in fade-in duration-500">
      <header>
        <h2 className="text-3xl font-bold tracking-tight">Bienvenido a ForgePro</h2>
        <p className="text-slate-500 mt-2 text-lg">Tu ecosistema avanzado para el desarrollo frontend moderno.</p>
      </header>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {stats.map((stat, i) => (
          <div key={i} className="bg-white p-6 rounded-3xl shadow-sm border border-slate-100 flex flex-col justify-center">
            <span className="text-slate-500 text-sm font-medium">{stat.label}</span>
            <div className="flex items-center gap-2 mt-1">
              <span className={`w-2 h-2 rounded-full ${stat.color}`}></span>
              <span className="text-2xl font-bold">{stat.value}</span>
            </div>
          </div>
        ))}
      </div>

      <div className="grid md:grid-cols-2 gap-8">
        <section className="bg-white p-8 rounded-3xl shadow-sm border border-slate-100 space-y-4">
          <h3 className="text-xl font-bold">Comienza Ahora</h3>
          <p className="text-slate-600 leading-relaxed">
            Explora nuestra biblioteca de plantillas optimizadas para React, Tailwind CSS y TypeScript. 
            Todas nuestras soluciones incluyen arquitecturas limpias y patrones de diseño modernos.
          </p>
          <div className="pt-4 flex flex-wrap gap-4">
            <button 
              onClick={() => onViewChange(AppView.TEMPLATES)}
              className="bg-indigo-600 text-white px-6 py-3 rounded-xl font-semibold hover:bg-indigo-700 transition-colors shadow-lg shadow-indigo-200"
            >
              Explorar Plantillas
            </button>
            <button 
              onClick={() => onViewChange(AppView.DOCUMENTATION)}
              className="bg-slate-100 text-slate-700 px-6 py-3 rounded-xl font-semibold hover:bg-slate-200 transition-colors"
            >
              Ver Documentación
            </button>
          </div>
        </section>

        <section className="bg-indigo-900 p-8 rounded-3xl shadow-xl text-white relative overflow-hidden group">
          <div className="relative z-10 space-y-4">
            <h3 className="text-xl font-bold">¿Necesitas ayuda con el código?</h3>
            <p className="text-indigo-200 leading-relaxed">
              Nuestro asistente inteligente basado en Gemini puede ayudarte a generar componentes, 
              refactorizar código o explicar conceptos complejos en segundos.
            </p>
            <button 
              onClick={() => onViewChange(AppView.AI_ASSISTANT)}
              className="bg-white text-indigo-900 px-6 py-3 rounded-xl font-semibold hover:bg-indigo-50 transition-colors inline-flex items-center gap-2"
            >
              Hablar con la IA
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-5 h-5">
                <path fillRule="evenodd" d="M2 10a.75.75 0 0 1 .75-.75h12.59l-2.1-1.95a.75.75 0 1 1 1.02-1.1l3.5 3.25a.75.75 0 0 1 0 1.1l-3.5 3.25a.75.75 0 1 1-1.02-1.1l2.1-1.95H2.75A.75.75 0 0 1 2 10Z" clipRule="evenodd" />
              </svg>
            </button>
          </div>
          <div className="absolute -right-10 -bottom-10 w-48 h-48 bg-indigo-500 rounded-full blur-3xl opacity-20 group-hover:opacity-40 transition-opacity"></div>
        </section>
      </div>
      
      <section>
        <div className="flex items-center justify-between mb-6">
          <h3 className="text-xl font-bold">Últimas Plantillas</h3>
          <button className="text-indigo-600 text-sm font-semibold hover:underline" onClick={() => onViewChange(AppView.TEMPLATES)}>
            Ver todas
          </button>
        </div>
        <div className="grid md:grid-cols-3 gap-6">
          {[
            { name: 'SaaS Modern Dash', category: 'SaaS', color: 'bg-blue-50' },
            { name: 'Portfolio Minimalista', category: 'Portfolio', color: 'bg-purple-50' },
            { name: 'E-commerce Flex', category: 'E-commerce', color: 'bg-emerald-50' },
          ].map((item, i) => (
            <div key={i} className={`p-6 rounded-3xl ${item.color} border border-slate-200/50 hover:shadow-md transition-shadow cursor-pointer`}>
              <span className="px-2 py-1 rounded-md bg-white text-[10px] font-bold uppercase tracking-wider text-slate-500 border border-slate-100">
                {item.category}
              </span>
              <h4 className="mt-4 font-bold text-slate-800">{item.name}</h4>
              <p className="text-sm text-slate-500 mt-1">Diseño adaptativo, Next.js 14 ready.</p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

export default Dashboard;
