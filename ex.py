class Person:
    def __init__ (self, nume, varsta):
        self.nume = nume
        self.varsta = varsta
    def __str__(self):
        return self.nume + " " + str(self.varsta)
    
person1 = Person("Ana", "30")
#print("Persoana: ", person1)

def createPersonList(lista1, lista2):
    lista_persoane = []

    l_lista1 = len(lista1)
    l_lista2 = len(lista2)

    for i in range(min(l_lista1,l_lista2)):
        lista_persoane.append(Person(lista1[i],lista2[i]))
        #print(lista_persoane)


    return lista_persoane
    
nume_test = ["Ana", "Mihai", "Andrei", "Mihai", "Alina"]
varsta_test = [10, 40, 20]
 
persoane = createPersonList(nume_test,varsta_test)

persoane_sorted = sorted(persoane, key = lambda v: v.varsta, reverse=False)

for elem in persoane_sorted:
    print(elem)

person1 = Person("Marin",12)

print(person1.varsta)

