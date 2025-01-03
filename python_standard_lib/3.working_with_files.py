from pathlib import Path
import sys
import shutil

current_path = Path.cwd()
source = Path(f'{current_path}/shop/__init__.py')
target = Path(f"{current_path}/shop/ans.py")

shutil.copy(source, target)
print('Copied successfully ')


# print(f'The path is {path}')
# print(f"Current path is {current_path}")


# data = source.read_text()
# print(data)

# target.write_text(data)

# print(path.exists())


# if path.exists():
#     print("File exists")
#     path.unlink()  # Delete the file
#     print("File deleted")
# else:
#     print("File does not exist")
