#Random number
import random as R
Random_number=R.randint(1,1000)
print(Random_number)
#random string
import string as s
string_alphanums=s.ascii_letters+s.digits
random_string=''
for i in range(int(input("string Length"))):
    random_string+=R.choice(string_alphanums)
print(random_string)