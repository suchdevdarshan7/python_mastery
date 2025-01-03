user = {"name": "Somename", "email": "somemails@gmail.com"}


book = dict(x=1, y=2, z=3)

book['m'] = 100

print(user)
print(book)

for i in book:
    print(i, book[i])


for key, value in book.items():
    print(key, value)
