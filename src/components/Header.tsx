import React from 'react';
import { Database, Cloud, BarChart3 } from 'lucide-react';

const Header: React.FC = () => {
  return (
    <header className="bg-gray-800 border-b border-gray-700">
      <div className="container mx-auto px-4 py-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="flex items-center space-x-2">
              <Database className="h-8 w-8 text-blue-400" />
              <Cloud className="h-8 w-8 text-green-400" />
              <BarChart3 className="h-8 w-8 text-purple-400" />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-white">Enterprise Cloud Storage Architecture</h1>
              <p className="text-gray-300 text-sm">Trillion-scale data storage solutions for AI/ML and analytics</p>
            </div>
          </div>
          <div className="text-right">
            <p className="text-sm text-gray-400">Data Science Professional Guide</p>
            <p className="text-xs text-gray-500">Scalable • Distributed • Fault-Tolerant</p>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;