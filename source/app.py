import os
import argparse

'''
Create app currently hardcoded folder structure will be taken from config in future.
'''
def create_app():
    # create folder
    os.mkdir('config')
    open('config/schema.yml', 'a').close()


    os.mkdir('notebook')
    open('notebook/paraphraser.ipynb', 'a').close()


    os.mkdir('paraphraser')
    # create folder in paraphraser
    os.mkdir('paraphraser/cloud_storage')
    open('paraphraser/cloud_storage/__init__.py', 'a').close()
    open('paraphraser/cloud_storage/s3_syncer.py', 'a').close()


    os.mkdir('paraphraser/components')
    open('paraphraser/components/__init__.py', 'a').close()
    open('paraphraser/components/data_ingestion.py', 'a').close()
    open('paraphraser/components/data_transformation.py', 'a').close()
    open('paraphraser/components/data_validation.py', 'a').close()
    open('paraphraser/components/model_evaluation.py', 'a').close()
    open('paraphraser/components/model_pusher.py', 'a').close()
    open('paraphraser/components/model_trainer.py', 'a').close()


    os.mkdir('paraphraser/configuration')
    open('paraphraser/configuration/__init__.py', 'a').close()
    open('paraphraser/configuration/mongo_db_connection.py', 'a').close()
    open('paraphraser/configuration/s3_operations.py', 'a').close()


    os.mkdir('paraphraser/constant')
    os.mkdir('paraphraser/constant/prediction_pipeline')
    open('paraphraser/constant/prediction_pipeline/__init__.py', 'a').close()
    os.mkdir('paraphraser/constant/training_pipeline')
    open('paraphraser/constant/training_pipeline/__init__.py', 'a').close()
    open('paraphraser/constant/__init__.py', 'a').close()
    open('paraphraser/constant/application.py', 'a').close()
    open('paraphraser/constant/database.py', 'a').close()
    open('paraphraser/constant/env.yaml', 'a').close()
    open('paraphraser/constant/env_variable.py', 'a').close()
    open('paraphraser/constant/s3_buckets.py', 'a').close()


    os.mkdir('paraphraser/data_access')
    open('paraphraser/data_access/__init__.py', 'a').close()
    open('paraphraser/data_access/paraphraser_data.py', 'a').close()


    os.mkdir('paraphraser/entity')
    open('paraphraser/entity/__init__.py', 'a').close()
    open('paraphraser/entity/artifact_entity.py', 'a').close()
    open('paraphraser/entity/config_entity.py', 'a').close()


    os.mkdir('paraphraser/exception')
    open('paraphraser/exception/__init__.py', 'a').close()

    os.mkdir('paraphraser/logger')
    open('paraphraser/logger/__init__.py', 'a').close()

    os.mkdir('paraphraser/models')
    os.mkdir('paraphraser/models/large_models')
    open('paraphraser/models/large_models/large.weights', 'a').close()
    os.mkdir('paraphraser/models/quant_models')
    os.mkdir('paraphraser/models/quant_models/fp16')
    open('paraphraser/models/quant_models/fp16/fp16.weights', 'a').close()
    os.mkdir('paraphraser/models/quant_models/fp32')
    open('paraphraser/models/quant_models/fp16/fp32.weights', 'a').close()
    os.mkdir('paraphraser/models/quant_models/fp64')
    open('paraphraser/models/quant_models/fp16/fp64.weights', 'a').close()
    os.mkdir('paraphraser/models/small_models')
    open('paraphraser/models/small_models/small.weights', 'a').close()

    os.mkdir('paraphraser/nlp')
    os.mkdir('paraphraser/nlp/estimator')
    open('paraphraser/nlp/estimator/__init__.py', 'a').close()
    open('paraphraser/nlp/estimator/paraphraser_estimator.py', 'a').close()

    os.mkdir('paraphraser/nlp/metric')
    open('paraphraser/nlp/metric/__init__.py', 'a').close()
    open('paraphraser/nlp/metric/paraphraser_metric.py', 'a').close()
    open('paraphraser/nlp/__init__.py', 'a').close()


    os.mkdir('paraphraser/pipeline')
    open('paraphraser/pipeline/__init__.py', 'a').close()
    open('paraphraser/pipeline/prediction_pipeline.py', 'a').close()
    open('paraphraser/pipeline/training_pipeline.py', 'a').close()


    os.mkdir('paraphraser/utils')
    open('paraphraser/utils/__init__.py', 'a').close()
    open('paraphraser/utils/demo.py', 'a').close()
    open('paraphraser/utils/main_utils.py', 'a').close()

    open('paraphraser/__init__.py', 'a').close()


    os.mkdir('templates')
    open('templates/request.html', 'a').close()
    open('templates/response.html', 'a').close()


    open('docker-compose.yml', 'a').close()
    open('Dockerfile', 'a').close()
    open('LICENSE', 'a').close()
    open('main.py', 'a').close()
    open('README.md', 'a').close()
    open('requirements.txt', 'a').close()
    open('setup.py', 'a').close()
    open('test.py', 'a').close()

    print("Project structure created successfully")

def main():
    # parse the command line arguments as per the argparse module
    DESCRIPTION = '''
        Vodka is a command line tool to create template for nlp/ml
        projects.
        To use vodka kindly type Vodka init.
    '''
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('init', nargs='+', help='bar help')
    args = parser.parse_args()
    if 'init' in args.init:
        create_app()

if __name__=='__main__':
    main()