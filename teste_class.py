from user_class import Usuario
import pickle
import os
 
def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
 
 
list_of_users=[]
list_of_users.append(Usuario("joao", "senha1"))
list_of_users.append(Usuario("pedro","senha2"))
list_of_users.append(Usuario("mariana","senha3"))
list_of_users.append(Usuario("marta","senha4"))

save_object(list_of_users)

lista_de_usuarios=load_object("data.pickle")


sair=0

while(sair!=1):
    os.system("clear")
    opcao=input("Para realizar o login digite 'L', para criar um novo usuário digite 'N':")
    if (opcao=='N'):
        novo_usuario=Usuario()
        lista_de_usuarios.append(novo_usuario)
    elif (opcao=='L'):
        username=input("Digite o seu username: ")
        senha_digitada=input("Digite a sua senha: ")
        Usuario(username, senha_digitada,lista_de_usuarios)
    
    sair=int(input("Para sair do programa tecle 1, para testar outro usuario tecle 2: "))