from teste_sisbanco import *

def main():
    conta = TesteConta()
    conta.teste_saldo()
    conta.teste_creditar()
    conta.teste_debitar()

    conta_poupanca = TesteContaPoupanca()
    conta_poupanca.teste_juros()

    conta_especial = TesteContaEspecial()
    conta_especial.teste_bonus()
    conta_especial.teste_creditar()
    conta_especial.teste_rende_bonus()

    conta_imposto = TesteContaImposto()
    conta_imposto.teste_debitar()
    conta_imposto.teste_taxa()

    banco = TesteBanco()
    banco.teste_debitar()
    banco.teste_cadastrar()
    banco.teste_credito()
    banco.teste_rende_bonus()
    banco.teste_render_juros()
    banco.teste_saldo()
    banco.teste_taxa_imposto()
    banco.teste_taxa_poupanca()
    banco.teste_transferir()


main()