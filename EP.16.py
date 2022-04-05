age=int(input("ป้อนอายุของคุณ : "))

'''
if age>=15 :
    print("คุณสามารถใช้ นาย ได้")
else : 
    print("คุณไม่สามารถใช้ นาย ได้")

print("จบโปรแกรม")
'''
'''
if จริง :
    ทำอะไร
else :
    ทำอะไร
'''
'''
if age>=30:
    print("วัยทำงาน")
elif age>=20:
    print("วัยผู้ใหญ่")
elif age>=15:
    print("วัยรุ่น")
else:
    print("วัยเด็ก")

print("จบการทำงาน")
'''

# 15-20 วัยรุ่น
# 21-29 วัยผู้ใหญ่
# 30-39 วัยทำงาน
#and or not

if age>=15 and age<=20:
    print("วัยรุ่น")
elif age>=21 and age<=29:
    print("วัยผู้ใหญ่")
elif age>=30 and age<=39:
    print("วัยทำงาน")
else:
    print("วัยเด็ก")

print("จบการทำงาน")