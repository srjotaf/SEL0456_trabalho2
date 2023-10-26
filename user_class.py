class Usuario(object):
    def __init__(self, username, senha_digitada, lista_de_usuarios):
        if username is None:
            self._perguntas()
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
                self._perguntas(lista_de_usuarios)
            if (criar=='N'):
                pass            

        
    
    def _perguntas(self,lista_de_usuarios):
        username=input("Digite o username do novo usuario:")
        hash_senha=input("Digite a senha:")
        
        self._criar_novo(username, hash_senha)