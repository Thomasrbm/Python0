# Exo 1 — générateur de pairs
# Écris un générateur evens(n) qui yield les nombres pairs de 0 jusqu'à n inclus.


# def count_pair(n : int):
# 	for i in range(0, n + 1, 2): # n + 1 car range exclut le stop,  0, 10  il s arrete a 9 pas 10, car parcours 10 case en partant de 0 (jusqu a 9)
# 		# if i < n: pas besoin range le gere tout seul
# 		yield i

# x = count_pair(10)

# for i in x:
# 	print(i)

# -------------------------------------------------


# Exo 2 — générateur infini
# Écris un générateur counter(start) qui yield les entiers à partir de start sans jamais s'arrêter. Utilise next() manuellement pour en récupérer 5 valeurs.


# def inf_counter(n : int):
# 	yield n 
# 	n += 1 # s arrete apres 1 next car plus de yield a produire.

# def inf_counter(n : int):
# 	for i in range(n, n + 2, 1): # range marche pas il est calculer une seule fois au debut du for
# 		yield i
# 		n += 1

# def inf_counter(n : int):
# 	while True	: # range marche pas il est calculer une seule fois au debut du for
# 		yield n
# 		n += 1


# x = inf_counter(15)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))





# -------------------------------------------------



# Exo 3 — générateur de fibonacci
# Écris un générateur fib() qui yield la suite de Fibonacci indéfiniment. Récupère les 8 premiers termes avec un for et range.



# def fib() :
# 	first = 0
# 	second = 1
# 	while True :
# 		yield first
# 		# first = second
# 		# second = first + second  ,  marche pas car tu modif first avant second faut le faire en simultanne
# 		first, second = second, first + second


# x = fib()

# for i in range(0, 9, 1) :
# 	print(next(x))	