import string  
import random

if __name__ == "__main__":
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation

    pass_len=int(input("Enter password length: "))
    while pass_len<8:
        print("Password must be at least 8 characters long")
        pass_len=int(input("Enter password length: "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    print ("Your password: ", end="")
    print ("".join([random.choice(s) for _ in range(pass_len)]))