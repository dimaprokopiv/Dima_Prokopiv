# def find_avarage(*args):
#     sum=0
#     count=0
#     for i in args :
#         sum+=int(i)
#         count+=1
#     return sum/count    
# print("avarage is :",find_avarage(11,10,12))

# def make_absolute(number):
#     if number >=0 : return number
#     else : return -number

# def max_number(num1,num2):
#     """Finds max number"""
#     if(num1>num2): return num1
#     elif (num1==num2) : 
#         print("numbers r equal")
#         return num1 
#     else : return num2
# print("max number is:",max_number(12,12)) 



###### task 4 squares


      
def square_rectangle(a,b):
    return a*b

def square_circle(radius):
    return 3.14*(radius**2)

def square_triangle(a,b,c):
    p=(a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5

choice=int(input("if u want square of triangle type 1 , for circle type 2, for rectangle type 3 :"))

if choice ==1 :
    print("now input 3 sides")
    side1=float(input("input side1:"))
    side2=float(input("input side2:"))
    side3=float(input("input side3:"))
    print("square of triangle is",square_triangle(side1,side2,side3))
elif choice == 2 :
    radius=float(input("input radius:"))
    print("square of circle is :",square_circle(radius))
elif choice == 3 :
    side1 = float(input("input side1:"))
    side2 = float(input("input side2:"))
    print("square of rectangle is:",square_rectangle(side1,side2))
else : print("u did something wrong , restart the program(")




