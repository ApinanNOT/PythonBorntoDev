#โปรแกรมเปรียบเทียบตัวเลข

print("โปรแกรมเปรียบเทียบตัวเลข\n")
num1=int(input("Enter Num 1 : "))
num2=int(input("Enter Num 2 : "))

if num1<num2 :
    print(str(num1)+"\tน้อยกว่า\t"+str(num2))
elif num1>num2 :
    print(str(num1)+"\tมากกว่า\t"+str(num2))
elif num1==num2 :
    print(str(num1)+"\tเท่ากับ\t"+str(num2))
else : print("Eror")

print("\nจบโปรแกรมเปรียบเทียบตัวเลข")