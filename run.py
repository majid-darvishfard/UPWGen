import string
import random

class UPWGen:
    SAMPLE_1 = ['a','b','c','d','e','f','g','h','i','k','l','o','q','s','t','v','x','y']
    SAMPLE_2 = [
        ['@','^','A','a'],['b','8','B'],['c','(','30','C'],['6','D','d'],['3','E','e'],
    ['#','F','f'],['9','G','g'],['#','H','h'],['i','!','1','I'],['i<','K','k'],['L','l'],['0','*','O','o'],['9','Q','q'],['5','$','z','S','s'],['t','+','T'],['<','v','>','V'],['x','%','X'],['y','?','Y']
        ]
    

    def _validate_password(self, password):
        if len(password) < 6:
            raise ValueError("password must not be lower than 6.")
        elif string.digits not in password:
            raise ValueError("password must have at least one number in it.")
        elif string.ascii_lowercase not in password:
            raise ValueError("password must have at least one lowercase character in it.")
        elif string.ascii_uppercase not in password:
            raise ValueError("password must have at least one uppercase character in it.")
        else:
            return True
    
    def _validate_username(self, username):
        if 4 < len(username) < 20:
            raise ValueError("username must be within 4 to 20 characters.")
        else:
            return True

    def _give_pw(self, pw_length):
        password = ''
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

        for _ in range(pw_length):
            password += random.choice(chars)
        
        return password

    def _generate_user_pw(self, username):
        #chars = string.ascii_letters
        #digit=string.digits
        passwords=[]
        for char in username:
            if char in self.SAMPLE_1:
                item_index = self.SAMPLE_1.index(char)
                if isinstance(self.SAMPLE_2[item_index], list):
                    replace_item = str(random.choice(self.SAMPLE_2[item_index]))
                else:
                    replace_item=str(self.SAMPLE_2[item_index])
                passwords.append(replace_item)
            elif char.isalpha():
                replace_item = char.upper()
                passwords.append(replace_item)
            else:
                passwords.append(char)

        return "".join(passwords)

    def _gen_username(self,firstname,lastname,birthday=None):
        if ' ' in lastname:
            lastname=lastname.replace(' ','')
        if birthday == None:
            first_part=[firstname,firstname[0],lastname]
            middel_part=['.','_',lastname]
            last_part=[firstname,lastname]
        else:
            first_part=[firstname,firstname[0],lastname]
            middel_part=['.','_',lastname]
            last_part=[firstname,lastname,birthday]

        first= str(random.choice(first_part))
        middel= str(random.choice(middel_part))
        while first == middel :
            middel= str(random.choice(middel_part))

        last = str(random.choice(last_part))
        while last == middel or last == first :
            last = str(random.choice(last_part))
            
        #for debug
        #print('first: {} - middel: {}  - last:{}'.format(first,middel,last))  
        username=first + middel + last 
        return username


    @classmethod
    def gen_pw(cls, pw_length = 6, reports = 1):
        if pw_length < 6:
            raise ValueError("password must not be lower than 6.")
        
        return [cls._give_pw(cls, pw_length) for _ in range(reports)]

    @classmethod
    def gen_upw(cls, username, reports = 1):
        return [cls._generate_user_pw(cls, username) for _ in range(reports)]
    
    @classmethod
    def generate_username(cls, first_name, last_name,birthday=None, reports = 1):
        return set([cls._gen_username(cls,first_name,last_name,birthday) for _ in range(reports)])


if __name__ == __main__:
    print(UPWGen.generate_username('majid','darvish fard',birthday=1398,reports=3))
