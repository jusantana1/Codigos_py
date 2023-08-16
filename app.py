lista = []
resp = "S"

def alterar (): # função para calcular novo valor
    alterar = input ("\nDigite o nome da musica que deseja alterar o valor:  ")
    for musica in lista: 
        if alterar == musica[0]:
            if musica[2] < 10.00:
                musica[2] = musica[2] * 2
            else:
                musica[2]= musica[2]* 0.5
            print (f"Novo valor: {musica[2]}")
        else: 
            print("Musica nao encontrada")
    

def exibir (): #funçao para exibir a lista
    for musica in lista:
        print(f"\nMusica: {musica[0]}" )
        print(f"Cantor: {musica[1]}" )
        print(f"Valor: {musica[2]}" )
        print(f"Quantidade: {musica[3]}" )

def buscar(): #função para buscar uma musica pelo nome do cantor
    busca = input ("\nDigite o nome do cantor que deseja buscar: ")
    for musica in lista: 
        if busca == musica[1]:
            print(f"Musica: {musica[0]}")
            print(f"Valor: {musica[2]}")
            print(f"Quantidade: {musica[3]}")
        else : 
            print("Cantor nao encontrado")


while resp == "S":
    musica= [ input("\nMusica: "),
             input("Cantor: "),
             float (input ("Valor: ")),
             int(input("Quantidade: ")) ]
    lista.append(musica)
    resp = input("\nDigite \"S\" para continuar:  ").upper()







