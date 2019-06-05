#Задано чотирицифрове натуральне число. 
#Знайти добуток цифр цього числа.
#Записати число в реверсному порядку.
#Посортувати цифри, що входять в дане число

number=int(input("pls input number:"))
numeral_4=number%10
numeral_3=int(number%100/10)
numeral_2=int(number%1000/100)
numeral_1=int(number%10000/1000)
multiplication=numeral_1*numeral_2*numeral_3*numeral_4
print("{}*{}*{}*{}={}".format(numeral_1,numeral_2,numeral_3,numeral_4,multiplication))