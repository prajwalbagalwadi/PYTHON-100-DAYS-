#JAI SHREE RAM 
# encryption messaging techniques in python easy way to encrypt and decrypt the text message  

aalpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z''a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
msg=input("enter msg\n").lower()
encode_shift=int(input("shift number\n"))
decode_shift=int(input("shift number\n"))

def encode(text,encode_num):
    chiper_text=""
    for letter in text:
        indx=alpha.index(letter)
        new_indx=indx+encode_num
        new_letter=alpha[new_indx]
        chiper_text=new_letter
        ctxt=chiper_text
        print(f"{chiper_text }")
        

def decode(text,decode_num):
    decode_text=""
    for letter in text:
        indx=alpha.index(letter)
        new_indx=indx -decode_num
        new_letter=alpha[new_indx]
        chiper_text=new_letter
        print(f"{decode_txt }")

        
        
encode(msg,encode_shift)
decode(msg,decode_shift)

