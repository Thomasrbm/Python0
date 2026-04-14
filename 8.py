
# --------------------------------
# def countdown(n):
# 	yield 1
# 	yield 2
# 	yield 3
# 	yield 4
# 	yield 5
# 	yield 6
# 	yield 7

# #  ici le for fait val recoit le yield de countdown, comme le yield s arrete jamais il va jusqu a 7 donc pas de stop en fonction de N 
# for val in countdown(5):
#     print(val)




# --------------------------------


# def countdown(n):
# 	yield 1
# 	yield 2
# 	yield 3
# 	yield 4
# 	yield 5
# 	yield 6
# 	yield 7


# #  part de 5, stop a -1 et -1 a chaque tours (le step)   
# for i in range(5, 0, -1) :
# 	val = countdown(1)  # ne marche pas car on recret le generateur a chaque fois a chaque iteration
# 	print(val)


# --------------------------------




# def countdown(n):
# 	yield 1
# 	yield 2
# 	yield 3
# 	yield 4
# 	yield 5
# 	yield 6
# 	yield 7

# val = countdown(1) #val debient le generateur, pas le yield returned.

# # use next permet d avancer au prochain yield ici
# for i in range(5, 0, -1) :
# 	# next(val)
# 	# print(val) // ca, ca print le generateur object et pas sa value
# 	print(next(val)) # next iterer dessus et renvoit son retour.

# --------------------------------



# def countdown(n):
# 	yield 1
# 	yield 2
# 	yield 3
# 	yield 4
# 	yield 5
# 	yield 6
# 	yield 7



# x = countdown(1)
# print(next(x))
# print(next(x))