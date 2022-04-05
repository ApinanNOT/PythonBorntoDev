fname="Apinan"
lname="Prakaekan"
age="21"
salary=18000.9999

fullname=fname+lname+age #ต่อ String
print(fullname+"555")

print("ชื่อต้น : "+fname+"\nนามสกุล : "+lname+"\nอายุ : "+age)

text="ชื่อต้น : {}\tนามสกุล : {}\tอายุ : {}"
print(text.format(fname,lname,age))

text="ชื่อต้น : {1}\tนามสกุล : {1}\tอายุ : {1}\tอาชีพ : {3}"
print(text.format(fname,lname,age,"โปรแกรมเมอร์")) #ตำแหน่งเริ่มตั้งแต่ 0

text="ชื่อต้น : {1}\tนามสกุล : {1}\tอายุ : {1}\tอาชีพ : {3}\tเงินเดือน : {4:.2f}" #:2f ทศนิยม 2 ตำแหน่ง
print(text.format(fname,lname,age,"โปรแกรมเมอร์",salary))

#นับจำนวนคำในประโยค
fruit="ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด"
print(fruit.count("ทุเรียน")) #เจอคำว่าทุเรียนในประโยคกี่คำ

#เช็คคำขึ้นต้น
name="นายกอไก่ ใจดี"
print(name.startswith("นาย")) #ตรวจสอบว่าประโยคขึ้นต้นด้วย นาย หรือเปล่า
if name.startswith("นาย"):
    print("เป็นเพศชาย")
else :
    print("เป็นเพศอื่นๆ")

#เช็คคำลงท้าย
lottery="199898"
if lottery.endswith("898"):
    print("ถูกเลขท้าย 3 ตัว")
else :
    print("เสียใจด้วยไม่ถูกเลขท้าย 3 ตัว")