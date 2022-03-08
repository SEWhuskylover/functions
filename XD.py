yesno = 2
total_adult = 0
total_child = 0
total_student = 0
total_gift = 0
profit = 0
while yesno == 2:
    ticket = input("what ticket do you want\n 1 for adult\n 2 for student\n 3 for child\n 4 for gift voucher: \n")
    if ticket == 1:
        print("sold")
        total_adult = total_adult + 1
        profit = profit + 12.5
    if ticket == 2:
        print("sold")
        total_student = total_student + 1
        profit = profit + 9
    if ticket == 3:
        print("sold")
        total_child = total_child + 1
        profit = profit + 7
    if ticket == 4:
        print("thankyou")
        total_gift = total_gift + 1
    yesno = input("do you want to sell another 2 for yes 1 for no:\n")
print("summary for today")
print(f"total adult tickets sold \n = {total_adult}")
print(f"total student tickets sold \n = {total_student}")
print(f"total child tickets sold \n = {total_child}")
print(f"total gift cards \n {total_gift}")
print(f"total profit \n {profit}")

