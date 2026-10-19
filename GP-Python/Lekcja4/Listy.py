lista = ["Wychowanie fizycznie", "Taco Hemingway", "Matematyka", "Mikroekonomia",67]
#                0                      1               2               3         4
print(lista)
print(lista[0])
print(lista[3]) 
lista[1] = "Paktofonika" # zmienia rzecz pod indexem 1
print(lista)
lista.append("Program") # dodaje do listy
print(lista)
lista.remove(67) # usuwa z listy
print(lista)
print(len(lista)) # len od słowa len podaje dł listy
import random
print(lista[random.randint(0,len(lista)-1)]) # losowanie randomowej liczby. Zawsze len(...)-1
