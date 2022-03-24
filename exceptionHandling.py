try:
    age = 20
    if (age < 18):
        raise ValueError("not Eligible for vote")
    else:
        print("Eligible for vote.")
except ZeroDivisionError as e:
    print("Exception occured == "+str(e))
else:
    print("Program executed.")
finally:
    print(".......")