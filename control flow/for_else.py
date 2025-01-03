
successful = True

for number in range(1, 10):
    print("Attempt ", number)
    if successful:
        print('Successfully executed')
        break

else:
    print('Failed after attempting')
