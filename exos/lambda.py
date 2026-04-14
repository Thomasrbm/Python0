
# exo 1 ------------------------

# convertir : def calculer_carre(x):
#     return x * x => en lambda 

# d = lambda x : x * x
# print(d(5))



# exo 2 ------------------------


# somme = lambda a, b : a + b

# print(somme(5, 6))



# exo 3 ------------------------

# produits = [("Pomme", 1.5), ("Banane", 0.8), ("Cerise", 2.2)]

# # 0 trie ordr alpha des key 1 trie les numeriques de values

# recoit le tuple et revoit soit la key ou la value pour savoir comment trier
# produits.sort(key= lambda x : x[0])
# print (produits)

# exo 4 ------------------------


# utilisateurs = ["Alice", "Bob", "Chrystelle", "Dan"]

# utilisateurs.sort(key = lambda x : len(x))
# print(utilisateurs)

# exo 5 ------------------------

# nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# x = list(filter(lambda x : True if x % 2 == 0 else False, nombres)) # filter ne touche pas a la liste, il faut cree a un objet avec son return
# print(x)

# exo 6 ------------------------



# mots = ["python", "lambda", "code"]

# x = list(map(lambda x : x.upper() , mots))
# print(x)

# exo 7 ------------------------


# x = lambda x : "Adulte" if int(x) >= 18 else "Mineur"

# n = input("nombre : ")

# print(x(n))

# exo 8 ------------------------



# print((lambda x : x + 10)(5))