import sqlite3 #banco

class Ecommerce:
    def _init_(self, db='db.sqlite3'):
        self.conn = sqlite3.connect(db)
        self.menu()

    def menu(self):
         while True:
            print('\n'
                '[1]-Create\n'
                '[2]-Read\n'
                '[3]-Update\n'
                '[4]-Delete\n'
                '[5]-Exit\n\n'
                )  
            op = input('Escolha uma opção: ')

            match op:
                case '1':
                    print('Create')
                case '2':
                    print('Read')
                case '3':
                    print('Update')
                case '4':
                    print('Delete')
                case '5':
                    print('Exit')
                    break
                case _:
                    print('Escolha uma opção correta.')
    def create(self,
               tituloProduto,preco,descricao,imagemProduto,categoriaProduto,classificacaoProduto,exibirHome=True
               ):
        pass
home = Ecommerce()