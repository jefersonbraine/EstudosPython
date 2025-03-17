# Paradigma de programação
# Classes e Objetos
#atributos e métodos

class Veiculo:
    def movimentar(self):
        #método
        print(f'Sou um veiculo e me desloco!')

    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
        self.num_registro = None
        


if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade' )
    meu_veiculo.movimentar()
    #acessar valores internos
    print(meu_veiculo.fabricante)


#atributo privado

class Veiculo:
    def movimentar(self):
        #método
        print(f'Sou um veiculo e me desloco!')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None


    #* Setter: É um método que permite gravar um dado dentro de um elemento dentro da classe/objeto
    def set_num_registro(self, registro):
        self.__num_registro = registro

    #* Getter: (Um método especial que permite acessar os atributos dentro da classe ou acessar outros elementos dentro da classe)
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante} \n')
        
    def get_num_registro(self):
        return self.__num_registro


if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade' )
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro('127849490-0900.15')
    print(f'Registro: {meu_veiculo.get_num_registro()}\n')


# Herança

class Veiculo:
    def movimentar(self):
        #método
        print(f'Sou um veiculo e me desloco!')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None


    def set_num_registro(self, registro):
        self.__num_registro = registro

    
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante} \n')
        
    def get_num_registro(self):
        return self.__num_registro


class Carro(Veiculo):
    #Método __init__ será herdado
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas!')\
        
class Motocicleta(Veiculo):
    def movimentar(self): #Polimorfismo
        print(f'Corro muito!')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)

    def get_categoria(self):
        return self.__cat
    
    def movimentar(self):
        print(f'Eu voo alto!')


if __name__ == '__main__':
    # meu_veiculo = Veiculo('GM', 'Cadillac Escalade' )
    # meu_veiculo.movimentar()
    # meu_veiculo.get_fabr_modelo()
    # meu_veiculo.set_num_registro('127849490-0900.15')
    # print(f'Registro: {meu_veiculo.get_num_registro()}\n')

    # meu_carro = Carro('Volkswagen', 'Polo')
    # meu_carro.movimentar()
    # meu_carro.get_fabr_modelo()

    # seu_carro = Carro('Audi', 'A7 Sportback')
    # seu_carro.movimentar()
    # seu_carro.get_fabr_modelo()

    # moto = Motocicleta('Harley-Davidson', 'Nigthster Special')
    # moto.movimentar()
    # moto.get_fabr_modelo()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'Categoria: {meu_aviao.get_categoria()}')