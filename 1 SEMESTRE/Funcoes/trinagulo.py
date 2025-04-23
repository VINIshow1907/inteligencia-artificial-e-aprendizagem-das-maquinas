def main():
    lad1 = int(input("Digite o valor do primeiro lado: "))
    lad2 = int(input("Digite o valor do segundo lado: "))
    lad3 = int(input("Digite o valor do terceiro lado: "))
   
    if(lad1 == lad2 and lad2 == lad3):
        equilatero()
    elif(lad1 == lad2 or lad1 == lad3 or lad2 == lad3):
        isosceles()
    else:
        escaleno()
       
def equilatero():
    print("O triângulo é esquilátero!")
 
def isosceles():
    print("O triângulo é isósceles!")
 
def escaleno():
    print("O triângulo é escaleno!")
 
main()