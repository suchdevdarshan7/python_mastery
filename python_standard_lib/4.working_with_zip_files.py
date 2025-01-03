from zipfile import ZipFile
from pathlib import Path


# zip = ZipFile('files.zip', 'w')

# for path in Path('shop').rgblob("*.*"):
#     zip.write(path)

# zip.close()

# with ZipFile('files.zip', 'w') as zip:
#     for path in Path('shop').rglob("*.*"):
#         zip.write(path)

with ZipFile('files.zip') as zip:
    print(zip.namelist())
    zip.extractall('extract')
