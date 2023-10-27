class Usuario(object):
    def __init__(self, username=None, senha_digitada=None, lista_de_usuarios=None):
        if (username is None) and (senha_digitada is None):
            self.prompt()
        elif lista_de_usuarios is None:
            self.criar_novo(username, senha_digitada)
        else:
            self._acessar_usuario(username, senha_digitada, lista_de_usuarios)


    def criar_novo(self,username, hash_senha):
        self.username=username
        self.hash_senha=hash_senha
        return self
        
    def _acessar_usuario(self, username, senha_digitada, lista_de_usuarios):
        for i in lista_de_usuarios:
            if (username==i.username):
                if (senha_digitada==i.hash_senha):
                    print("Acesso permitido ao usuario {}.".format(username))
                    return self
                else:
                    print("Senha errada.")
                    return -1
        print("O usuario digitado nao existe no banco de dados.")
            
            
    def prompt(self):
        username=input("Digite o username do novo usuario: ")
        hash_senha=input("Digite a senha: ")
        
        self.criar_novo(username, hash_senha)

