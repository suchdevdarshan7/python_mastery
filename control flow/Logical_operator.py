HighIncome = True
GoodCredit = True
Student = True


if (HighIncome or GoodCredit) and not Student:
    print("Eligble")
else:
    print("Not Eligble")
