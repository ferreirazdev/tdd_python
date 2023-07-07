def test_cliente_cadastrado_com_sucesso():
    cliente = Cliente()
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cadastrado com Sucesso" == resposta
