def summ(sonlar: list) -> int:
    total = 0
    for i in sonlar:
        total += i
    return total
print(summ([2,8,8,4,65,7]))


def num(k: list) -> int:
    kopaytma = 1
    for son in k:
        kopaytma *= son
    return kopaytma
print(num([5,5,4,5,5,5]))




def kvadrat (son):
    return son ** 2

a = kvadrat(9)
print(a)


def yigindi (a,b):
    return a+b
b = yigindi(7,8)
print(b)

def list (sonlar=[]):
    return max(sonlar)
g = list(sonlar=[65,76,23,2,34,5,6,78,90])
print(g)


def string (matn):
    soni = 0
    for i in matn:
     soni += 1
    return soni
print(string(matn= "yaxshimisz sizning kontrakt tolovingiz"))

def num (a):
    if  a %2 == 0:
     return f"{a} soni juft"
    else:
     return f"{a} soni toq"
son2 = num(7)
print(son2)


def fact (r):
    import math
    return math.factorial(r)
www = fact(9)
print(www)


def roy (list=[]):
    return sum(list)
yigindi = roy([5,6,77,66,55,44])
print(yigindi)


def string1 (matn1):
    return matn1[::-1]
asar = string1("nma gapla tincmi uydegila yaxshimi ")
print(asar)


def kkk (a, b):
 sonlar = []
 for i in range(a, b +1):
    sonlar.append(i)
 return sonlar
s = kkk(3,12)
print(s)


def tub (a):
    if a%a==0 and a%1==0:
        return f"{a} soni tub"
    else:
        return f"{a} soni tub emas"
fff = tub(7)
print(fff)

def kub (a):
    return a**3
son3 = kub(6)
print(son3)

def juft (royxat = []):
    Juft = []
    for i in royxat:
     if i%2 == 0:
         Juft.append(i)
    return Juft
y = juft([3,5,4,7,8,6,10,120])
print(y)



def kub(a):
    return a ** 3
A = kub(2)

def kvadrat(a):
    return  a ** 2
B = kvadrat(2)


print(kvadrat(kub(2)))



def salom(ism):
    print(f"salom {ism}")

salom("Ibrohim ")
salom("EMil")
salom("saman")

def kvadrat(son):
    return  son ** 2
tt = kvadrat(2)

def kub(a):
    return a ** 3
D = kub(2)
print(kvadrat(kub(2)))

def katta_son(number1,number2):
    if number1 > number2:
        print(f"{number1} soni katta ")
    else:
        print(f"{number2} soni kattaroq ")
katta_son(45,84)


def celsius_to_fahr(temp):
    return temp * 9/5 + 32

def fahr_to_celsius(temp):
    return (temp - 32) * 5/9

celsius = 25

fahrenheit = celsius_to_fahr(celsius)
print(f"{celsius}°C → {fahrenheit}°F")

yana_celsius = fahr_to_celsius(fahrenheit)
print(f"{fahrenheit}°F → {yana_celsius}°C")


def juft(son):
    return son % 2 == 0

for i in range(1,11):
    print(i, juft(i))

def chegirma(narx, foiz=10):
    return narx - (narx*foiz/100)

print(int(chegirma(400000,0)))
print(int(chegirma(400000,25)))



def ortacha(*args):
    total_score = 0
    for i in args:
        total_score += i
    return total_score / len(args)
print(ortacha(4,5,6,7,8,9))
print(ortacha(7,8,7,5,4,6,9,4,8,7,2,3,5,4,77))



def anketa(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} <!!!> {value}")

anketa(ism="Ali", sinf=9,shahar="Toshkent")


def baxo(**kwargs):
    for  k,v in kwargs.items():
        if v >= 90 :
            print( k , v ,"bal bilan " ,"Alo baxo ")
        elif v >= 70:
            print(k,  v ,"bal bilan " , "Yaxshi")
        elif v >= 60:
            print(k ,  v ,"bal bilan " ,"Qoniqarli ")
        else:
            print(k  ,  v ,"bal bilan " ,"Yiqildingiz ! ")

baxo(Ali = 95, emil = 89, ibrohim = 114, saman = 50, doni = 70)


# def kalkulyator(a, amal, b):
#     if amal == "+":
#         return a + b
#     elif amal == "-":
#         return a - b
#     elif amal == "*":
#         return a * b
#     elif amal == "/":
#         if b == 0:
#             return "Xato maxraj"
#         return a / b
#     else:
#         return "Bunday amal mavjud emas ! "
#
# while True:
#     amal = input("Amal kiriting (+, -, *, /) yoki stop : ")
#     if amal == "stop":
#         print("dastur tugadi ! ")
#         break
#     a = int(input("Birinchi sonni kiriting : "))
#     b = int(input("Ikkinchi sonni kiriting : "))
#     result = kalkulyator(a, amal, b)
#     print("Natija", result)

















