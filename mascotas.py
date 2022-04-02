class mascotas:
    def __init__(self, tipo, raza, tamaño, color, granja, domestico, animalCompañia, fines_economicos, onomatopeya):
        self.tipo= tipo 
        self.raza= raza
        self.tamaño= tamaño
        self.color= color
        self.granja= granja 
        self.domestico= domestico
        self.animalCompañia= animalCompañia
        self.fines_economicos= fines_economicos
        self.onomatopeya= onomatopeya
        
    def acariciarAnimal(self):
        print(self.onomatopeya)

    def precio(self, precioMin):
        precio=0
        if self.domestico==True:
            precio=precio+15000
        if self.granja==True:
            precio=precio+25000
        if self.animalCompañia==True:
            precio=precio+35000
        if self.fines_economicos==True:
            precio=precio+50000
        if precio < precioMin:
            precio = precioMin
        print(precio)



Jorge=mascotas("perro", "chipchu", "pequeño", "cafecito con blanco", False, True, True, False, "guau")
Marianita=mascotas("vaca", "Fluffy Cows", "mediana", "cafecita", True, False, False, False, "muuuu")
Doña_juana=mascotas("vaca", "Holstein", "grande", "dalmata", True, False, False, True, "muuuu")

Marianita.acariciarAnimal()
print("---------------------")
Jorge.acariciarAnimal()
print("---------------------")
Doña_juana.acariciarAnimal()
print("---------------------")

Marianita.precio(20000)
print("---------------------")
Jorge.precio(10000)
print("---------------------")
Doña_juana.precio(70000)
print("---------------------")