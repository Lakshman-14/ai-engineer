import React, { useState } from 'react';
import { storageServices } from '../data/storageServices';
import ServiceCard from './ServiceCard';

const ServiceComparison: React.FC = () => {
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [selectedProvider, setSelectedProvider] = useState('all');

  const categories = ['all', 'object-storage', 'data-warehouse', 'nosql', 'streaming', 'archival'];
  const providers = ['all', 'aws', 'gcp', 'azure', 'multi-cloud'];

  const filteredServices = storageServices.filter(service => {
    const categoryMatch = selectedCategory === 'all' || service.category === selectedCategory;
    const providerMatch = selectedProvider === 'all' || service.provider === selectedProvider;
    return categoryMatch && providerMatch;
  });

  return (
    <div className="space-y-6">
      <div className="bg-gray-800 rounded-lg p-6">
        <h2 className="text-2xl font-bold mb-4 text-white">Cloud Storage Service Categories</h2>
        <p className="text-gray-300 mb-6">
          Enterprise-grade storage solutions designed for trillion-scale data management, 
          optimized for different access patterns and use cases.
        </p>
        
        <div className="flex flex-wrap gap-4 mb-6">
          <div className="flex flex-col">
            <label className="text-sm font-medium text-gray-400 mb-2">Category</label>
            <select
              value={selectedCategory}
              onChange={(e) => setSelectedCategory(e.target.value)}
              className="bg-gray-700 border border-gray-600 rounded-md px-3 py-2 text-white focus:ring-2 focus:ring-blue-500"
            >
              <option value="all">All Categories</option>
              <option value="object-storage">Object Storage</option>
              <option value="data-warehouse">Data Warehouse</option>
              <option value="nosql">NoSQL Databases</option>
              <option value="streaming">Real-time Streaming</option>
              <option value="archival">Archival Storage</option>
            </select>
          </div>
          
          <div className="flex flex-col">
            <label className="text-sm font-medium text-gray-400 mb-2">Provider</label>
            <select
              value={selectedProvider}
              onChange={(e) => setSelectedProvider(e.target.value)}
              className="bg-gray-700 border border-gray-600 rounded-md px-3 py-2 text-white focus:ring-2 focus:ring-blue-500"
            >
              <option value="all">All Providers</option>
              <option value="aws">Amazon Web Services</option>
              <option value="gcp">Google Cloud Platform</option>
              <option value="azure">Microsoft Azure</option>
              <option value="multi-cloud">Multi-Cloud</option>
            </select>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredServices.map((service) => (
          <ServiceCard key={service.id} service={service} />
        ))}
      </div>
    </div>
  );
};

export default ServiceComparison;