
import React from 'react';

const ContributionSpace: React.FC = () => {
  return (
    <div className="max-w-4xl mx-auto space-y-12 animate-in zoom-in-95 duration-500">
      <section className="text-center space-y-4">
        <h2 className="text-4xl font-bold tracking-tight">Construyamos juntos</h2>
        <p className="text-slate-500 text-lg max-w-2xl mx-auto">
          ForgePro es un proyecto impulsado por la comunidad. Tus aportes ayudan a miles de desarrolladores a trabajar mejor.
        </p>
      </section>

      <div className="grid md:grid-cols-2 gap-8">
        <div className="bg-white p-8 rounded-3xl border border-slate-100 shadow-sm space-y-6">
          <div className="w-12 h-12 bg-indigo-100 text-indigo-600 rounded-2xl flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-6 h-6">
              <path strokeLinecap="round" strokeLinejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
            </svg>
          </div>
          <h3 className="text-xl font-bold">Añadir una Plantilla</h3>
          <p className="text-slate-600 text-sm leading-relaxed">
            ¿Has creado algo increíble? Comparte tu plantilla con nosotros. Revisamos cada envío para asegurar la calidad y el cumplimiento de las guías de estilo.
          </p>
          <ul className="space-y-2 text-sm text-slate-500">
            <li className="flex items-center gap-2">
              <span className="text-indigo-500">✓</span> Código limpio y documentado
            </li>
            <li className="flex items-center gap-2">
              <span className="text-indigo-500">✓</span> Totalmente responsivo
            </li>
            <li className="flex items-center gap-2">
              <span className="text-indigo-500">✓</span> Assets con licencia libre
            </li>
          </ul>
          <button className="w-full bg-slate-900 text-white py-3 rounded-xl font-semibold hover:bg-slate-800 transition-colors">
            Enviar Plantilla
          </button>
        </div>

        <div className="bg-white p-8 rounded-3xl border border-slate-100 shadow-sm space-y-6">
          <div className="w-12 h-12 bg-emerald-100 text-emerald-600 rounded-2xl flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-6 h-6">
              <path strokeLinecap="round" strokeLinejoin="round" d="M11.48 3.499a.562.562 0 0 1 1.04 0l2.125 5.111a.563.563 0 0 0 .475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 0 0-.182.557l1.285 5.385a.562.562 0 0 1-.84.61l-4.725-2.885a.562.562 0 0 0-.586 0L6.982 20.54a.562.562 0 0 1-.84-.61l1.285-5.386a.562.562 0 0 0-.182-.557l-4.204-3.602a.563.563 0 0 1 .321-.988l5.518-.442a.563.563 0 0 0 .475-.345L11.48 3.5Z" />
            </svg>
          </div>
          <h3 className="text-xl font-bold">Reportar Bugs / Sugerencias</h3>
          <p className="text-slate-600 text-sm leading-relaxed">
            Tu feedback es vital para mejorar ForgePro. Si encuentras un error o tienes una idea para una nueva característica, abre un issue en GitHub.
          </p>
          <div className="pt-4">
            <a 
              href="https://github.com/makinatetanos/Generador-de-sitios-estaticos/issues" 
              target="_blank" 
              className="inline-flex items-center gap-2 text-indigo-600 font-bold hover:underline"
            >
              Abrir Issue en GitHub
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-4 h-4">
                <path strokeLinecap="round" strokeLinejoin="round" d="M13.5 6H5.25A2.25 2.25 0 0 0 3 8.25v10.5A2.25 2.25 0 0 0 5.25 21h10.5A2.25 2.25 0 0 0 18 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25" />
              </svg>
            </a>
          </div>
        </div>
      </div>

      <section className="bg-slate-50 p-8 rounded-3xl border border-slate-200">
        <h3 className="text-xl font-bold mb-6 text-center">Nuestros Colaboradores Top</h3>
        <div className="flex flex-wrap justify-center gap-6">
          {[1, 2, 3, 4, 5].map(i => (
            <div key={i} className="flex flex-col items-center gap-2">
              <div className="w-14 h-14 rounded-full bg-indigo-200 border-2 border-white shadow-sm overflow-hidden">
                <img src={`https://i.pravatar.cc/150?u=${i}`} alt="Avatar" />
              </div>
              <span className="text-xs font-semibold text-slate-600">Dev_{i}00</span>
            </div>
          ))}
          <div className="flex flex-col items-center gap-2">
            <div className="w-14 h-14 rounded-full bg-slate-200 border-2 border-dashed border-slate-400 flex items-center justify-center text-slate-500 cursor-pointer hover:bg-slate-300 transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-6 h-6">
                <path strokeLinecap="round" strokeLinejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
              </svg>
            </div>
            <span className="text-xs font-semibold text-slate-400">Tú</span>
          </div>
        </div>
      </section>
    </div>
  );
};

export default ContributionSpace;
