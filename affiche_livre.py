class livre:
    def __init__(self,titre,auteur,isbn):
        self.titre=titre
        self.auteur=auteur
        self.isbn=isbn
        self.disponible=True
    
    def afficher_livre(self):
        disponibilite="disponible" if self.disponible  else "emprunté"
        print(f"titre du livre : {self.titre},auteur : {self.auteur},disponibilité: {disponibilite}") 

    def emprunter(self):
        if self.disponible:
            print(f"ce livre est emprunté")
        else:
            print(f"ce livre n'est pas disponible")
    
    def retouner(self):
        if not self.disponible:
            self.disponible=False
            print(f"ce livre {self.titre} a ete retouné")
        else:
            print(f"le lvre {self.titre} est deja disponible")

livre1=livre("ma tente","N.cho val","IN8956")
livre1.afficher_livre()
livre1.emprunter()
livre1.retouner()
        