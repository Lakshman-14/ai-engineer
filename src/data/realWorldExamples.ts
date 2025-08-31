export const realWorldExamples = [
  {
    id: 'netflix',
    name: 'Netflix',
    logo: '🎬',
    industry: 'Streaming Media',
    scale: {
      users: '230M+',
      dataVolume: '1+ PB daily',
      requests: '1B+ per day'
    },
    architecture: {
      overview: 'Multi-layered architecture with separate systems for content delivery, user data, and analytics. Uses microservices with event-driven communication.',
      storageStack: [
        {
          layer: 'Content Storage',
          technology: 'Amazon S3 + CloudFront CDN',
          purpose: 'Global content distribution with 99.9% availability'
        },
        {
          layer: 'User Data',
          technology: 'Amazon DynamoDB',
          purpose: 'User profiles, viewing history, preferences'
        },
        {
          layer: 'Analytics Platform',
          technology: 'Amazon S3 + Apache Spark',
          purpose: 'Recommendation algorithms and content analytics'
        },
        {
          layer: 'Real-time Events',
          technology: 'Apache Kafka + Amazon Kinesis',
          purpose: 'User interaction tracking and real-time personalization'
        }
      ]
    },
    innovations: [
      {
        title: 'Adaptive Bitrate Streaming',
        description: 'Dynamic content encoding stored across global CDN for optimal streaming quality'
      },
      {
        title: 'Chaos Engineering',
        description: 'Proactive failure testing to ensure system resilience at massive scale'
      },
      {
        title: 'Machine Learning Pipeline',
        description: 'Real-time recommendation engine processing 500+ billion events daily'
      }
    ],
    challenges: [
      {
        problem: 'Global Content Distribution',
        solution: 'Multi-tier CDN with intelligent caching algorithms across 190+ countries'
      },
      {
        problem: 'Real-time Personalization',
        solution: 'Event-driven architecture with sub-100ms recommendation updates'
      },
      {
        problem: 'Data Privacy Compliance',
        solution: 'Data residency controls with region-specific storage and processing'
      }
    ],
    metrics: {
      globalAvailability: '99.9%',
      streamingLatency: '<2 seconds',
      recommendationLatency: '<100ms',
      dataReplication: '3+ regions',
      costPerUser: '$3.50/month'
    }
  },
  {
    id: 'meta',
    name: 'Meta (Facebook)',
    logo: '📘',
    industry: 'Social Media',
    scale: {
      users: '3.8B+',
      dataVolume: '4+ PB daily',
      requests: '100B+ per day'
    },
    architecture: {
      overview: 'Massive scale social graph storage with real-time feed generation. Custom-built systems optimized for social data patterns.',
      storageStack: [
        {
          layer: 'Social Graph',
          technology: 'TAO (Custom Graph Database)',
          purpose: 'Billions of social connections with sub-millisecond access'
        },
        {
          layer: 'Media Storage',
          technology: 'Haystack (Custom Object Store)',
          purpose: 'Photos and videos with efficient small-file optimization'
        },
        {
          layer: 'Analytics Warehouse',
          technology: 'Presto + Apache Hive',
          purpose: 'Ad targeting and user behavior analytics'
        },
        {
          layer: 'Real-time Messaging',
          technology: 'Apache Kafka + Custom Streaming',
          purpose: 'News feed updates and real-time notifications'
        }
      ]
    },
    innovations: [
      {
        title: 'TAO Graph Database',
        description: 'Custom-built distributed graph database handling 1+ trillion edges'
      },
      {
        title: 'Haystack Object Storage',
        description: 'Optimized for billions of small files with 80% storage efficiency improvement'
      },
      {
        title: 'Presto Query Engine',
        description: 'Interactive analytics on petabyte-scale data with SQL interface'
      }
    ],
    challenges: [
      {
        problem: 'Social Graph Scaling',
        solution: 'Custom TAO database with intelligent caching and geographic distribution'
      },
      {
        problem: 'Photo/Video Storage',
        solution: 'Haystack system optimized for billions of small media files'
      },
      {
        problem: 'Real-time Feed Generation',
        solution: 'Multi-layer caching with predictive content pre-loading'
      }
    ],
    metrics: {
      globalAvailability: '99.95%',
      feedLatency: '<200ms',
      photoUploadTime: '<3 seconds',
      graphQueryLatency: '<1ms',
      storageEfficiency: '80% improvement'
    }
  },
  {
    id: 'amazon',
    name: 'Amazon',
    logo: '📦',
    industry: 'E-commerce',
    scale: {
      users: '400M+',
      dataVolume: '10+ PB daily',
      requests: '10B+ per day'
    },
    architecture: {
      overview: 'Service-oriented architecture with thousands of microservices. Each service owns its data with eventual consistency patterns.',
      storageStack: [
        {
          layer: 'Product Catalog',
          technology: 'Amazon DynamoDB',
          purpose: 'Product information with global secondary indexes'
        },
        {
          layer: 'Order Management',
          technology: 'Amazon RDS + DynamoDB',
          purpose: 'Transactional order processing with ACID guarantees'
        },
        {
          layer: 'Recommendation Engine',
          technology: 'Amazon EMR + S3',
          purpose: 'Machine learning on customer behavior data'
        },
        {
          layer: 'Search Index',
          technology: 'Amazon Elasticsearch',
          purpose: 'Real-time product search with faceted navigation'
        }
      ]
    },
    innovations: [
      {
        title: 'DynamoDB',
        description: 'Purpose-built NoSQL database now used by thousands of AWS customers'
      },
      {
        title: 'Microservices Architecture',
        description: 'Pioneered service-oriented architecture with database-per-service pattern'
      },
      {
        title: 'Personalization at Scale',
        description: 'Real-time recommendation engine processing 150+ million customer interactions'
      }
    ],
    challenges: [
      {
        problem: 'Peak Traffic Scaling',
        solution: 'Auto-scaling groups with predictive scaling for seasonal demand'
      },
      {
        problem: 'Global Inventory Management',
        solution: 'Eventually consistent replication with compensation workflows'
      },
      {
        problem: 'Recommendation Latency',
        solution: 'Multi-tier caching with pre-computed recommendation sets'
      }
    ],
    metrics: {
      globalAvailability: '99.99%',
      searchLatency: '<100ms',
      checkoutTime: '<30 seconds',
      inventoryAccuracy: '99.5%',
      recommendationCTR: '35% improvement'
    }
  },
  {
    id: 'uber',
    name: 'Uber',
    logo: '🚗',
    industry: 'Transportation',
    scale: {
      users: '118M+',
      dataVolume: '100+ TB daily',
      requests: '15B+ per day'
    },
    architecture: {
      overview: 'Real-time location-based architecture with geospatial optimization. Event-driven system for trip matching and pricing.',
      storageStack: [
        {
          layer: 'Geospatial Data',
          technology: 'PostGIS + Redis Geospatial',
          purpose: 'Real-time location tracking and proximity matching'
        },
        {
          layer: 'Trip Data',
          technology: 'Amazon DynamoDB + MySQL',
          purpose: 'Trip history, payments, and driver information'
        },
        {
          layer: 'Analytics Platform',
          technology: 'Apache Hadoop + Presto',
          purpose: 'Demand forecasting and surge pricing algorithms'
        },
        {
          layer: 'Stream Processing',
          technology: 'Apache Kafka + Apache Storm',
          purpose: 'Real-time trip matching and ETA calculations'
        }
      ]
    },
    innovations: [
      {
        title: 'DISCO - Distributed Storage',
        description: 'Custom distributed storage system optimized for geospatial queries'
      },
      {
        title: 'Real-time Matching',
        description: 'Sub-second driver-rider matching using geohashing algorithms'
      },
      {
        title: 'Surge Pricing Engine',
        description: 'Dynamic pricing based on real-time supply-demand analytics'
      }
    ],
    challenges: [
      {
        problem: 'Real-time Location Processing',
        solution: 'Geospatial indexing with Redis and custom proximity algorithms'
      },
      {
        problem: 'Global Scaling',
        solution: 'City-specific data sharding with local processing centers'
      },
      {
        problem: 'Fraud Detection',
        solution: 'Real-time ML models analyzing trip patterns and anomalies'
      }
    ],
    metrics: {
      globalAvailability: '99.9%',
      matchingTime: '<3 seconds',
      etaAccuracy: '95%+',
      priceUpdateLatency: '<1 second',
      fraudDetectionRate: '99.7%'
    }
  },
  {
    id: 'airbnb',
    name: 'Airbnb',
    logo: '🏠',
    industry: 'Travel & Hospitality',
    scale: {
      users: '150M+',
      dataVolume: '50+ TB daily',
      requests: '5B+ per day'
    },
    architecture: {
      overview: 'Search-centric architecture with ML-driven ranking and pricing. Multi-region deployment with data locality optimization.',
      storageStack: [
        {
          layer: 'Listing Data',
          technology: 'Amazon RDS + Redis',
          purpose: 'Property listings with high-speed search indexing'
        },
        {
          layer: 'Search Engine',
          technology: 'Elasticsearch + Amazon S3',
          purpose: 'Faceted search with ML-powered ranking'
        },
        {
          layer: 'Analytics Warehouse',
          technology: 'Apache Airflow + Spark + S3',
          purpose: 'Pricing optimization and demand forecasting'
        },
        {
          layer: 'Image Storage',
          technology: 'Amazon S3 + CloudFront',
          purpose: 'Property photos with global CDN delivery'
        }
      ]
    },
    innovations: [
      {
        title: 'Dynamic Pricing Engine',
        description: 'ML-powered pricing recommendations using 100+ features'
      },
      {
        title: 'Search Relevance ML',
        description: 'Neural networks for search ranking with personalization'
      },
      {
        title: 'Trust & Safety ML',
        description: 'Real-time fraud detection and content moderation'
      }
    ],
    challenges: [
      {
        problem: 'Search Performance',
        solution: 'Elasticsearch with custom scoring algorithms and ML ranking'
      },
      {
        problem: 'Dynamic Pricing',
        solution: 'Real-time ML pipeline processing market data and demand signals'
      },
      {
        problem: 'Image Processing',
        solution: 'Automated image processing pipeline with quality detection'
      }
    ],
    metrics: {
      globalAvailability: '99.95%',
      searchLatency: '<200ms',
      pricingAccuracy: '85%+',
      imageLoadTime: '<2 seconds',
      mlModelAccuracy: '92%+'
    }
  }
];