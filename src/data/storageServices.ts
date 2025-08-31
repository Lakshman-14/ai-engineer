export const storageServices = [
  {
    id: 'aws-s3',
    name: 'Amazon S3',
    provider: 'aws',
    category: 'object-storage',
    description: 'Industry-leading object storage with 99.999999999% (11 9s) durability',
    useCase: 'Data lakes, backup/archival, content distribution, big data analytics',
    scalability: 'Virtually unlimited storage capacity, automatic scaling across multiple AZs',
    durability: '99.999999999% (11 9s) with cross-region replication',
    throughput: '3,500 PUT/COPY/POST/DELETE + 5,500 GET/HEAD per second per prefix',
    costModel: 'Pay-as-you-go: $0.023/GB/month (Standard), $0.0125/GB/month (IA)',
    aiMlIntegration: 'Native integration with SageMaker, EMR, Athena for ML pipelines',
    realWorldExample: 'Netflix stores 1+ PB of content, serving 200M+ users globally with 99.99% availability'
  },
  {
    id: 'aws-redshift',
    name: 'Amazon Redshift',
    provider: 'aws',
    category: 'data-warehouse',
    description: 'Petabyte-scale data warehouse with columnar storage and MPP architecture',
    useCase: 'Business intelligence, complex analytics, historical data analysis',
    scalability: 'Up to 128 nodes, 8PB compressed storage, linear performance scaling',
    durability: '99.9% availability with automated backups and snapshots',
    throughput: '500,000+ queries per hour, sub-second response for most queries',
    costModel: '$0.25/hour per node (dc2.large), reserved instances up to 75% savings',
    aiMlIntegration: 'Redshift ML for in-database ML, integration with SageMaker',
    realWorldExample: 'Lyft processes 100TB+ of ride data daily for real-time pricing and demand forecasting'
  },
  {
    id: 'gcp-bigquery',
    name: 'Google BigQuery',
    provider: 'gcp',
    category: 'data-warehouse',
    description: 'Serverless, highly scalable enterprise data warehouse with built-in ML',
    useCase: 'Ad-hoc analytics, real-time insights, ML model training on large datasets',
    scalability: 'Auto-scaling, processes petabytes in minutes, 2000+ concurrent queries',
    durability: '99.95% SLA with automatic replication across regions',
    throughput: 'Up to 100,000 rows/second streaming inserts, 1TB/second query processing',
    costModel: '$5/TB queried (on-demand), $20/TB/month (flat-rate), $0.20/GB streamed',
    aiMlIntegration: 'BigQuery ML for SQL-based ML, Vertex AI integration, AutoML',
    realWorldExample: 'Spotify analyzes 8 billion hours of music streaming data for personalized recommendations'
  },
  {
    id: 'aws-dynamodb',
    name: 'Amazon DynamoDB',
    provider: 'aws',
    category: 'nosql',
    description: 'Single-digit millisecond latency NoSQL database with automatic scaling',
    useCase: 'Real-time applications, gaming leaderboards, IoT data, user profiles',
    scalability: 'Unlimited storage, automatic partitioning, on-demand/provisioned capacity',
    durability: '99.999% availability across multiple AZs with Global Tables',
    throughput: 'Millions of requests/second, single-digit millisecond latency',
    costModel: '$0.25/WCU/month, $0.25/RCU/month, $0.25/GB/month storage',
    aiMlIntegration: 'DynamoDB Streams for real-time ML feature stores, Kinesis integration',
    realWorldExample: 'Uber stores 100+ billion location updates daily for real-time driver matching'
  },
  {
    id: 'gcp-bigtable',
    name: 'Google Cloud Bigtable',
    provider: 'gcp',
    category: 'nosql',
    description: 'High-performance NoSQL database service for large analytical workloads',
    useCase: 'Time-series data, IoT analytics, financial trading data, ad tech',
    scalability: 'Petabyte-scale, linear scaling up to hundreds of nodes',
    durability: '99.5% availability SLA with multi-region replication',
    throughput: '10,000+ QPS per node, sub-10ms latency at 95th percentile',
    costModel: '$0.65/hour per node + $0.17/GB/month storage',
    aiMlIntegration: 'Direct integration with Dataflow, AI Platform for ML pipelines',
    realWorldExample: 'Snapchat stores 4+ billion snaps daily using Bigtable for real-time analytics'
  },
  {
    id: 'aws-kinesis',
    name: 'Amazon Kinesis',
    provider: 'aws',
    category: 'streaming',
    description: 'Real-time streaming data platform for continuous data ingestion',
    useCase: 'Real-time analytics, log processing, IoT data streams, fraud detection',
    scalability: 'Unlimited shards, automatic scaling based on throughput',
    durability: '99.9% availability with automatic replication across AZs',
    throughput: '1,000 records/second per shard, 1MB/second data ingestion per shard',
    costModel: '$0.015/shard/hour + $0.014/million records PUT',
    aiMlIntegration: 'Kinesis Analytics for real-time ML, integration with SageMaker',
    realWorldExample: 'Pinterest processes 20+ billion events daily for real-time recommendation updates'
  },
  {
    id: 'azure-cosmos',
    name: 'Azure Cosmos DB',
    provider: 'azure',
    category: 'nosql',
    description: 'Globally distributed, multi-model database with guaranteed SLAs',
    useCase: 'Global applications, multi-region consistency, graph analytics',
    scalability: 'Unlimited storage and throughput, automatic global distribution',
    durability: '99.999% availability with 5 consistency levels',
    throughput: 'Millions of operations/second with single-digit millisecond latency',
    costModel: '$0.008/100 RU/hour + $0.25/GB/month, serverless billing available',
    aiMlIntegration: 'Azure Machine Learning integration, Cognitive Services APIs',
    realWorldExample: 'H&M uses Cosmos DB globally for inventory management across 5,000+ stores'
  },
  {
    id: 'aws-glacier',
    name: 'Amazon S3 Glacier',
    provider: 'aws',
    category: 'archival',
    description: 'Ultra-low-cost archival storage for long-term data retention',
    useCase: 'Compliance archiving, backup retention, disaster recovery',
    scalability: 'Unlimited storage capacity with automatic lifecycle management',
    durability: '99.999999999% (11 9s) with cross-region replication',
    throughput: 'Bulk retrieval: 5-12 hours, Expedited: 1-5 minutes',
    costModel: '$0.004/GB/month (Deep Archive), $0.0036/GB/month (Glacier Instant)',
    aiMlIntegration: 'S3 Select for querying archived data, Athena for analytics',
    realWorldExample: 'NASA stores 247+ PB of Earth science data in Glacier for climate research'
  },
  {
    id: 'gcp-cloud-storage',
    name: 'Google Cloud Storage',
    provider: 'gcp',
    category: 'object-storage',
    description: 'Unified object storage with global edge caching and CDN integration',
    useCase: 'Content delivery, data lakes, backup/DR, ML training datasets',
    scalability: 'Exabyte-scale storage with automatic multi-region replication',
    durability: '99.999999999% (11 9s) with dual-region storage',
    throughput: '1000+ requests/second with global load balancing',
    costModel: '$0.020/GB/month (Standard), $0.010/GB/month (Nearline)',
    aiMlIntegration: 'Vertex AI integration, AutoML datasets, BigQuery external tables',
    realWorldExample: 'Discord stores 10+ PB of media files with global CDN for 150M+ users'
  }
];

export interface Service {
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