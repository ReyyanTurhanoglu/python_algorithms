#write python code that extracts the phone number in a given string expression.


#  Example:
# ->-> given_str="My phone number is (111) 222-33-44"
# ----> output=1112223344

numara=""
cumle=input("bir metin giriniz:")
for i in cumle:
    if(i.isnumeric()):
        numara+=i
print(f"telefon numaranız:{numara}")