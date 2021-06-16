def findFiles(filenames):


    rootdir = 'Z:\data\ZnO\PL\Data'
    paths = []
    
    j = input('Enter year: ')

    if filenames == '':
        print('No input.')
        print()
        return

    if j == '':
        print('Searching all...')
    else:
        print('Searching ' + j + '...')

    found = False

    for subdir, dirs, files in os.walk(rootdir):
        if j in subdir:
            for file in files:
                if file in filenames:
                    paths.append(os.path.join(subdir,file))
                
    return paths
