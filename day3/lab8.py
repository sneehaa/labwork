n=int(input("number:"))
result=0
for i in range (len(str(n))):
    digit=n%10
    result=result+digit
    n=n//10
    print(result)
