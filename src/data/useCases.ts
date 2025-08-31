export const useCases = [
  {
    id: 'transactional',
    title: 'Transactional Workloads',
    icon: '⚡',
    pattern: 'High-frequency reads/writes, ACID compliance, low latency',
    dataCharacteristics: 'Small to medium record sizes (KB-MB), structured data, frequent updates',
    performance: 'Sub-millisecond latency, 100K+ TPS, strong consistency',
    recommendedServices: [
      {
        layer: 'Primary Database',
        service: 'Amazon DynamoDB / Azure Cosmos DB',
        provider: 'AWS/Azure',
        reason: 'Single-digit millisecond latency with automatic scaling'
      },
      {
        layer: 'Caching Layer',
        service: 'Amazon ElastiCache / Redis Enterprise',
        provider: 'AWS/Multi',
        reason: 'Sub-millisecond access for frequently accessed data'
      },
      {
        layer: 'Change Data Capture',
        service: 'DynamoDB Streams / Cosmos DB Change Feed',
        provider: 'AWS/Azure',
        reason: 'Real-time data propagation for downstream systems'
      }
    ],
    costOptimization: 'Use on-demand billing for unpredictable workloads, reserved capacity for steady-state traffic, implement data tiering for older records'
  },
  {
    id: 'analytical',
    title: 'Analytical Workloads',
    icon: '📈',
    pattern: 'Complex queries, batch processing, historical analysis',
    dataCharacteristics: 'Large datasets (TB-PB), denormalized schemas, append-mostly patterns',
    performance: 'High throughput over latency, parallel processing, compression efficiency',
    recommendedServices: [
      {
        layer: 'Data Warehouse',
        service: 'Google BigQuery / Amazon Redshift',
        provider: 'GCP/AWS',
        reason: 'Columnar storage optimized for analytical queries'
      },
      {
        layer: 'Data Lake',
        service: 'Amazon S3 / Google Cloud Storage',
        provider: 'AWS/GCP',
        reason: 'Cost-effective storage for raw data in multiple formats'
      },
      {
        layer: 'Processing Engine',
        service: 'Apache Spark on Databricks / EMR',
        provider: 'Multi',
        reason: 'Distributed processing for large-scale transformations'
      }
    ],
    costOptimization: 'Use columnar formats (Parquet), implement data partitioning, leverage spot instances for processing, automated data lifecycle policies'
  },
  {
    id: 'archival',
    title: 'Archival & Compliance',
    icon: '🗃️',
    pattern: 'Write-once-read-rarely, long-term retention, compliance requirements',
    dataCharacteristics: 'Immutable data, large file sizes, infrequent access patterns',
    performance: 'Storage cost over access speed, high durability, retrieval SLAs',
    recommendedServices: [
      {
        layer: 'Deep Archive',
        service: 'Amazon S3 Glacier Deep Archive',
        provider: 'AWS',
        reason: 'Lowest cost storage for long-term retention'
      },
      {
        layer: 'Lifecycle Management',
        service: 'S3 Intelligent Tiering / GCS Autoclass',
        provider: 'AWS/GCP',
        reason: 'Automatic cost optimization based on access patterns'
      },
      {
        layer: 'Compliance & Governance',
        service: 'AWS Macie / Azure Purview',
        provider: 'AWS/Azure',
        reason: 'Data discovery, classification, and compliance monitoring'
      }
    ],
    costOptimization: 'Implement aggressive lifecycle policies, use deep archive for compliance data, compress before archiving, batch retrieval requests'
  },
  {
    id: 'ml-ai',
    title: 'AI/ML Workloads',
    icon: '🤖',
    pattern: 'Large dataset training, feature stores, model serving',
    dataCharacteristics: 'Massive training datasets (PB scale), feature engineering pipelines, model artifacts',
    performance: 'High bandwidth for training, low latency for inference, versioning support',
    recommendedServices: [
      {
        layer: 'Training Data',
        service: 'Amazon S3 / Google Cloud Storage',
        provider: 'AWS/GCP',
        reason: 'High-throughput access for distributed training workloads'
      },
      {
        layer: 'Feature Store',
        service: 'Amazon SageMaker Feature Store / Vertex AI',
        provider: 'AWS/GCP',
        reason: 'Managed feature engineering and serving pipeline'
      },
      {
        layer: 'Model Registry',
        service: 'MLflow on S3 / Vertex AI Model Registry',
        provider: 'Multi/GCP',
        reason: 'Version control and lineage tracking for ML models'
      }
    ],
    costOptimization: 'Use spot instances for training, implement model compression, leverage transfer learning, optimize data formats for ML frameworks'
  },
  {
    id: 'streaming',
    title: 'Real-time Streaming',
    icon: '🌊',
    pattern: 'Continuous data ingestion, real-time processing, low-latency analytics',
    dataCharacteristics: 'High-velocity data streams, time-series patterns, event-driven architecture',
    performance: 'Microsecond latency, millions of events/second, exactly-once processing',
    recommendedServices: [
      {
        layer: 'Stream Ingestion',
        service: 'Amazon Kinesis / Apache Kafka',
        provider: 'AWS/Multi',
        reason: 'High-throughput data ingestion with ordering guarantees'
      },
      {
        layer: 'Stream Processing',
        service: 'Amazon Kinesis Analytics / Dataflow',
        provider: 'AWS/GCP',
        reason: 'Real-time stream processing with SQL and complex event processing'
      },
      {
        layer: 'Time-series Storage',
        service: 'Amazon Timestream / InfluxDB Cloud',
        provider: 'AWS/Multi',
        reason: 'Optimized storage and querying for time-series data'
      }
    ],
    costOptimization: 'Right-size shard count, use compression for historical data, implement data retention policies, optimize consumer lag'
  },
  {
    id: 'hybrid-multi',
    title: 'Hybrid/Multi-Cloud',
    icon: '🌐',
    pattern: 'Data sovereignty, vendor independence, disaster recovery across clouds',
    dataCharacteristics: 'Distributed across multiple regions/providers, synchronized replicas',
    performance: 'Global consistency, cross-cloud networking, unified management',
    recommendedServices: [
      {
        layer: 'Multi-Cloud Orchestration',
        service: 'HashiCorp Terraform / Pulumi',
        provider: 'Multi',
        reason: 'Infrastructure as code across multiple cloud providers'
      },
      {
        layer: 'Data Synchronization',
        service: 'MongoDB Atlas / CockroachDB Cloud',
        provider: 'Multi',
        reason: 'Global distribution with automatic conflict resolution'
      },
      {
        layer: 'Unified Analytics',
        service: 'Databricks Lakehouse / Snowflake',
        provider: 'Multi',
        reason: 'Single analytics platform across multiple cloud environments'
      }
    ],
    costOptimization: 'Leverage cloud arbitrage, use spot markets across providers, implement intelligent data placement based on access patterns'
  }
];