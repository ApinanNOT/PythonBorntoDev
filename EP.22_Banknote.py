#แลกเงินและหาจำนวนแบงค์
#2000 => 1000 2 ใบ
#1500 => 1000 1 ใบ , 500 1 ใบ

money=float(input("ป้อนจำนวนเงิน : "))

if money>=1000 :
    print("1000 บาท : ",money//1000,"ใบ")
    money=money%1000

if money>=500 :
    print("500 : ",money//500,"ใบ")
    money=money%500

if money>=100 :
    print("100 : ",money//100,"ใบ")
    money=money%100

if money>=50 :
    print("50 : ",money//50,"ใบ")
    money=money%50

if money>=20 :
    print("20 : ",money//20,"ใบ")
    money=money%20

if money>=10 :
    print("10 : ",money//10,"เหรียญ")
    money=money%10

if money>=5 :
    print("5 : ",money//5,"เหรียญ")
    money=money%5

if money>=2 :
    print("2 : ",money//2,"เหรียญ")
    money=money%2

if money>=1 :
    print("1 : ",money//1,"เหรียญ")
    money=money%1

if money>=0.50 :
    print("0.50 : ",money//0.50,"เหรียญ")
    money=money%0.50

if money>=0.25 :
    print("0.25 : ",money//0.25,"เหรียญ")
    money=money%0.25


