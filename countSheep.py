#Consider an array of sheep where some sheep may be missing from their place. 
#We need a function that counts the number of sheep present in the array (true means present).
def count_sheeps(arrayOfSheeps):
    counter=0
    for i in arrayOfSheeps :
        if i== True:
            counter+=1
    return counter