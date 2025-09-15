import React, { useState } from 'react';
import Header from './components/Header';
import ServiceCategoryTabs from './components/ServiceCategoryTabs';
import ServiceComparison from './components/ServiceComparison';
import UseCaseExplorer from './components/UseCaseExplorer';
import ArchitectureDiagram from './components/ArchitectureDiagram';
import RealWorldExamples from './components/RealWorldExamples';

function App() {
  const [activeTab, setActiveTab] = useState('overview');

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <Header />
      
      <main className="container mx-auto px-4 py-8">
        <ServiceCategoryTabs activeTab={activeTab} onTabChange={setActiveTab} />
        
        <div className="mt-8">
          {activeTab === 'overview' && <ServiceComparison />}
          {activeTab === 'use-cases' && <UseCaseExplorer />}
          {activeTab === 'architecture' && <ArchitectureDiagram />}
          {activeTab === 'examples' && <RealWorldExamples />}
        </div>
      </main>
    </div>
  );
}

export default App;