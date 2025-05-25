from claim.entity.data_ingestion_config import DataIngestionConfig

from claim.components.data_ingestion import DataIngestion

from claim.entity.training_config import TrainingPipelineConfig
import sys


training_config = TrainingPipelineConfig()
data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_config)
data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
print(data_ingestion_artifact)
print("-===========================")