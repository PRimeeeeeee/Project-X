from array import array


y = "-"*30

print(y.center(50,))
print("\033[0;31;43m","\033[0;31;43m Work 3".center(50,),end=' ')
print("\033[0m")
print(y.center(50,))
x = int(input('Input student ID='))
a = x // 10000
x -= a * 10000
b = x // 1000
x -= b * 1000
c = x // 100
x -= c * 100
d = x // 10
x -= d * 10
e = x // 1

print("\033[1;32;48m1st :","\033[1;31;48m",a)
print("\033[1;32;48m2nd :","\033[1;31;48m",b)
print("\033[1;32;48m3rd :","\033[1;31;48m",c)
print("\033[1;32;48m4th :","\033[1;31;48m",d)
print("\033[1;32;48m5th :","\033[1;31;48m",e)
print("\033[1:35;48m"+str(y))
q = int(input("\033[1;36;48mPrice = "))
w = int(input("Unit = "))
t = q * w
print("Total =","\033[1;31;48m",t)
print("\033[1;32;48m"+str(y))
p = float(input("\033[1;33;48mPay by cash = "))
ch = int(p) - t
print("\033[1;34;48m"+str(y))
print("\033[1;35;48mChange = ",float(ch))
m = ch // 500
ch -= m * 500
n = ch // 100
ch -= n * 100
o = ch // 50
ch -= o * 50
p = ch // 20
ch -= p * 20
r = ch // 10
ch -= r * 10
s = ch // 5
ch -= s * 5
t = ch // 2
ch -= t * 2
u = ch // 1
ch -= u * 1
v = ch // 0.5
ch -= v * 0.5
w = ch // 0.25
ch -= w * 0.25
print("\033[1;33;48m500 ="+"\033[1;34;48m",str(m)+"\t\t\033[1;33;48m10 =","\033[1;32;48m"+str(r) +"\t\t\033[1;33;48m0.5  =","\033[1;35;48m"+str(int(v)))
print("\033[1;33;48m100 ="+"\033[1;34;48m",str(n)+"\t\t\033[1;33;48m5  =","\033[1;32;48m"+str(s) +"\t\t\033[1;33;48m0.25 =","\033[1;35;48m"+str(int(w)))
print("\033[1;33;48m50  ="+"\033[1;34;48m",str(o)+"\t\t\033[1;33;48m2  =","\033[1;32;48m"+str(t))
print("\033[1;33;48m20  ="+"\033[1;34;48m",str(p)+"\t\t\033[1;33;48m1  =","\033[1;32;48m"+str(u))

ary = [1,2,3,4,5]
ans = "12345"

##for i in ary:
##   ans += str(ary[i])

print(ans)






















