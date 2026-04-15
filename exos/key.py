

#  ex 1 ----------------------------

# lst = ["asdsada", "gdgdfgdfg", " fsfdgdsfgsdfg", "poizpxcvipozxivc"]

# if all(len(s) > 10 for s in lst) :
#     print("yes")
# else :
#     print("no")



# nbs = [87, 44675, 21731, 7842]

# if all('7' in str(s) for s in nbs) :
#     print("yes")
# else :
#     print("no")




#  ex 2 ----------------------------


# serv_list = {"serv1" : True, "serv2" : True, "serv3" : True, "serv4" : True}


# if any(state == False for state in serv_list.values()) :
#     print("at least one down")
# else :
#     print("every server running")



#  ex 3 ----------------------------

# fruits = ["pomme", "banane", "cerise", "datte", "orange"]

# for idx, fruit in enumerate(fruits) :
#     if idx % 2 == 0 :
#         print(fruit)


#  ex 4 ----------------------------

# nbs = ["849", "15", "23", "42", "116"]

# for idx, n in enumerate(nbs) :
#     if n == "42" :
#         print(idx)




#  ex 5 ----------------------------

# produits = ["Laptop", "Souris", "Clavier"]
# stocks = [15, 42, 8]

# combine = zip(produits, stocks)


# for pro, sto in combine:
#     print(f"Stock de {pro} quantite = {sto}")

#  ex 6 ----------------------------


# cles = ["nom", "age", "ville"]
# valeurs = ["Alice", 25, "Paris"]

# comb = zip(cles, valeurs)

# for key, val in comb:
#     print(f"{key} | {val}")


#  ex 7 ----------------------------


# with open("notes.txt") as file :
#     for line in file :
#         if len(line) > 10:
#             print(line)



# #  ex 8 ----------------------------

# with open("log.txt", "r") as file:
#     lines = file.readlines()

# #sinon write vide tout si on write direct
# with open("log.txt", "w") as file :
#     for line in lines :
#         if "jour" in line :
#             new_line = line.strip() + " : done nothing" + '\n'
#             file.write(new_line)
#         else:
#             file.write(line)