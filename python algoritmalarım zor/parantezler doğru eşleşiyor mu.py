# parantezlerden oluşan bir dize verildiğinde parantezlerin doğru sırada ve aynı tip parantez ile açılıp kapatıldığını
# teyit eden bir algoritma oluşturun
# Example 1: Input: s="()"      >>  Output:True
# Example 2: Input: s="()[]{}"  >>  Output:True
# Example 3: Input: s="(]"      >>  Output:False
# Example 4: Input: s="([)]"    >>  Output:False
# Example 5: Input: s="{[]}"    >>  Output:True

def parantez(liste):
    while "()" in liste or "[]" in liste or "{}" in liste:
        liste=liste.replace("()","").replace("[]","").replace("{}","")
    print(liste=="")

parantez("()[]{}(")






