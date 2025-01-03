from pathlib import Path


path = Path('python_standard_lib/shop')
# print(path.absolute())

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("eccomerce2")


# return a generator
for p in path.iterdir():
    print(f"{p} \n")
