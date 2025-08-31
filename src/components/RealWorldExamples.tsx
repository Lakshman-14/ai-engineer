import React, { useState } from 'react';
import { realWorldExamples } from '../data/realWorldExamples';
import { ExternalLink, Users, Database, Cpu } from 'lucide-react';

const RealWorldExamples: React.FC = () => {
  const [selectedCompany, setSelectedCompany] = useState(realWorldExamples[0]);

  return (
    <div className="space-y-6">
      <div className="bg-gray-800 rounded-lg p-6">
        <h2 className="text-2xl font-bold mb-4">Real-World Enterprise Implementations</h2>
        <p className="text-gray-300 mb-6">
          Learn how industry leaders architect their data storage systems to handle 
          billions of users and petabytes of data daily.
        </p>
        
        <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
          {realWorldExamples.map((company) => (
            <button
              key={company.id}
              onClick={() => setSelectedCompany(company)}
              className={`p-4 rounded-lg border-2 transition-all duration-200 ${
                selectedCompany.id === company.id
                  ? 'border-blue-500 bg-blue-900/20'
                  : 'border-gray-600 bg-gray-700 hover:border-gray-500'
              }`}
            >
              <div className="text-center">
                <div className="text-3xl mb-2">{company.logo}</div>
                <h3 className="font-semibold text-white">{company.name}</h3>
                <p className="text-xs text-gray-400">{company.industry}</p>
              </div>
            </button>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 bg-gray-800 rounded-lg p-6">
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-xl font-bold flex items-center">
              <span className="text-3xl mr-3">{selectedCompany.logo}</span>
              {selectedCompany.name} Data Architecture
            </h3>
            <span className="bg-gray-700 px-3 py-1 rounded-full text-sm">{selectedCompany.industry}</span>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div className="bg-gray-700 rounded-lg p-4 text-center">
              <Users className="h-8 w-8 text-blue-400 mx-auto mb-2" />
              <p className="text-sm text-gray-400">Daily Active Users</p>
              <p className="text-xl font-bold text-white">{selectedCompany.scale.users}</p>
            </div>
            <div className="bg-gray-700 rounded-lg p-4 text-center">
              <Database className="h-8 w-8 text-green-400 mx-auto mb-2" />
              <p className="text-sm text-gray-400">Data Volume</p>
              <p className="text-xl font-bold text-white">{selectedCompany.scale.dataVolume}</p>
            </div>
            <div className="bg-gray-700 rounded-lg p-4 text-center">
              <Cpu className="h-8 w-8 text-purple-400 mx-auto mb-2" />
              <p className="text-sm text-gray-400">Daily Requests</p>
              <p className="text-xl font-bold text-white">{selectedCompany.scale.requests}</p>
            </div>
          </div>
          
          <div className="space-y-4">
            <div>
              <h4 className="font-semibold text-blue-400 mb-2">Architecture Overview</h4>
              <p className="text-gray-300">{selectedCompany.architecture.overview}</p>
            </div>
            
            <div>
              <h4 className="font-semibold text-green-400 mb-3">Storage Stack</h4>
              <div className="space-y-2">
                {selectedCompany.architecture.storageStack.map((layer, index) => (
                  <div key={index} className="bg-gray-700 rounded-md p-3">
                    <div className="flex items-center justify-between">
                      <span className="font-medium text-white">{layer.layer}</span>
                      <span className="text-xs bg-gray-600 px-2 py-1 rounded">{layer.technology}</span>
                    </div>
                    <p className="text-sm text-gray-300 mt-1">{layer.purpose}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
        
        <div className="space-y-6">
          <div className="bg-gray-800 rounded-lg p-6">
            <h4 className="font-semibold text-orange-400 mb-4">Key Innovations</h4>
            <div className="space-y-3">
              {selectedCompany.innovations.map((innovation, index) => (
                <div key={index} className="border-l-2 border-orange-500 pl-4">
                  <h5 className="font-medium text-white">{innovation.title}</h5>
                  <p className="text-sm text-gray-300">{innovation.description}</p>
                </div>
              ))}
            </div>
          </div>
          
          <div className="bg-gray-800 rounded-lg p-6">
            <h4 className="font-semibold text-purple-400 mb-4">Challenges Solved</h4>
            <div className="space-y-2">
              {selectedCompany.challenges.map((challenge, index) => (
                <div key={index} className="flex items-start space-x-2">
                  <span className="text-red-400 mt-1">⚡</span>
                  <div>
                    <p className="font-medium text-white">{challenge.problem}</p>
                    <p className="text-sm text-gray-300">{challenge.solution}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
          
          <div className="bg-gray-800 rounded-lg p-6">
            <h4 className="font-semibold text-green-400 mb-4">Performance Metrics</h4>
            <div className="space-y-3">
              {Object.entries(selectedCompany.metrics).map(([key, value]) => (
                <div key={key} className="flex justify-between items-center">
                  <span className="text-gray-300 capitalize">{key.replace(/([A-Z])/g, ' $1')}</span>
                  <span className="font-bold text-white">{value}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RealWorldExamples;