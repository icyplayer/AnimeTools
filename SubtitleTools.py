""" 
For subtitle zip file unzip and rename to fit video file name, 
so as to auto-adde by video player while video file opened.
Works under Python 2.7.10 
"""

import os
import sys
import zipfile


#unzip
def unzip(fileName):
    zfile = zipfile.ZipFile(fileName,'r')
    for filename in zfile.namelist():
        data = zfile.read(filename)
        with open(filename, 'w+b') as file:
            file.write(data)
    print('%s unzipped' % fileName)


#unzip files under path, ~/ as default
def unzipFilePath(dir = os.getcwd()):    
    list = os.listdir(dir)
    for fileName in list:
        if fileName.split('.uni_sub.')[-1] == 'zip':
            unzip(fileName)


def renameFileUnderPath(dir = os.getcwd()):
    list = os.listdir(dir)
    for fileName in list:
        nameList = fileName.split('.')
        if nameList[-1] == 'ass':
            if nameList[1] == 'uni_gb': 
                newName = nameList[0] + '.' + nameList[-1]
                os.renames(fileName, nameList[0]+'.'+'ass')
                print('renamed: %s => %s' % (fileName, newName))


if __name__ == '__main__':
    # print('Start unzipping...')
    # unzipFilePath()
    print('Start renaming...')
    renameFileUnderPath()
    print('Finished!')

    
# # ref: http://www.sharejs.com/codes/python/210
# #zip all files under folder
# f = zipfile.ZipFile('archive.zip','w',zipfile.ZIP_DEFLATED)
# startdir = "c:\\mydirectory"
# for dirpath, dirnames, filenames in os.walk(startdir):
#     for filename in filenames:
#         f.write(os.path.join(dirpath,filename))
# f.close()
 
#zip
# import zipfile
# f = zipfile.ZipFile('archive.zip','w',zipfile.ZIP_DEFLATED)
# f.write('file_to_add.py')
# f.close()
