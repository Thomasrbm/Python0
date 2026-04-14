



# Exo 1  --------------------------------------------



# inventaire = ["Pierre", "Potion", "Arc"]
# stats = ("Snake", 100, 9)  # (nom, hp, level)


# inventaire.remove("Pierre")
# inventaire.append("Épée")
# inventaire.append("Bouclier")

# print(inventaire)


# print(stats[1])



# Exo 2  --------------------------------------------



# user_a = {"read", "write", "delete", "admin"}
# user_b = {"read", "write", "execute"}

# # Ton code ici : intersection, différence, frozenset admin


# diff = user_a.difference(user_b)
# inter = user_a.intersection(user_b)

# #  OU 

# diff2 = user_a - user_b # les operateur peuvent servir de shortcuts pour les methods
# inter2 = user_a & user_b

# print(f"diff = {diff}")
# print(f"inter = {inter}")


# frozen = frozenset()





# Exo 3  --------------------------------------------


# cache = {1001: "bash", 1002: "syslogd", 1003: "sshd"}

# # Ajoute PID 1004: "systemd" et 1005: "python3"
# # Supprime PID 1001
# # Affiche les processus dont le nom commence par "sys"

# for i in cache :
#     e = cache.get(i)
#     if e.startswith("sys") :
#         print(e)

# cache.pop(1001)
# cache.update({1004 : "systemd", 1005 : "python3"})

# print(cache)



# Exo 4  --------------------------------------------


# from collections import deque
# from array import array

# buffer = deque(maxlen=5)
# sizes = array('I', [])  # 'I' = unsigned int

# sizes.extend([40, 20 , 1500 , 20 ,40 ,100])

# # Ajoute les paquets: "SYN","ACK","DATA","FIN","RST","PUSH" dans buffer deque 
# # Ajoute leurs tailles: 40,20,1500,20,40,100 dans sizes
# # Affiche le buffer (5 max) et la taille totale des paquets

# buffer.append("SYN")
# buffer.append("ACK")
# buffer.append("DATA")
# buffer.append("FIN")
# buffer.append("RST")
# buffer.append("PUSH")

# print(buffer)
# print(sizes)







# Exo 5 --------------------------------------------


# des list qui donne acces prio au plus petit elem par defaut ou max si on config



# import heapq

# tasks = []
# status = {"cleanup" : "undone", "kernel_panic" : "undone", "malloc" : "undone", "segfault" : "undone"}

# heapq.heapify(tasks)
# heapq.heappush(tasks, (3, "cleanup"))
# heapq.heappush(tasks, (1, "kernel_panic"))
# heapq.heappush(tasks, (2, "malloc"))
# heapq.heappush(tasks, (1, "segfault"))

# print(status)
# print(tasks)

# for i in range(0, 2, 1) :
#     priority, task = heapq.heappop(tasks)
#     print(task)
#     status[task] = "done"



# print(tasks)
# print(status)


# Ajoute ces tâches avec heapq.heappush:
# (3, "cleanup"), (1, "kernel_panic"), (2, "malloc"), (1, "segfault")
# Exécute les 2 premières tâches (heappop) et marque-les "done" dans status
# Affiche les tâches restantes et le status dict










# Exo X  --------------------------------------------

# "iterer sur des set + prouver que frozen pas modif"

# permissions_user  = {"read", "write", "execute", "admin"}
# PERMISSIONS_ROOT  = frozenset({"admin", "delete", "root", "sudo"})

# # 1. Itère sur permissions_user et affiche chaque permission en majuscules

# # 2. Itère sur PERMISSIONS_ROOT et affiche uniquement les perms de + de 4 lettres

# # 3. Essaie d'ajouter "write" à PERMISSIONS_ROOT dans un try/except
# #    et affiche le type de l'erreur attrapée


# for i in permissions_user:
#     print(f"{i.upper()} ", end = "")

# print()

# for i in PERMISSIONS_ROOT:
#     if len(i) > 4:
#         print(f"{i} ", end = "")

# try :
#     PERMISSIONS_ROOT.add("asd")
# except AttributeError as e:
#     print()
#     print(f"error : {e}")
    













# Exo y  --------------------------------------------

#  use each methods of every container


# Exo — use each methods of every container
# list / tuple / set / dict
# Contrainte : utilise AU MOINS UNE FOIS chaque méthode native du container

# ============================================================
# DATASET de base — ne pas modifier
# ============================================================

scores     = [12, 7, 19, 4, 19, 3, 7]        # list
coords     = (48.8566, 2.3522, "Paris")       # tuple
tags       = {"python", "c", "linux", "asm"}  # set
registry   = {"pid": 1337, "name": "kash",    # dict
              "status": "running", "cpu": 0.4}

# ============================================================
# LIST — méthodes à utiliser :
# .append() .extend() .insert() .remove() .pop() .index()
# .count()  .sort()   .reverse() .copy()  .clear()
# ============================================================


# # 1. Ajoute le score 15 à la fin
# scores.append(15)

# print(scores)

# # 2. Étends avec [8, 22, 1]
# scores.extend([8, 22, 1])

# print(scores)

# # 3. Insère 99 à l'index 2
# scores.insert(2, 99)

# print(scores)

# # 4. Retire la première occurrence de 7
# for i in scores :
#     if i == 7:
#         scores.remove(i)
#         break

# print(scores)

# # 5. Pop le dernier élément, stocke-le dans `last`
# last = scores.pop()

# print(f"last = {last}")

# # 6. Trouve l'index de 19 (première occurrence)
# ind = scores.index(19)
# print(f"index de 19 = {ind}")


# # 7. Compte combien de fois 19 apparaît

# count = scores.count(19)
# print(f"nb de 19 = {count}")

# # 8. Trie la liste

# scores.sort()
# print(scores)

# # 9. Inverse-la

# scores.reverse()
# print(scores)

# # 10. Copie-la dans `scores_backup`

# scores_backup = scores.copy()
# print (f"backup = {scores_backup}")

# # 11. Clear scores_backup (la liste copiée, pas l'originale !)

# scores_backup.clear()
# print(scores_backup)







# ============================================================
# TUPLE — méthodes à utiliser :
# .count()  .index()
# + unpacking, slicing, len(), in
# ============================================================

# # => coords

# print(coords)

# # 12. Compte combien de fois "Paris" apparaît dans coords
# cnt = coords.count("Paris")
# print(f"cnt = {cnt}")

# # 13. Trouve l'index de 2.3522

# ind = coords.index(2.3522)
# print(f"ind = {ind}")

# # 14. Unpacke coords en 3 variables : lat, lon, city

# lat, lon, city = coords

# print(f"lat = {lat} \nlon = {lon} \ncity = {city}")

# # 15. Slice les deux premiers éléments dans `geo`

# geo = coords[0:2]
# print(geo)

# # 16. Vérifie si "Paris" est dans coords avec `in`

# if "Paris" in coords:
#     print("yes")
# else :
#     print("no")






# ============================================================
# SET — méthodes à utiliser :
# .add() .discard() .remove() .pop() .copy()
# .union() .intersection() .difference() .issubset()
# .issuperset() .update() .clear()
# ============================================================

# => tags

other_tags = {"rust", "linux", "nix"}
print(other_tags)

# 17. Ajoute "vulkan" au set

other_tags.add("vulkan")
print(other_tags)

# 18. Discard "asm" (sans erreur si absent)

if "asm" in other_tags:
    other_tags.discard("asm")
else :
    print("asm is not in set")

# 19. Remove "c" (lève KeyError si absent — c'est voulu, wrappe en try/except)

try :
    other_tags.remove("c")
except KeyError as e :
    print(f"error : {e} is not in set")

# 20. Pop un élément aléatoire, stocke dans `popped_tag`

popped_tag = other_tags.pop()
print(f"random popped = {popped_tag}")

# 21. Copie tags dans `tags_backup`

tags_backup = other_tags.copy()
print(f"tag_backup = {tags_backup}")

# 22. Union de tags et other_tags dans `all_tags`

all_tags = tags.union(other_tags)
print(all_tags)

# 23. Intersection dans `common_tags`

print(tags)
print(other_tags)
common_tags = other_tags.intersection(tags)
print(f"intersection = {common_tags}")

# 24. Différence tags - other_tags dans `only_tags`

print()

only_tags = tags - other_tags
print(f"unic tags = {only_tags}")



# .issubset()
# .issuperset() .update() .clear()

# 25. Vérifie si {"linux"} est subset de all_tags


if all_tags.issubset({"linux"}) :
    print("yes")

# 26. Vérifie si all_tags est superset de {"nix"}



# 27. Update tags avec {"opengl", "glsl"}


other_tags.update({"opengl", "glsl"})
print(other_tags)

# 28. Clear tags_backup





# ============================================================
# DICT — méthodes à utiliser :
# .get() .keys() .values() .items()
# .update() .pop() .popitem() .setdefault()
# .copy() .clear() .fromkeys()
# ============================================================


# => registry 


# 29. Get "cpu" avec valeur par défaut 0.0
# 30. Affiche toutes les keys
# 31. Affiche toutes les values
# 32. Itère sur .items() et affiche "key → value"
# 33. Update registry avec {"cpu": 1.2, "mem": 512}
# 34. Pop "status", stocke dans `old_status`
# 35. Popitem() — récupère et affiche le dernier item inséré
# 36. Setdefault "priority" à 5 (ne doit pas écraser si existant)
# 37. Copie registry dans `reg_backup`
# 38. Crée un dict depuis une liste de clés avec fromkeys(["a","b","c"], 0)
# 39. Clear reg_backup