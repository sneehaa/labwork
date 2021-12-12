print("enter age")
age=int(input())
print("gender? (M or F)")
gender= input()
if (gender == "F" or gender == "f") and 20 <= age <= 60:
    print("Urban areas only")
elif(gender == "M" or gender == "m") and 20<= age <= 60: 
    print("you cab work anywhere")
elif(gender == "M" or gender == "m") and 40<= age <= 60:
    print("Urban area only")
else:
    print('ERROR')
