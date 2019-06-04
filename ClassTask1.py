#	Написати скрипт, який з двох введених чисел визначить, яке з них більше, а яке менше.



first_number=input("Input first number")
second_number=input ("Input second number")
if first_number>second_number:
    print ("{} is bigger than {}".format(first_number,second_number))
elif second_number>first_number:
    print ("{} is bigger than {}".format(second_number,first_number))
else:
    print ("{} is equal to {}".format(first_number,second_number))



