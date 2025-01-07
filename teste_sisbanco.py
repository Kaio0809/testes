import unittest
from sisbanco import *

class TesteConta(unittest.TestCase):
    def teste_saldo(self):
        conta = Conta("123")
        self.assertEqual(conta.get_saldo(), 0.0)

    def teste_creditar(self):
        conta = Conta("123")
        conta.creditar(10)
        self.assertEqual(conta.get_saldo(), 10.0)

    def teste_debitar(self):
        conta = Conta("123")
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), -5.0)
        conta.creditar(10)
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), 0.0)

class TesteContaPoupanca(unittest.TestCase):
    def teste_juros(self):
        conta = ContaPoupanca('123')
        conta.creditar(10)
        conta.render_juros(0.1)
        self.assertEqual(conta.get_saldo(), 11)

class TesteContaEspecial(unittest.TestCase):
    def teste_bonus(self):
        conta = ContaEspecial("123")
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 0.0)
    
    def teste_rende_bonus(self):
        conta = ContaEspecial("123")
        conta.creditar(10)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 10,1)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 10,1)
    
    def teste_creditar(self):
        conta = ContaEspecial("123")
        conta.creditar(100)
        self.assertEqual(conta.get_saldo(), 100)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 101)
    

class TesteContaImposto(unittest.TestCase):
    def teste_taxa(self):
        conta = ContaImposto("123")
        self.assertEqual(conta.get_taxa(), 0.001)
        conta.set_taxa(0.1)
        self.assertEqual(conta.get_taxa(), 0.1)
    
    def teste_debitar(self):
        conta = ContaImposto("123")
        conta.creditar(10)
        conta.debitar(1)
        self.assertEqual(conta.get_saldo(), 8.999)
    
class TesteBanco(unittest.TestCase):
    def teste_cadastrar(self):
        banco = Banco()
        conta = Conta("123")
        banco.cadastrar(conta)
        self.assertEqual(banco.procurar("123"), conta)
        contaI = ContaImposto("234")
        banco.cadastrar(contaI)
        self.assertEqual(contaI.get_taxa(), 0.001)


    def teste_credito(self):
        banco = Banco()
        conta = Conta("123")
        banco.cadastrar(conta)
        banco.creditar("123",20)
        self.assertEqual(conta.get_saldo(), 20)

    def teste_debitar(self):
        banco = Banco()
        conta = Conta("123")
        banco.cadastrar(conta)
        banco.debitar("123", 20)
        self.assertEqual(conta.get_saldo(), -20)
    
    def teste_saldo(self):
        banco = Banco()
        conta = Conta("123")
        banco.cadastrar(conta)
        banco.creditar("123", 100)
        self.assertEqual(banco.saldo("123"), conta.get_saldo())
    
