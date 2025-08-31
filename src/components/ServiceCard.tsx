import React, { useState } from 'react';
import { ChevronDown, ChevronUp, Zap, Shield, Globe } from 'lucide-react';

interface Service {
  id: string;
  name: string;
  provider: string;
  category: string;
  description: string;
  useCase: string;
  scalability: string;
  durability: string;
  throughput: string;
  costModel: string;
  aiMlIntegration: string;
  realWorldExample: string;
}

interface ServiceCardProps {
  service: Service;
}

const ServiceCard: React.FC<ServiceCardProps> = ({ service }) => {
  const [isExpanded, setIsExpanded] = useState(false);

  const getCategoryColor = (category: string) => {
    const colors = {
      'object-storage': 'bg-blue-500',
      'data-warehouse': 'bg-green-500',
      'nosql': 'bg-purple-500',
      'streaming': 'bg-orange-500',
      'archival': 'bg-gray-500'
    };
    return colors[category as keyof typeof colors] || 'bg-gray-500';
  };

  const getProviderLogo = (provider: string) => {
    const logos = {
      'aws': '🟧',
      'gcp': '🔵',
      'azure': '🔷',
      'multi-cloud': '🌐'
    };
    return logos[provider as keyof typeof logos] || '☁️';
  };

  return (
    <div className="bg-gray-800 rounded-lg border border-gray-700 hover:border-gray-600 transition-all duration-300 hover:shadow-lg">
      <div className="p-6">
        <div className="flex items-start justify-between mb-4">
          <div className="flex items-center space-x-3">
            <span className="text-2xl">{getProviderLogo(service.provider)}</span>
            <div>
              <h3 className="text-xl font-bold text-white">{service.name}</h3>
              <span className={`inline-block px-2 py-1 rounded-full text-xs font-medium text-white ${getCategoryColor(service.category)}`}>
                {service.category.replace('-', ' ').toUpperCase()}
              </span>
            </div>
          </div>
        </div>

        <p className="text-gray-300 mb-4">{service.description}</p>

        <div className="grid grid-cols-2 gap-4 mb-4">
          <div className="flex items-center space-x-2">
            <Zap className="h-4 w-4 text-yellow-400" />
            <span className="text-sm text-gray-400">Throughput: {service.throughput}</span>
          </div>
          <div className="flex items-center space-x-2">
            <Shield className="h-4 w-4 text-green-400" />
            <span className="text-sm text-gray-400">Durability: {service.durability}</span>
          </div>
        </div>

        <button
          onClick={() => setIsExpanded(!isExpanded)}
          className="w-full flex items-center justify-between py-2 px-3 bg-gray-700 rounded-md hover:bg-gray-600 transition-colors duration-200"
        >
          <span className="text-sm font-medium">View Details</span>
          {isExpanded ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
        </button>

        {isExpanded && (
          <div className="mt-4 space-y-4 border-t border-gray-700 pt-4">
            <div>
              <h4 className="font-semibold text-blue-400 mb-2">Primary Use Case</h4>
              <p className="text-sm text-gray-300">{service.useCase}</p>
            </div>
            
            <div>
              <h4 className="font-semibold text-green-400 mb-2">Scalability</h4>
              <p className="text-sm text-gray-300">{service.scalability}</p>
            </div>
            
            <div>
              <h4 className="font-semibold text-purple-400 mb-2">AI/ML Integration</h4>
              <p className="text-sm text-gray-300">{service.aiMlIntegration}</p>
            </div>
            
            <div>
              <h4 className="font-semibold text-orange-400 mb-2">Cost Model</h4>
              <p className="text-sm text-gray-300">{service.costModel}</p>
            </div>
            
            <div className="bg-gray-700 rounded-md p-3">
              <h4 className="font-semibold text-yellow-400 mb-2 flex items-center">
                <Globe className="h-4 w-4 mr-2" />
                Real-World Example
              </h4>
              <p className="text-sm text-gray-300">{service.realWorldExample}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ServiceCard;