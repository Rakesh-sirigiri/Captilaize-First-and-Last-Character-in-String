test_str = "hello world"
print("String before:", test_str)
string = ""
for i in test_str.title().split():
    string += (i[:-1] + i[-1].upper()) + ' '
print("String after:", string.strip())
