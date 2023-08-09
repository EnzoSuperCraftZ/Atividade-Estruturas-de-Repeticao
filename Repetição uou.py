import time
#Enzo Kai VIzalli, INFO 1°B


#escolher questão
q = str.upper(input("Escolha qual questão quer fazer: "))


#Questão 1:
if q == "1":
    for q1 in range(0,50):
        print(f"Número: {q1}")


#Questão 2:
elif q == "2":
    for q2 in range(2, 100, 2):
        print(f"Número: {q2}")


#Questão 3:
elif q == "3":
    contador = 20
    while contador > -1:
        print(contador)
        contador -= 1
        time.sleep(1)


#Questão 4:
if q == "4":
    for q4 in range(0,50,2):
        print(q4, end = "   ")


#Questão 5:
if q == "5":
    t = int(input("Mim dê um número: "))
    for q5 in range(1, 11):
        print("{} * {} = {}".format(t, q5, t * q5))


#Questão 6:
if q == "6":
    nome = str(input("Mim dê seu nome: "))
    for n in nome:
        print(n, end="/")


#Questão 7:
if q == "7":
    n1 = int(input("Me dê um número: "))
    while n1 != 0:
        


#Questão 8:
if q == "8":
    q8 = int(input("Mim dê um número: "))
    print("{}!: {} = {}".format(q8, q8 * q8 in range(q8, q8-1)))