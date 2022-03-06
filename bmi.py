def check_bmi(bmi):
    if bmi < 18.5:
        return "under weight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "over weight"
    else:
        return "obese"


# main routine
get_bmi = float(input("enter bmi "))
print(f"with a bmi of {get_bmi} your status is {check_bmi(get_bmi)}")
5
