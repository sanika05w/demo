marks = int(input("enter your marks"))
if(marks>90 and marks<100):
    print("o")
elif(marks>80 and marks<100):
    print("A")
elif(marks>65 and marks<100):
    print("B")
elif(marks>35 and marks<100):
     print("c")    
else: 
    if(marks<35):
       print("fail")
    else:
        print("invalid number")   