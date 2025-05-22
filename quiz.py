print("Seja bem vindo ao quiz do Thiago!")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S":
    quit()

score = 0

print("Começando...")
print("Quem desenvolveu o Facebook? \n (A) Evan Spiegel \n (B) Mark Zuckerberg \n (C) Jackson Five \n (D) Lusie Mark \n")
answer_1 = input("Respostas: ")

if answer_1 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("O que significa a sigla WWW na internet ? \n (A) World Wide Web \n (B) Web World Wide \n (C) Web Wide World \n (D) N/D \n")
answer_2 = input("Respostas: ")

if answer_2 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual foi a primeira rede social da história da inernet? \n (A) MySpace \n (B) Classmate \n (C) Orkut \n (D) Twitter\n")
answer_3 = input("Respostas: ")

if answer_3 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Quando foi criado o primeiro celular da história? \n (A) 2000 \n (B) 1998 \n (C) 1985 \n (D) 1994\n")
answer_4 = input("Respostas: ")

if answer_4 == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual a resolução de uma imagem Full HD? \n (A) 1920x1080 \n (B) 1280x720 \n (C) 2560x1440 \n (D) 1720x220\n")
answer_5 = input("Respostas: ")

if answer_5 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Quantos bits cabem em um byte? \n (A) 1 bit \n (B) 25 bits \n (C) 8 bits \n (D) 12 bits\n")
answer_6 = input("Respostas: ")

if answer_6 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual das opções abaixo é um sistema operacional? \n (A) Microsoft Word \n (B) Linux \n (C) Google Chrome \n (D) Intel\n")
answer_7 = input("Respostas: ")

if answer_7 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("O que é um software? \n (A) Dispositivo físico do computador \n (B) Parte mecânica do computador \n (C) Conjunto de instruções que podem ser executadas por um computador \n (D) Um sistema de cabeamento\n")
answer_8 = input("Respostas: ")

if answer_8 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual dos seguintes é um navegador de internet? \n (A) Microsoft Word \n (B) Mozilla Firefox \n (C) Adobe Photoshop \n (D)Windows Midea Player\n")
answer_9 = input("Respostas: ")

if answer_9 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("O que é um arquivo PDF? \n (A) Umtipo de vírus de computador \n (B) Um formato de arquivo de imagem \n (C) Um software de edição de textos \n (D) Um formato de arquivo de documento portátil\n")
answer_10 = input("Respostas: ")

if answer_10 == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print(f"Quiz acabou... Pontuação: {score}/10")