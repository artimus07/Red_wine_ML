from src.Red_Wine import logger
from src.Red_Wine.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Red_Wine.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = 'Data Ingestion stage'
try:
    logger.info(f'>>>>>> stage{STAGE_NAME} started <<<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>> stage{STAGE_NAME} completed <<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e  


STAGE_NAME = 'Data Validation stage'
try:
    logger.info(f'>>>>>> stage{STAGE_NAME} started <<<<<<<<')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'>>>>>> stage{STAGE_NAME} completed <<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e