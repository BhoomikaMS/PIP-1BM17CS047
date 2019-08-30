import string 
import random

result=string.ascii_letters+string.digits+string.punctuation

def rand_password(size):
	pwd=''.join([random.choice(result) for n in range(size)])
	return pwd
n=int(input("Enter the size of password: "))
password=rand_password(n)
print("Password: ",password)
