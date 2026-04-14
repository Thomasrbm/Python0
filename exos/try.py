



# exo 1 --------------------------------

# def div_100():
#     rep = input("Entrez un nombre : ")
#     return 100 / int(rep) 


# try :
#     print(div_100())
# except Exception as e :
#     print(f"error : {e}")

    


# exo 2 --------------------------------



# def connect() :
#     mdp = input("mdp ? : ")
#     if mdp == "1" :
#         return True
#     else :
#         raise AssertionError("ALEEEEEEEEEEERTE TENTATIVE D'INTRUSION !!!!!!")


# try :
#     ret = connect()
# except Exception as e :
#     print(f"Error raised : {e}")
# else :
#     print(f"Traitement réussi : {ret} received")
# finally :
#     print("Ending connexion...")

# exo 3 --------------------------------


# class AgeInvalideError(Exception) :
#     def __init__(self, age):
#         self.age = int(age)
#         if self.age > 150 :
#             self.message = "Age too high"
#         elif self.age < 0 :
#             self.message = "Age too little"
#         super().__init__(self.message)



# def verifier_age() :
#     age = input("Entrer age : ")
#     if int(age) > 150 or int(age) < 0 :
#         raise AgeInvalideError(age)
#     else :
#         print(age)


    
# try:
#     verifier_age()
# except Exception as e :
#     print(f"error : {e}")




# exo 4 --------------------------------

# def calcul_interne(n : int) :
#     if n == 0:
#         raise ZeroDivisionError("Log interne : division par zéro détectée")
#     else :
#         return 10 / n
        

# def interface_user() :
#     nb = input("entre un chiffre : ")
#     try :
#         res = calcul_interne(int(nb))
#     except Exception :
#         raise
#     else :
#         return res


# try:
#     print(interface_user())
# except Exception as e :
#     print(f"Alerte utilisateur : calcul impossible")



# exo 5 --------------------------------




# while True :
#     try :
#         rel = input()
#         if rel == "quit" :
#             break
#     finally :
#         print("Nettoyage du cycle")



#  utile dans le cas ou :

# while True:
#     try:
#         nom_fichier = input("Fichier à traiter : ")
#         f = open(nom_fichier, "r")
#         # ... traitement ...
#     finally:
#         f.close() # On garantit que le fichier est fermé AVANT de demander le suivant