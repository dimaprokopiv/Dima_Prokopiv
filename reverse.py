#You need to write a function that reverses the words in a given string.
#A word can also fit an empty string.
#If this is not clear enough, here are some examples:
#reverse('Hello World') == 'World Hello'
#reverse('Hi There.') == 'There. Hi'
#As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

def reverse(st):
    result=""
    my_string= st.split()
    my_string.reverse()
    result=" ".join(my_string)
    return result