import argparse

def ParseArg():
    DESCRIPTION = '''
        Vodka is a command line tool to create template for nlp/ml
        projects.
        To use vodka kindly type Vodka init.
    '''
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('init', nargs='+', help='bar help')
    args = parser.parse_args()
    return args