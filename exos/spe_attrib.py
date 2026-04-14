

# Niveau 1 : La carte d'identité (__str__ vs __repr__)

# class Livre() :
#     def __init__(self, title = "L'alchimiste", author = "Paolo Coehllo"):
#         self.title = title
#         self.author = author 
#     def __str__(self) :
#         return f"{self.title} par {self.author} "
#     def __repr__(self):
#         return f"Livre(titre='{self.title}', auteur='{self.author}'"


# a = Livre()

# print(a)
# print(repr(a))






# Niveau 2 : Inspecter les entrailles (__dict__ et __class__)

# chaque variable d une classe est stock dans un dico appele dict

# class Smartphone:
#     def __init__(self, marque, modele):
#         self.marque = marque
#         self.modele = modele

# tel = Smartphone("Apple", "iPhone 15")

# print(tel.__dict__)

# print(tel.__class__.__name__)





# Niveau 3 : L'objet qui se prend pour une fonction (__call__)

# class Multiplicateur():
# 	def __init__(self, n) :  # attribu quand on cree l instance le n
# 		self.n = n
# 	def __call__(self, mult): # attribe le mult quand on l use comme fonction
# 		return self.n * mult

# double = Multiplicateur(2)
# print(double(10)) # Doit afficher 20





# Niveau 4 : L'objet qui se prend pour une liste (__len__ et __getitem__)




# class Equipe():
# 	def __init__(self, membres):
# 		self.membres = membres
# 	def __len__(self):
# 		return len(self.membres)
# 	def __getitem__(self, n):
# 		return self.membres[n]


# team = Equipe(['leo', 'roro', 'neyney'])

# print(len(team))

# print(team[0])










# Niveau 5 : La doc et les fichiers (__doc__ et __file__)


# def nul():
# 	"""rien"""
# 	pass


# print(nul.__doc__)
# print(__file__)


















# Niveau 7 : Le plan de bataille : __mro__ (Method Resolution Order)


# class A:
#     def saluer(self):
#         print("Hello de A")

# class B(A):
#     def saluer(self):
#         print("Hello de B")

# class C(A):
#     def saluer(self):
#         print("Hello de C")

# class D(B, C):
#     def saluer(self):
#         super().saluer() # permet d appeler celui du parent aussi
#         print("Hello de D")

# objet_d = D()
# objet_d.saluer()

# print("\nPlan de bataille (MRO) :")
# print(D.__mro__)

# Niveau 8 : L'optimiseur de mémoire : __slots__





# class JoueurNormal():
# 	def __init__(self, pseudo, score):
# 		self.pseudo = pseudo
# 		self.score = score



# class JoueurOptimise():
# 	__slots__ = ('pseudo', 'score')
# 	def __init__(self, pseudo, score):
# 		self.pseudo = pseudo
# 		self.score = score
	


# j1 = JoueurNormal("tueur", 5000)

# print(j1.__dict__)

# j1.couleur = "rouge"

# print(j1.__dict__)



# j2 = JoueurOptimise("Roro", 100)
# j2.age = 25

