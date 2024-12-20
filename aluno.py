class AlunoClass:
    def __init__(self, nome, sobrenome, nota):    
        self.nome = nome
        self.sobrenome = sobrenome
        self.nota = nota

    def mostrarAluno(self):
        return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota)

    def salvar(self, conexao, colecao):
        # Transforma o objeto Aluno em um dicionário
        mydict = self.__dict__
        
        # Insere o dicionário na coleção MongoDB
        x = conexao[colecao].insert_one(mydict)
        
        # Retorna True se o salvamento foi bem-sucedido
        return x.acknowledged
