from random import randint, choice


Cap_letters=['A','B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
samll_letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=['1','2','3','4','5','6','7','8','9','0']
sym=['!','@','#','$','%','^','*',]

def password_gen():
    password=[]

    password_letters=[choice(Cap_letters)  for _ in range(randint(2,8))]
    password_letters_2=[choice(samll_letter)  for _ in range(randint(2,4))]
    password_num=[choice(num)  for _ in range(randint(1,2))]
    password_sym=[choice(sym)  for _ in range(randint(0,3))]

    password=password_letters+password_letters_2+password_sym+password_num
        
    password =''.join(password)
    return password
    

    


        




