class Usuario(object):
    def __init__(self, username=None, senha_digitada=None, lista_de_usuarios=None):
        if lista_de_usuarios is None:
            self._criar_novo(username, senha_digitada)
        else:
            self._acessar_usuario(username, senha_digitada, lista_de_usuarios)


    def _criar_novo(self,username, hash_senha):
        self.username=username
        self.hash_senha=hash_senha
        


    def _acessar_usuario(self, username, senha_digitada, lista_de_usuarios):
        for i in lista_de_usuarios:
            if (username==i.username):
                if (senha_digitada==i.hash_senha):
                    print("Acesso permitido ao usuario {}.".format(username))
                    break
                else:
                    print("Senha errada.")
                    break
            criar=input("O usuario digitado nao existe no banco de dados. Deseja criar um novo usuario? S/N")
            if (criar=='S'):
                self._perguntas()
            if (criar=='N'):
                pass            

        
    
    def _perguntas(self):
        username=input("Digite o username do novo usuario:")
        hash_senha=input("Digite a senha:")
        
        self._criar_novo(username, hash_senha)

