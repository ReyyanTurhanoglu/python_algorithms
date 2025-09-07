# Anagram kelimeler,aynı harflere sahip ancak farklı düzenlenmiş dizeleri ifade eder.
# Verilen bir dizedeki anagramları gruplayın.
# Çıktınızın sırası önemli değil.
# Input: ("eat","tea","tan","eat","nat","bat")
# Output: (("eat","eat","tea"),("tan","nat"),("bat"))
list1=["eat","tea","tan","eat","nat","bat"]
result={}
for item in list1:
    x="".join(sorted(item))
    if x not in result:
        result[x]=[item]
    else:
        result[x].append(item)
print(list(result.values()))



