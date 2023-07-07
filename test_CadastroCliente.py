from Cliente import Cliente
from CadastriCliente import CadastroCliente


def test_cliente_cadastrado_com_sucesso():
    cliente = Cliente("Flavio", 21, "flavio@gmail.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cadastrado com sucesso" == resposta
    

def test_cliente_maior_de_idade():
    cliente = Cliente("Flavio", 17, "flavio@gmail.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cliente menor de idade" == resposta
    

def test_email_valido():
    cliente = Cliente("Flavio", 21, "flaviogmail.com")
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Email invalido" == resposta
