# import yaml

# def LoadDefaultConfig(file = 'config.yaml'):
#     with open(file) as f:
#         return yaml.load(f , Loader=yaml.FullLoader)

LoadDefaultConfig = {
    'Folders': [
        {
            'Name': 'Vodka', 'Folders': [
                {
                    'Name': 'Config', 'Files': [
                        {
                            'Name': 'schema.yml'}
                    ]},
                {
                    'Name': 'notebook', 'Files': [
                        {
                            'Name': 'paraphraser.ipynb'}
                    ]},
                {
                    'Name': 'paraphraser', 'Folders': [
                        {
                            'Name': 'cloud_storage', 'Files': [
                                {
                                    'Name': '__init__.py'},
                                {
                                    'Name': 's3_syncer.py'},
                                {
                                    'Name': 'gcs_syncer.py'}
                            ]},
                        {
                            'Name': 'components', 'Files': [
                                {
                                    'Name': '__init__.py'},
                                {
                                    'Name': 'data_ingestion.py'},
                                {
                                    'Name': 'data_transformation.py'},
                                {
                                    'Name': 'data_validation.py'},
                                {
                                    'Name': 'model_evaluation.py'},
                                {
                                    'Name': 'model_pusher.py'},
                                {
                                    'Name': 'model_trainer.py'}
                            ]},
                        {
                            'Name': 'configuration', 'Files': [
                                {
                                    'Name': '__init__.py'},
                                {
                                    'Name': 'mongo_db_connection.py'},
                                {
                                    'Name': 's3_operations.py'}
                            ]},
                        {
                            'Name': 'constant', 'Folders': [
                                {
                                    'Name': 'prediction_pipeline', 'Files': [
                                        {
                                            'Name': '__init__.py'}
                                    ]},
                                {
                                    'Name': 'training_pipeline', 'Files': [
                                        {
                                            'Name': '__init__.py'}
                                    ]}
                            ], 'Files': [
                                {
                                    'Name': '__init__.py'},
                                {
                                    'Name': 'applications.py'},
                                {
                                    'Name': 'database.py'},
                                {
                                    'Name': 'env.yaml'},
                                {
                                    'Name': 'env_variable.py'},
                                {
                                    'Name': 's3_buckets.py'}
                            ]},
                        {
                            'Name': 'data_access', 'Files': [
                                {
                                    'Name': '__init__.py'},
                                {
                                    'Name': 'paraphraser_data.py'}
                            ]},
                        {
                            'Name': 'entity', 'Files': [
                                {
                                    'Name': '__init__.py'},
                                {
                                    'Name': 'artifact_entity.py'},
                                {
                                    'Name': 'config_entity.py'}
                            ]},
                        {
                            'Name': 'exception', 'Files': [
                                {
                                    'Name': '__init__.py'}
                            ]},
                        {
                            'Name': 'models', 'Folders': [
                                {
                                    'Name': 'large_models', 'Files': [
                                        {
                                            'Name': 'large.weights'}
                                    ]},
                                {
                                    'Name': 'quant_models', 'Folders': [
                                        {
                                            'Name': 'fp16', 'Files': [
                                                {
                                                    'Name': 'fp16.weights'}
                                            ]},
                                        {
                                            'Name': 'fp32', 'Files': [
                                                {
                                                    'Name': 'fp32.weights'}
                                            ]},
                                        {
                                            'Name': 'fp64', 'Files': [
                                                {
                                                    'Name': 'fp64.weights'}
                                            ]}
                                    ]},
                                {
                                    'Name': 'small_models', 'Files': [
                                        {
                                            'Name': 'small.weights'}
                                    ]}
                            ]},
                        {
                            'Name': 'nlp', 'Folders': [
                                {
                                    'Name': 'estimator', 'Files': [
                                        {
                                            'Name': '__init__.py'},
                                        {
                                            'Name': 'paraphraser_estimator.py'}
                                    ]},
                                {
                                    'Name': 'metric', 'Files': [
                                        {
                                            'Name': '__init__.py'},
                                        {
                                            'Name': 'paraphraser_metric.py'}
                                    ]}
                            ], 'Files': [
                                {
                                    'Name': '__init__.py'}
                            ]},
                        {
                            'Name': 'pipeline', 'Files': [
                                {
                                    'Name': '__init__.py'},
                                {
                                    'Name': 'prediction_pipeline.py'},
                                {
                                    'Name': 'training_pipeline.py'}
                            ]},
                        {
                            'Name': 'utils', 'Files': [
                                {
                                    'Name': '__init__.py'},
                                {
                                    'Name': 'demo.py'},
                                {
                                    'Name': 'main_utils.py'}
                            ]}
                    ], 'Files': [
                        {
                            'Name': '__init__.py'}
                    ]},
                {
                    'Name': 'templates', 'Files': [
                        {
                            'Name': 'request.html'},
                        {
                            'Name': 'response.html'}
                    ]}
            ], 'Files': [
                {
                    'Name': '.gitignore'},
                {
                    'Name': 'Dockerfile',
                    'Content': 'FROM python:3.7-slim-buster\nRUN apt update -y && apt install awscli -y\nCOPY . /paraphraser\nWORKDIR /paraphraser\nRUN pip install --upgrade pip\nRUN pip install -r requirements.txt\n\nCMD [ "python","main.py" ]\n'},
                {
                    'Name': 'LICENSE'},
                {
                    'Name': 'README.md'},
                {
                    'Name': 'docker-compose.yml'},
                {
                    'Name': 'main.py'},
                {
                    'Name': 'requirements.txt'},
                {
                    'Name': 'setup.py'},
                {
                    'Name': 'test.py'}
            ]}
    ]}
