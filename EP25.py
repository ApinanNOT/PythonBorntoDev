name="Apinan studio : 21"

print(name[0:3]) #index เริ่มตั้งแต่ 0 ช่องว่างก็นับเป็น index
print("อายุเท่าไหร่ = ",name[-2:]) #นับ index เริ่มจากข้างหลัง
print("จำนวนตัวอักษร = ",len(name)) #len คือคำสั่งนับจำนวนตัวอักษร
name1=" Apinan "
name1=name1.strip() #ลบช่องว่างซ้ายขวา
name1=name1.lstrip() #ลบช่องว่างซ้าย
name1=name1.rstrip() #ลบช่องว่างขวา
print(name1.upper()) #แปลงเป็นตัวพิมพ์ใหญ่ทั้งหมด
print(name1.lower()) #แปลงเป็นตัวพิมพ์เล็กทั้งหมด
print(name1.capitalize()) #ตัวแรกเป็นตัวพิมพ์ใหญ่
print(name1.replace("Api","OOH")) #แทนที่ Api เป็น OOH
name2="Apinan เกรด 3 ปี 3"
print(name2.replace("3","4",1)) #แทนที่เกรด 3 เป็น 4 ในเลข่ 3 ตัวแรก
name3="ไปซื้อข้าวและอาหาร"
x = "ข้าว" in name3 #เช็คว่า ข้าว อยู่ใน name3 มั๊ยเก็บค่าไว้ใน x
print(x)
if x:
    name3=name3.replace("ข้าว","ข้าวสุก")
    print(name3)