#if ซ้อน if
age=int(input("ป้อนอายุของคุณ : "))

if age<=15:
    print("มัธยมต้น")
    if age==15:
        print("ม.3")
    elif age==14:
        print("ม.2")
    elif age==13:
        print("ม.1")
    elif age==12:
        print("ม.1")
    elif age<=11:
        print("ประถมศึกษา")
else:
    print("มัธยมปลาย")