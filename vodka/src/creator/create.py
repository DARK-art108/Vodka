import os

def createFolderStructure(config, path):
    if config is None or config == []:
        return
    # if path is not '':
    #     path += '/'
    try:
        # print('Creating folder structure')
        for f in config if type(config) is list else []:
            os.mkdir(path+f['Name'])
            # print('Created folder: '+path+f['Name'])
            npath = path+f['Name']+ '/'
            if f is not None:
                for file in f['Files'] if 'Files' in f else []:
                    with open(npath+file['Name'], 'a') as curFile:
                        # print('Creating file: '+npath+file['Name'])
                        if 'Content' in file:
                            curFile.write(file['Content'])
                    # print(file['Content'])
                createFolderStructure(f['Folders'], npath) if 'Folders' in f else []
    except FileExistsError:
        print('Directory already exists')
    except Exception as e:
        print(f"error {e} occured")