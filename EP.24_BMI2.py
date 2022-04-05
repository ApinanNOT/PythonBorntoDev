print("โปรแกรมคำนวณค่าดัชนีมวลกาย BMI")
Weight=float(input("น้ำหนักของท่าน(กิโลกรัม) : "))
Heigh=float(input("ส่วนสูงของท่าน(เซนติเมตร) : "))
BMI=Weight/((Heigh/100)**2)
print("ค่าดัชนีมวลกายของท่าน : %.2f"%BMI)
if BMI<18.00 :
    print("ต่ำกว่าเกณฑ์")
elif BMI>=18.00 and BMI<=22.9:
    print("สมส่วน")
elif BMI>=23.00 and BMI<=24.9:
    print("น้ำหนักเกิน")
elif BMI>=25.00 and BMI<=29.9:
    print("โรคอ้วนระดับที่ 1")
elif BMI>=30:
    print("โรคอ้วนระดับอันตราย") #สามารถใช้ result แทน print ได้