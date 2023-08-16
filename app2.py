from app import *

# menu de decição
print("\nEscolha uma das opcoes abaixo:\n")
print("1 - Exibir lista")
print("2- Buscar pelo cantor")
print("3- Alterar o valor ")
opc = int (input("\n> ")) 

if opc == 1:
    exibir()
elif opc ==2:
    buscar()
elif opc ==3:
    alterar()
else :
    print("Opcao invalida")