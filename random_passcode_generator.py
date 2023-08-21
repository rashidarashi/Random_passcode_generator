import random
Alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Numbers = ["1","2","3","4","5","6","7","8","9","0"]
Symbols = ["~","!","@","#","$","%","^","&","*","(",")","_"]
# a = Alphabets+Numbers+Symbols
# print(a)
alphabet_input = int(input("Enter the number of Alphabet Inputs required : "))
number_input = int(input("Enter the number of Number Inputs required : "))
symbol_input = int(input("Enter the number of Symbol Inputs required : "))
alpha = random.choices(Alphabets, k = alphabet_input)
num = random.choices(Numbers, k = number_input)
sym = random.choices(Symbols, k = symbol_input)
password_generated = alpha+num+sym
# print(password_generated)
random.shuffle(password_generated)
print(password_generated)