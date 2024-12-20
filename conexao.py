import pymongo;

class ConexaoClass:
  def conexaoMongoDB(self, url, banco):
    conexao = pymongo.MongoClient(url);
    bancodados = conexao[banco];    
    return bancodados;
