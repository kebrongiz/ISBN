def isbn():
    isbn = input("Enter the 9 digit number:")

    while len(isbn) != 9:
        print("please Enter 9 digit number")
        isbn = input("Enter the 9 digit number:")


    sum = 0
    for ldx, value in enumerate(list(isbn)):
        sum += int(value) * (ldx + 1)
    check_sum = sum % 11
    if check_sum == 10:
        isbn += 'x'


    else:
        isbn += str(check_sum)

    print("The 10-digit ISBN is: {}".format(isbn))


isbn()





















