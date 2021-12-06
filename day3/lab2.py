a = int(input("subject 1 makrs: "))
b=  int(input("subject 2 marks: "))
c = int(input("subject 3 marks: "))
d = int(input("subject 4 marks: "))
total = (a+b+c+d)
print(f"total: {total}")
avg = (a+b+c+d)/5
print(f"poercentage: {avg}%")

if(avg>90):
    print("Congratulations! Your Grade is A")
elif(avg>=80 and avg<90):
    print("Congratulations! Your Grade is B")
elif(avg>=70 and avg<80):
    print("Congratulations! Your Grade is C")
elif(avg>60 and avg<70):
    print("Congratulations! Your Grade is D")
else:
    print("Sorry you have failed!")