export const architecturePatterns = [
  {
    id: 'lambda-architecture',
    name: 'Lambda Architecture',
    description: 'Hybrid approach combining batch and real-time processing for comprehensive data analytics with fault tolerance through immutable data stores.',
    benefits: [
      'Handles both batch and real-time processing',
      'Fault-tolerant through immutable data storage',
      'Provides both accurate batch views and fast approximate results',
      'Scales to handle massive data volumes'
    ],
    useCases: [
      'Real-time fraud detection with historical analysis',
      'E-commerce recommendation engines',
      'Financial risk management systems',
      'IoT sensor data processing and alerting'
    ],
    layers: [
      {
        name: 'Data Ingestion',
        type: 'Streaming',
        description: 'High-throughput data collection from multiple sources',
        technologies: ['Apache Kafka', 'Amazon Kinesis', 'Google Pub/Sub']
      },
      {
        name: 'Batch Layer',
        type: 'Storage',
        description: 'Immutable, append-only storage for complete historical data',
        technologies: ['Amazon S3', 'HDFS', 'Google Cloud Storage']
      },
      {
        name: 'Speed Layer',
        type: 'Processing',
        description: 'Real-time processing for low-latency results',
        technologies: ['Apache Storm', 'Amazon Kinesis Analytics', 'Google Dataflow']
      },
      {
        name: 'Serving Layer',
        type: 'Query',
        description: 'Combines batch and real-time views for query serving',
        technologies: ['Apache Druid', 'Amazon Redshift', 'Google BigQuery']
      }
    ],
    faultTolerance: 'Immutable data storage ensures recoverability from any failures. Speed layer failures only affect real-time views, not historical accuracy.',
    scalingStrategy: 'Linear scaling in batch layer through distributed storage. Speed layer scales by adding more parallel processing units.'
  },
  {
    id: 'kappa-architecture',
    name: 'Kappa Architecture',
    description: 'Stream-first architecture that treats all data as streams, simplifying the data pipeline by eliminating the batch layer complexity.',
    benefits: [
      'Simplified architecture with single code path',
      'True real-time processing capabilities',
      'Easier to maintain and debug',
      'Lower operational overhead'
    ],
    useCases: [
      'Real-time personalization systems',
      'Live dashboard and monitoring',
      'Streaming ETL pipelines',
      'Event-driven microservices'
    ],
    layers: [
      {
        name: 'Stream Ingestion',
        type: 'Input',
        description: 'All data treated as continuous streams',
        technologies: ['Apache Kafka', 'Amazon Kinesis', 'Apache Pulsar']
      },
      {
        name: 'Stream Processing',
        type: 'Processing',
        description: 'Real-time transformation and analytics',
        technologies: ['Apache Flink', 'Kafka Streams', 'Azure Stream Analytics']
      },
      {
        name: 'Stream Storage',
        type: 'Storage',
        description: 'Durable stream storage with replay capabilities',
        technologies: ['Apache Kafka', 'Amazon Kinesis', 'Google Pub/Sub']
      },
      {
        name: 'Serving Views',
        type: 'Output',
        description: 'Materialized views updated in real-time',
        technologies: ['Apache Cassandra', 'Amazon DynamoDB', 'Redis']
      }
    ],
    faultTolerance: 'Stream replay capabilities allow reprocessing from any point in time. Stateful processing with checkpointing ensures exactly-once semantics.',
    scalingStrategy: 'Horizontal scaling through stream partitioning. Auto-scaling based on lag and throughput metrics.'
  },
  {
    id: 'data-lakehouse',
    name: 'Data Lakehouse',
    description: 'Modern architecture combining data lake flexibility with data warehouse performance, enabling both structured and unstructured analytics.',
    benefits: [
      'Unified platform for all data types',
      'ACID transactions on data lakes',
      'Schema evolution and versioning',
      'Direct ML training on raw data'
    ],
    useCases: [
      'Unified analytics platform',
      'ML feature engineering at scale',
      'Multi-format data integration',
      'Self-service analytics'
    ],
    layers: [
      {
        name: 'Storage Layer',
        type: 'Foundation',
        description: 'Object storage with ACID transaction support',
        technologies: ['Delta Lake', 'Apache Iceberg', 'Apache Hudi']
      },
      {
        name: 'Metadata Layer',
        type: 'Catalog',
        description: 'Unified catalog with schema management',
        technologies: ['AWS Glue Catalog', 'Apache Atlas', 'Unity Catalog']
      },
      {
        name: 'Compute Layer',
        type: 'Processing',
        description: 'Multiple engines for different workload patterns',
        technologies: ['Apache Spark', 'Presto', 'Apache Flink']
      },
      {
        name: 'Analytics Layer',
        type: 'Interface',
        description: 'SQL, Python, R interfaces for data access',
        technologies: ['Databricks', 'Snowflake', 'Amazon Athena']
      }
    ],
    faultTolerance: 'ACID transactions ensure data consistency. Time travel capabilities allow rollback to previous versions.',
    scalingStrategy: 'Elastic compute resources scale independently from storage. Auto-optimization of file layouts and statistics.'
  },
  {
    id: 'event-sourcing',
    name: 'Event Sourcing',
    description: 'Architecture pattern where all changes are stored as immutable events, providing complete audit trails and enabling event replay.',
    benefits: [
      'Complete audit trail of all changes',
      'Temporal queries and point-in-time recovery',
      'Enables complex event processing',
      'Natural fit for distributed systems'
    ],
    useCases: [
      'Financial transaction systems',
      'Supply chain tracking',
      'User behavior analytics',
      'Regulatory compliance systems'
    ],
    layers: [
      {
        name: 'Event Store',
        type: 'Storage',
        description: 'Immutable append-only event storage',
        technologies: ['EventStore', 'Amazon Kinesis', 'Apache Kafka']
      },
      {
        name: 'Event Processing',
        type: 'Processing',
        description: 'Event stream processing and aggregation',
        technologies: ['Apache Flink', 'Akka Streams', 'Azure Functions']
      },
      {
        name: 'Read Models',
        type: 'Views',
        description: 'Materialized views optimized for specific queries',
        technologies: ['Amazon DynamoDB', 'MongoDB', 'Elasticsearch']
      },
      {
        name: 'Event Bus',
        type: 'Communication',
        description: 'Decoupled communication between services',
        technologies: ['Amazon EventBridge', 'Google Pub/Sub', 'Apache Kafka']
      }
    ],
    faultTolerance: 'Immutable events provide natural disaster recovery. Event replay enables system reconstruction from any point.',
    scalingStrategy: 'Partition events by aggregate ID. Scale read models independently based on query patterns.'
  }
];