from zipfile import *

# write zip file
# with ZipFile('pswd.zip') as my_zip:
#     with my_zip.open('duplicate-2.txt') as my_file:
#         for line in my_file:
#             print(line)

# extract all files from zip
with ZipFile('pswd.zip') as my_zip:
    my_zip.extractall()


# print('creating archive...')
# zip_f = zipfile.ZipFile('pswd.zip', 'w')
#
# zip_f.write('pswd.txt')
# zip_f.write('duplicate.txt')
# zip_f.write('duplicate-2.txt')

# read zip file
# zip_f.close()
# zip_f = zipfile.ZipFile('pswd.zip')
# print(zip_f.namelist())
# zip_f.printdir()

# print(zip_f.read('duplicate.txt'))
