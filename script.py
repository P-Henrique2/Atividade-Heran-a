class Empregado:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

class Gerente(Empregado):
    def __init__(self, nome, salario_base, bonus_fixo):
        super().__init__(nome, salario_base)
        self.bonus_fixo = bonus_fixo

    def calcular_salario(self):
        return self.salario_base + self.bonus_fixo


class Vendedor(Empregado):
    def __init__(self, nome, salario_base, comissao, vendas):
        super().__init__(nome, salario_base)
        self.comissao = comissao  
        self.vendas = vendas  

    def calcular_salario(self):
       
        return self.salario_base + (self.comissao * self.vendas)

if __name__ == "__main__":

    gerente = Gerente("Alice", 5000, 2000)  
    print(f"O salário total do gerente {gerente.nome} é: R${gerente.calcular_salario()}")

    vendedor = Vendedor("João", 3000, 0.05, 20000) 
    print(f"O salário total do vendedor {vendedor.nome} é: R${vendedor.calcular_salario()}")
