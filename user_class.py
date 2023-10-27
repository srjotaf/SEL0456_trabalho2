class Usuario(object):
    """ A classe Usuario tem como parâmetros username, senha_digitada, e lista_de_usuarios.
    Ela pode ser chamada de 3 maneiras:
    - sem nenhum parâmetro: para que seja exibido o prompt para receber dados para criar uma nova instância.
    - com username e senha_digitada, mas sem lista de usuarios: para criar uma nova instância da classe Usuario usando os parâmetros fornecidos.
    - com todos os 3 parâmetros: para realizar login.
    Apresenta como atributos: username, hash_senha, tipo_usuario (esse atributo pode assumir or valores 1("comum"), 2("gerente") e 3("adm"), em grau crescente
    de permissões).
    Args:
        username (string): Ao criar Será um atributo. O atributo username deverá ser uma sequência única de caracteres 
        iniciada por uma letra, o username também pode conter números e underscores.
        senha_digitada(string): O parâmetro senha_digitada será usada pelo método _hash para gerar o atributo
        hash_senha ou para realizar o login.
        lista_de_usuarios(list): Quando usado na chamada da classe Usuario, será a lista na se buscará os usuários que podem ser acessados.
    """
    def __init__(self, username=None, senha_digitada=None, lista_de_usuarios=None):
        if (username is None) and (senha_digitada is None):
            self.prompt()
        elif lista_de_usuarios is None:
            self._criar_novo(username, senha_digitada)
        else:
            self._acessar_usuario(username, senha_digitada, lista_de_usuarios)

    def prompt(self):
        """Exibe na tela os pedidos por um novo username e uma nova senha. E em seguida chama o método _criar_novo.
        """
        username=input("Digite o username do novo usuario: ")
        hash_senha=input("Digite a senha: ")
        
        self._criar_novo(username, hash_senha)

    def _criar_novo(self,username, hash_senha,tipo="comum"):
        """Faz a atribuição de valores para os atributos de uma nova instância da classe.
        Retorna uma instância da classe Usuario.

        Args:
            username (string): A sequência de caracteres que define um usuario
            hash_senha (string): A codificação da senha que é armazenada na classe.
            tipo (string): O tipo de usuario. Pode assumir os valores "comum", "gerente", "adm", listados em ordem crescente de permissões.

        Returns:
            Usuario: Uma nova instância da classe Usuario. 
        """
        self.username=username
        self.hash_senha=hash_senha
        self.tipo=1
        return self
        
    def _acessar_usuario(self, username_digitado, senha_digitada, lista_de_usuarios):
        """Realiza uma busca na lista lista_de_usuarios, pelo objeto Usuario com o username igual a usernamen_digitado.
        Se encontrá-lo faz a verificação da senha. Se não encontrá-lo retorna uma mensagem de erro.

        Args:
            username_digitado (string): É o username que se quer acessar. Pode conter letras, números e underscores. Deve começar com uma letra.
            senha_digitada (string): É a senha que o usuário digita para realizar o login.
            lista_de_usuarios (string): É a lista em que se buscará o Usuario.
        """
        for i in lista_de_usuarios:
            if (username_digitado==i.username):
                if (senha_digitada==i.hash_senha):
                    print("Acesso permitido ao usuario {}. Com atribuição do tipo {}".format(username_digitado,i.tipo))
                    return self
                else:
                    print("Senha errada.")
                    return -1
        print("O usuario digitado nao existe no banco de dados.")

    def alterar_tipo(self, username, tipo, lista_de_usuarios):
        """Altera o tipo de um outro usuario. Um usuario somente pode ter seu nivel alterado por um outro usuario de nível
        maior. Um usuario somente alterar as permissoes usuarios de nível inferior ou igual ao seu. 

        Args:
            username (string): O Usuario cuja permissao será alterada.
            tipo (string): O novo tipo de usuario para o usuário que está sendo alterado. 
            lista_de_usuarios (list): A lista em que se buscará o usuario a ser alterado.
        """
        
        match tipo:
            case "comum":
                novo_tipo=1
            case "gerente":
                novo_tipo=2
            case "adm":
                novo_tipo=3
            case _:
                print("Esse tipo de usuário não existe")
                return -1
                
        if novo_tipo>self.tipo: 
            print("Você não tem permissao de realizar essa alteração.")
    
        for i in lista_de_usuarios:
            if(username==i.username):
                if (self.tipo>=i.tipo):
                    print("O usuario {} esta tendo a sua permissao alterada de nível {} para nivel {}".format(i.username, i.tipo, novo_tipo))
                    i.tipo=novo_tipo
                else:
                    print("Você não tem permissao de realizar essa alteração.")
                
        