
from vodka.src.creator import create
from vodka.src.config import configLoader
from vodka.src.parsearg import argparse

'''
Create app currently hardcoded folder structure will be taken from config in future.
'''
def create_app():
    config = configLoader.LoadDefaultConfig
    # print(config)
    create.createFolderStructure(config['Folders'], '')
    print('App created')

def main():
    # parse the command line arguments as per the argparse module
    args = argparse.ParseArg()
    if 'init' in args.init:
        # print('Creating app')
        create_app()

if __name__=='__main__':
    main()