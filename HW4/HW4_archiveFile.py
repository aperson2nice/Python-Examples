#Sheila Robles
#Assignment 3 Problem 3
#Python Version 3.0.1

from __future__ import print_function #DELETE LATER
import argparse as arg
#import linecache as cache
import os
import zipfile

parser = arg.ArgumentParser(description='Zips files in a new zip or current zip folder')

parser.add_argument('ARCHIVEFILE', help='The name of the zip file')
parser.add_argument('-f', '--files', nargs="*", help='A list of files to put in the archive file')
parser.add_argument('-x', '--extract', type=bool, help='Extract the archive file')
parser.add_argument('-w', '--working-directory', help='Create a working directory in which everything will be saved to.')

# I need to check if ARCHIVEFILE is a zipfile, if not I have to give an error or make it a zip
arguments = parser.parse_args()
print(arguments) #DELETE LATER
filepath = arguments.ARCHIVEFILE
list_of_files = arguments.files
toextract = arguments.extract
working_dir = arguments.working_directory

#with zipfile.ZipFile('TESTING.zip', 'w') as new_zip:
#    new_zip.write('test1.txt')
message = ""

if os.path.exists(filepath):
    with zipfile.ZipFile(filepath, 'a') as new_zip:
        for f in list_of_files: #add files to working directory
            if not os.path.exists(f) and not os.path.exists(fpath+"\\"+f):
                message += "File1: " + f + " does not exist.\n"
            elif not os.path.exists(f) and os.path.exists(fpath+"\\"+f)
                message += "File3: a file " + f + " already exists"
            else:
                new_zip.write(file)
            
else:
    with zipfile.ZipFile(filepath, 'w') as new_zip:
        for f in list_of_files: #add files to working directory    
            if not os.path.exists(f):
                message += "File2: " + f + " does not exist.\n"
            else:
                    new_zip.write(f)

#print the information of the archive file use writing zipinfo instance on zipfile page
print("\n",message)
new_zip.printdir()

new_zip.close()

