import unittest
from aluno import AlunoClass
from turma import TurmaClass
from conexao import ConexaoClass
import mongomock  # Projeto: https://github.com/mongomock/mongomock

class alunoTest(unittest.TestCase):
    @mongomock.patch(servers=(('localhost.com', 27017),))
    def setUp(self):
        print('Teste', self._testMethodName, 'sendo executado...')
        self.aluno = AlunoClass('Fabio', 'Teixeira', 10)
        self.turma = TurmaClass()
        self.turma.cadastrarAlunos([self.aluno])
        self.conexao = ConexaoClass().conexaoMongoDB(url='localhost.com', banco='faculdade')

    def test_salvarAluno(self):
        # Salva o aluno na coleção 'alunos'
        resposta = self.aluno.salvar(conexao=self.conexao, colecao='alunos')
        self.assertEqual(True, resposta, 'Aluno não foi salvo corretamente!')

        # Verifica se o aluno foi salvo corretamente
        saved_aluno = self.conexao['alunos'].find_one({'nome': 'Fabio'})
        self.assertIsNotNone(saved_aluno, 'Aluno não encontrado na coleção!')
        self.assertEqual(saved_aluno['nome'], 'Fabio', 'O nome do aluno salvo está incorreto!')
        self.assertEqual(saved_aluno['nota'], 10, 'A nota do aluno salvo está incorreta!')

    def test_salvarTurma(self):
        # Salva a turma na coleção 'turma'
        resposta = self.turma.salvar(conexao=self.conexao, colecao='turma')
        self.assertEqual(True, resposta, 'Turma cadastrada incorretamente!')

        # Verifica se a turma foi salva corretamente
        saved_turma = self.conexao['turma'].find_one()
        self.assertIsNotNone(saved_turma, 'Turma não encontrada na coleção!')
        self.assertEqual(len(saved_turma['turma']), 1, 'A turma salva tem número incorreto de alunos!')
        self.assertEqual(saved_turma['turma'][0]['nome'], 'Fabio', 'O nome do aluno na turma salva está incorreto!')

if __name__ == "__main__":
    unittest.main()
