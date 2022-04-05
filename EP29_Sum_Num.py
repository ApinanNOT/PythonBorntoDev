#โปรแกรมผลรวมของตัวเลข

i=1
sum=0
avg=0

while i<=10:
    sum+=i
    i+=1
avg=sum/i
print("ผลรวม :",sum)
print("ค่าเฉลี่ย :%.2f"%avg)