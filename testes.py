import unittest
from aluno import AlunoClass
from conexao import ConexaoClass
import mongomock  # Projeto: https://github.com/mongomock/mongomock


class alunoTest(unittest.TestCase):
    @mongomock.patch(servers=(('localhost.com', 27017),))
    def setUp(self):
        print('Teste', self._testMethodName, 'sendo executado...')
        
        # Configurações para os testes
        self.aluno = AlunoClass('Fabio', 'Teixeira', 10)
        self.conexao = ConexaoClass().conexaoMongoDB(url='localhost.com', banco='faculdade')

    def test_salvarAluno(self):
        # Salva o aluno na coleção 'alunos'
        resposta = self.aluno.salvar(conexao=self.conexao, colecao='alunos')
        self.assertEqual(True, resposta, 'Aluno não foi salvo corretamente!')

        # Verifica se o aluno foi salvo corretamente no MongoDB simulado
        saved_aluno = self.conexao['alunos'].find_one({'nome': 'Fabio'})
        self.assertIsNotNone(saved_aluno, 'Aluno não encontrado na coleção!')
        self.assertEqual(saved_aluno['nome'], 'Fabio', 'O nome do aluno salvo está incorreto!')
        self.assertEqual(saved_aluno['nota'], 10, 'A nota do aluno salvo está incorreta!')


if __name__ == "__main__":
    unittest.main()
