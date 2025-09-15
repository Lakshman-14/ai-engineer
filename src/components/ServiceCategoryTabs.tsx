import React from 'react';

interface ServiceCategoryTabsProps {
  activeTab: string;
  onTabChange: (tab: string) => void;
}

const tabs = [
  { id: 'overview', label: 'Service Overview', icon: '📊' },
  { id: 'use-cases', label: 'Use Cases', icon: '🎯' },
  { id: 'architecture', label: 'Architecture', icon: '🏗️' },
  { id: 'examples', label: 'Real Examples', icon: '🏢' }
];

const ServiceCategoryTabs: React.FC<ServiceCategoryTabsProps> = ({ activeTab, onTabChange }) => {
  return (
    <div className="border-b border-gray-700">
      <nav className="flex space-x-8">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => onTabChange(tab.id)}
            className={`py-4 px-2 border-b-2 font-medium text-sm transition-colors duration-200 ${
              activeTab === tab.id
                ? 'border-blue-400 text-blue-400'
                : 'border-transparent text-gray-400 hover:text-gray-300 hover:border-gray-600'
            }`}
          >
            <span className="mr-2">{tab.icon}</span>
            {tab.label}
          </button>
        ))}
      </nav>
    </div>
  );
};

export default ServiceCategoryTabs;