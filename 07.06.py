
#for value in range(counter):
#   element = int(input("enter element"))
#   my_list.append(element)

my_list = [int(input("input your numbers of your list:")) for element in range(int(input("input number of elements"))) ]    

max_number=0
min_number=100000000000000000000000000000
for i in my_list:
    if i>= max_number:
        max_number=i

for i in my_list:
    if i<= min_number:
        min_number=i

print("max number is :{}, min number is :{}".format(max_number,min_number))
        