from testes import Usuario
import pickle
 
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

for i in lista_de_usuarios:
    print(i.username)
