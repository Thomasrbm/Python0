
# exo 1 

# t_list = [15, 42.2, True, "str", ["asd", 42]]

# for elem in t_list :
#     print(type(elem).__name__)



# exo 2 


# donnees = [10, "Python", 3.14, True, "Code", 42, [1, 2]]

# nombres = []

# for i in donnees :
#     if isinstance(i, int) and i != True or False :
#         nombres.append(i)

# print(nombres)

# # exo 3



# class Vehicule :
#     pass

# class Voiture(Vehicule) :
#     pass

# ma_caisse = Voiture()

# print(f"ma caisse instance de Voiture ? : {isinstance(ma_caisse, Voiture)}")
# print(f"ma caisse instance de Vehicule ? : {isinstance(ma_caisse, Vehicule)}")
# print(type(ma_caisse))





# exo 4

# def calculer_surface(rayon) :
#     if type(rayon) != int and not float :
#         raise ValueError("Not an int nor a float")
#     surface_cercle = 3.14 * (rayon * rayon)
#     return surface_cercle


# try :
#     print(calculer_surface(5.5))
# except ValueError as e :
#     print(f"Error : {e}")

# exo 5


# user = {"nom": "Alice", "age": 25, "score": 95.5, "admin": False}


# for elem in user :
#     if isinstance(user[elem], str) :
#         print(elem)