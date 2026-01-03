
import React, { useState } from 'react';
import { AppView } from './types';
import Dashboard from './components/Dashboard';
import TemplateGallery from './components/TemplateGallery';
import Documentation from './components/Documentation';
import ContributionSpace from './components/ContributionSpace';
import GeminiAssistant from './components/GeminiAssistant';
import Navigation from './components/Navigation';
import DeploymentView from './components/DeploymentView';

const App: React.FC = () => {
  const [currentView, setCurrentView] = useState<AppView>(AppView.DASHBOARD);

  const renderView = () => {
    switch (currentView) {
      case AppView.DASHBOARD:
        return <Dashboard onViewChange={setCurrentView} />;
      case AppView.TEMPLATES:
        return <TemplateGallery />;
      case AppView.DOCUMENTATION:
        return <Documentation />;
      case AppView.CONTRIBUTE:
        return <ContributionSpace />;
      case AppView.AI_ASSISTANT:
        return <GeminiAssistant />;
      case AppView.DEPLOY:
        return <DeploymentView />;
      default:
        return <Dashboard onViewChange={setCurrentView} />;
    }
  };

  return (
    <div className="min-h-screen flex flex-col md:flex-row bg-slate-50">
      <Navigation currentView={currentView} onViewChange={setCurrentView} />
      <main className="flex-1 overflow-y-auto p-4 md:p-8">
        <div className="max-w-7xl mx-auto">
          {renderView()}
        </div>
      </main>
    </div>
  );
};

export default App;
