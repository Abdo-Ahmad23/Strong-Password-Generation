import string
import random
import math
class Password:
    upper_percent=.3
    lower_percent=.3
    digit_percent=.3
    punc_percent=.1
    def set_len(self):
        while True:
            choice=int(input("Please Enter Your length: "))
            try:
                if choice>=6:
                    return choice
                else:
                    print("Please Enter a valid number >= 6")
            except:
                print("Print a number not character.")
        

    def set_strings(self):
        self.upper_string=list(string.ascii_uppercase)
        self.lower_string=list(string.ascii_lowercase)
        self.digit_string=list(string.digits)
        self.punc_string=list(string.punctuation)
    
    def shuffle_strings(self):
        self.set_strings()
        random.shuffle(self.upper_string)
        random.shuffle(self.lower_string)
        random.shuffle(self.digit_string)
        random.shuffle(self.punc_string)
    
    def last_method(self):
        length=self.set_len()
        self.shuffle_strings()
        password=[]
        part1=round(self.upper_percent * length)
        part2=round(self.lower_percent * length)
        part3=round(self.digit_percent * length)
       
        part4=round(self.punc_percent * length)
       
       
        for i in range(part1):
            password.append(self.upper_string[i])

        for i in range(part2):
            password.append(self.lower_string[i])

        for i in range(part3):
            password.append(self.digit_string[i])

        for i in range(part4):
            password.append(self.punc_string[i])
        random.shuffle(password)
        password="_".join(password)
        print(password)


example=Password()
example.last_method()


    
    
