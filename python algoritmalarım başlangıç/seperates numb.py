#write a python code that seperates numbers 1 to 50 as even orr odd.
evens=[i for i in range(1,51) if i%2==0]
odds=[i for i in range(1,51) if i%2==1]
print(f" ÇİFT SAYILAR:\n {evens}")
print(f"TEK SAYILAR:\n {odds}")