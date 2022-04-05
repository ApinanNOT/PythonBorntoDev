#break and continue

"""
i=1
while i<=10:
    print("รอบที่ :",i)
    if(i==5): #ถ้า i=5 ให้หยุดการทำงาน
        break
    i+=1
    
print("จบโปรแกรม")
"""
i=0
while i<=10:
    i+=1
    if(i==5):
        continue #กระโดดข้าม 5 ไป
    print("รอบที่ :",i)
        
    
print("จบโปรแกรม")