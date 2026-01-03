
import React, { useState } from 'react';

const DeploymentView: React.FC = () => {
  const [copiedIndex, setCopiedIndex] = useState<number | null>(null);

  const steps = [
    {
      title: "Inicializar Repositorio",
      desc: "Prepara el proyecto para el control de versiones.",
      cmd: "git init\ngit add .\ngit commit -m 'feat: initial high-end dev hub structure'"
    },
    {
      title: "Conectar con GitHub",
      desc: "Vincular con tu repositorio remoto.",
      cmd: "git remote add origin https://github.com/tu-usuario/nombre-del-repo.git\ngit branch -M main"
    },
    {
      title: "Publicar Código",
      desc: "Sube los archivos a la nube.",
      cmd: "git push -u origin main"
    }
  ];

  const copyToClipboard = (text: string, index: number) => {
    navigator.clipboard.writeText(text);
    setCopiedIndex(index);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  return (
    <div className="space-y-10 animate-in fade-in slide-in-from-right-8 duration-500 pb-20">
      <header className="flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
        <div className="space-y-2">
          <h2 className="text-3xl font-bold tracking-tight flex items-center gap-3">
            Centro de Despliegue
            <span className="px-2 py-1 rounded bg-indigo-100 text-indigo-700 text-xs font-bold uppercase tracking-widest">DevOps</span>
          </h2>
          <p className="text-slate-500 text-lg">Sigue estos pasos para subir tu proyecto a GitHub profesionalmente.</p>
        </div>
        <div className="flex items-center gap-3 bg-white px-4 py-2 rounded-2xl border border-slate-200 shadow-sm">
          <div className="w-3 h-3 bg-emerald-500 rounded-full animate-pulse"></div>
          <span className="text-sm font-semibold text-slate-700">Listo para Push</span>
        </div>
      </header>

      <div className="grid lg:grid-cols-3 gap-6">
        {steps.map((step, i) => (
          <div key={i} className="bg-white rounded-3xl border border-slate-100 p-6 shadow-sm flex flex-col hover:border-indigo-200 transition-colors group">
            <div className="flex items-center gap-3 mb-4">
              <span className="flex items-center justify-center w-8 h-8 rounded-full bg-slate-900 text-white font-bold text-sm">
                {i + 1}
              </span>
              <h4 className="font-bold text-slate-800">{step.title}</h4>
            </div>
            <p className="text-sm text-slate-500 mb-6">{step.desc}</p>
            <div className="mt-auto relative">
              <pre className="bg-slate-900 text-slate-300 p-4 rounded-xl text-[11px] font-mono overflow-x-auto">
                {step.cmd}
              </pre>
              <button 
                onClick={() => copyToClipboard(step.cmd, i)}
                className="absolute top-2 right-2 p-2 bg-slate-800 hover:bg-slate-700 rounded-lg text-slate-400 transition-colors border border-slate-700"
              >
                {copiedIndex === i ? (
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4 text-emerald-400">
                    <path strokeLinecap="round" strokeLinejoin="round" d="m4.5 12.75 6 6 9-13.5" />
                  </svg>
                ) : (
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M15.75 17.25v3.375c0 .621-.504 1.125-1.125 1.125h-9.75a1.125 1.125 0 0 1-1.125-1.125V7.875c0-.621.504-1.125 1.125-1.125H6.75a9.06 9.06 0 0 1 1.5.124m7.5 10.376h3.375c.621 0 1.125-.504 1.125-1.125V11.25c0-4.46-3.243-8.161-7.5-8.876a9.06 9.06 0 0 0-1.5-.124H9.375c-.621 0-1.125.504-1.125 1.125v3.5m7.5 10.375H9.375a1.125 1.125 0 0 1-1.125-1.125v-9.25m12 6.625v-1.875a3.375 3.375 0 0 0-3.375-3.375h-1.5a1.125 1.125 0 0 1-1.125-1.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H9.75" />
                  </svg>
                )}
              </button>
            </div>
          </div>
        ))}
      </div>

      <div className="bg-indigo-900 rounded-[2.5rem] p-10 text-white relative overflow-hidden">
        <div className="relative z-10 grid md:grid-cols-2 gap-12 items-center">
          <div className="space-y-6">
            <h3 className="text-2xl font-bold italic">"Tu código merece el mejor hogar."</h3>
            <p className="text-indigo-200 leading-relaxed">
              Hemos incluido una configuración de <strong>GitHub Actions</strong> optimizada para ForgePro. 
              Al hacer push, se ejecutará automáticamente un linter y un build test para asegurar 
              que tu código esté siempre listo para producción.
            </p>
            <div className="flex flex-wrap gap-4">
              <button className="bg-white text-indigo-900 px-6 py-3 rounded-xl font-bold flex items-center gap-2 hover:bg-indigo-50 transition-colors">
                Ver CI/CD Config
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-5 h-5">
                  <path d="M10 3a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM10 8.5a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM11.5 15.5a1.5 1.5 0 1 0-3 0 1.5 1.5 0 0 0 3 0Z" />
                </svg>
              </button>
            </div>
          </div>
          <div className="bg-slate-900/50 backdrop-blur rounded-3xl p-6 border border-white/10 shadow-2xl space-y-4 font-mono text-xs">
            <div className="flex gap-2">
              <div className="w-3 h-3 rounded-full bg-red-500/50"></div>
              <div className="w-3 h-3 rounded-full bg-yellow-500/50"></div>
              <div className="w-3 h-3 rounded-full bg-emerald-500/50"></div>
            </div>
            <div className="space-y-2">
              <p className="text-indigo-400 font-bold">$ npm run deploy</p>
              <p className="text-slate-400">&gt; Building for production...</p>
              <p className="text-emerald-400 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4">
                  <path strokeLinecap="round" strokeLinejoin="round" d="m4.5 12.75 6 6 9-13.5" />
                </svg>
                Build successful
              </p>
              <p className="text-slate-400">&gt; Syncing with GitHub API...</p>
              <p className="text-indigo-300 font-bold">Successfully deployed to main branch.</p>
            </div>
          </div>
        </div>
        <div className="absolute top-0 right-0 w-64 h-64 bg-white/5 rounded-full -translate-y-1/2 translate-x-1/2 blur-3xl"></div>
      </div>
    </div>
  );
};

export default DeploymentView;
