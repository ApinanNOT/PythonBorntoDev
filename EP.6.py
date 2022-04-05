#Type Coversion
x = 10
y = 3.14
z = "20"

print(type(x))
print(type(y))
print(type(z))

#บวกเลข
Answer=x+y #เอาค่า 10+3.14 และเก็บค่าไว้ใน Answer
print(Answer)

#แปลง String เป็น int
int(z) #วิธีแปลง z จาก String เป็น int
Result=x+int(z)
print(Result)

#แปลง int เป็น String
str(x) #วิธีแปลง x จาก int เป็น String
Word=str(x)+z
print(Word)

#แปลง String เป็น float
float(z)
OP=float(z)+y
print(OP)

#สรุปอยากเปลี่ยนตัวแปลไหนให้นำคำสั่งที่ต้องการแปลงไปไว้ข้างหน้าตัวที่ต้องการจะแปลง