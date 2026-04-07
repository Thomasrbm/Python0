

ft_list = ["Hello", "World"] # https://docs.python.org/3/library/stdtypes.html#lists
ft_tuple = ("Hello", "France") # https://docs.python.org/3/library/stdtypes.html#tuples
ft_set = {"Hello", "le Havre"} # https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
ft_dict = {"Hello" : "42 le Havre"} # https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
 
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)


# list [] — ordonné, modifiable, doublons  => ordonne = garde l ordre ou tu les as range (ne re trie pas),
# tuple () — ordonné, non modfiable, doublons      => tu peux pas rajouter de truc apres sa creation  
# set {} — non ordonné, modifiable, pas de doublons => a chaque exec peut etre dans un sens ou l autre. 
# dict {clé: valeur} — ordonné (Python 3.7+), modifiable, clés uniques  = les map en c++



#     Ordonné     Modifiable      Doublons            Index
    
# list  ✅             ✅              ✅              ✅

# tuple ✅             ❌              ✅              ✅

# set   ❌             ✅              ❌              ❌

# dict  ✅             ✅              ❌         (clés)par clé