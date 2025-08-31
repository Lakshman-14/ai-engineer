import React, { useState } from 'react';
import { architecturePatterns } from '../data/architecturePatterns';

const ArchitectureDiagram: React.FC = () => {
  const [selectedPattern, setSelectedPattern] = useState(architecturePatterns[0]);

  return (
    <div className="space-y-6">
      <div className="bg-gray-800 rounded-lg p-6">
        <h2 className="text-2xl font-bold mb-4">Storage Architecture Patterns</h2>
        <p className="text-gray-300 mb-6">
          Explore different architectural patterns used by leading tech companies 
          for managing trillion-scale data workloads.
        </p>
        
        <div className="flex flex-wrap gap-3 mb-6">
          {architecturePatterns.map((pattern) => (
            <button
              key={pattern.id}
              onClick={() => setSelectedPattern(pattern)}
              className={`px-4 py-2 rounded-lg transition-all duration-200 ${
                selectedPattern.id === pattern.id
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-700 text-gray-300 hover:bg-gray-600'
              }`}
            >
              {pattern.name}
            </button>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-gray-800 rounded-lg p-6">
          <h3 className="text-xl font-bold mb-4">{selectedPattern.name}</h3>
          <p className="text-gray-300 mb-4">{selectedPattern.description}</p>
          
          <div className="space-y-3">
            <div>
              <h4 className="font-semibold text-blue-400 mb-2">Key Benefits</h4>
              <ul className="space-y-1">
                {selectedPattern.benefits.map((benefit, index) => (
                  <li key={index} className="text-sm text-gray-300 flex items-start">
                    <span className="text-green-400 mr-2">✓</span>
                    {benefit}
                  </li>
                ))}
              </ul>
            </div>
            
            <div>
              <h4 className="font-semibold text-purple-400 mb-2">Use Cases</h4>
              <ul className="space-y-1">
                {selectedPattern.useCases.map((useCase, index) => (
                  <li key={index} className="text-sm text-gray-300 flex items-start">
                    <span className="text-blue-400 mr-2">•</span>
                    {useCase}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
        
        <div className="bg-gray-800 rounded-lg p-6">
          <h4 className="font-semibold text-orange-400 mb-4">Architecture Flow</h4>
          <div className="space-y-4">
            {selectedPattern.layers.map((layer, index) => (
              <div key={index} className="relative">
                <div className="bg-gray-700 rounded-lg p-4 border-l-4 border-blue-500">
                  <div className="flex items-center justify-between mb-2">
                    <h5 className="font-medium text-white">{layer.name}</h5>
                    <span className="text-xs bg-gray-600 px-2 py-1 rounded">{layer.type}</span>
                  </div>
                  <p className="text-sm text-gray-300 mb-2">{layer.description}</p>
                  <div className="flex flex-wrap gap-2">
                    {layer.technologies.map((tech, techIndex) => (
                      <span key={techIndex} className="text-xs bg-blue-900/30 text-blue-300 px-2 py-1 rounded">
                        {tech}
                      </span>
                    ))}
                  </div>
                </div>
                {index < selectedPattern.layers.length - 1 && (
                  <div className="flex justify-center py-2">
                    <div className="w-px h-4 bg-gray-600"></div>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </div>
      
      <div className="bg-gradient-to-r from-blue-900/20 to-purple-900/20 border border-blue-700 rounded-lg p-6">
        <h4 className="font-semibold text-blue-400 mb-3">Implementation Considerations</h4>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <h5 className="font-medium text-white mb-2">Fault Tolerance</h5>
            <p className="text-sm text-gray-300">{selectedPattern.faultTolerance}</p>
          </div>
          <div>
            <h5 className="font-medium text-white mb-2">Scaling Strategy</h5>
            <p className="text-sm text-gray-300">{selectedPattern.scalingStrategy}</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ArchitectureDiagram;