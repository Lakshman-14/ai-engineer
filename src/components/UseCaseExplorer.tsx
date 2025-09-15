import React, { useState } from 'react';
import { useCases } from '../data/useCases';

const UseCaseExplorer: React.FC = () => {
  const [selectedUseCase, setSelectedUseCase] = useState(useCases[0]);

  return (
    <div className="space-y-6">
      <div className="bg-gray-800 rounded-lg p-6">
        <h2 className="text-2xl font-bold mb-4">Access Pattern Analysis</h2>
        <p className="text-gray-300 mb-6">
          Different data access patterns require different storage architectures. 
          Explore how major companies optimize their storage strategies.
        </p>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {useCases.map((useCase) => (
            <button
              key={useCase.id}
              onClick={() => setSelectedUseCase(useCase)}
              className={`p-4 rounded-lg border-2 transition-all duration-200 text-left ${
                selectedUseCase.id === useCase.id
                  ? 'border-blue-500 bg-blue-900/20'
                  : 'border-gray-600 bg-gray-700 hover:border-gray-500'
              }`}
            >
              <div className="flex items-center space-x-3 mb-2">
                <span className="text-2xl">{useCase.icon}</span>
                <h3 className="font-semibold">{useCase.title}</h3>
              </div>
              <p className="text-sm text-gray-400">{useCase.pattern}</p>
            </button>
          ))}
        </div>
      </div>

      <div className="bg-gray-800 rounded-lg p-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div>
            <h3 className="text-xl font-bold mb-4 flex items-center">
              <span className="text-2xl mr-3">{selectedUseCase.icon}</span>
              {selectedUseCase.title}
            </h3>
            <div className="space-y-4">
              <div>
                <h4 className="font-semibold text-blue-400 mb-2">Access Pattern</h4>
                <p className="text-gray-300">{selectedUseCase.pattern}</p>
              </div>
              <div>
                <h4 className="font-semibold text-green-400 mb-2">Data Characteristics</h4>
                <p className="text-gray-300">{selectedUseCase.dataCharacteristics}</p>
              </div>
              <div>
                <h4 className="font-semibold text-purple-400 mb-2">Performance Requirements</h4>
                <p className="text-gray-300">{selectedUseCase.performance}</p>
              </div>
            </div>
          </div>
          
          <div>
            <h4 className="font-semibold text-orange-400 mb-4">Recommended Architecture Stack</h4>
            <div className="space-y-3">
              {selectedUseCase.recommendedServices.map((service, index) => (
                <div key={index} className="bg-gray-700 rounded-md p-3">
                  <div className="flex items-center justify-between mb-2">
                    <span className="font-medium text-white">{service.layer}</span>
                    <span className="text-xs bg-gray-600 px-2 py-1 rounded">{service.provider}</span>
                  </div>
                  <p className="text-sm text-gray-300">{service.service}</p>
                  <p className="text-xs text-gray-400 mt-1">{service.reason}</p>
                </div>
              ))}
            </div>
            
            <div className="mt-6 p-4 bg-blue-900/20 border border-blue-700 rounded-lg">
              <h5 className="font-semibold text-blue-400 mb-2">Cost Optimization Strategy</h5>
              <p className="text-sm text-gray-300">{selectedUseCase.costOptimization}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UseCaseExplorer;