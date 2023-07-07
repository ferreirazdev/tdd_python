class CadastroCliente:
    def __init__(self):
        self.clientes_cadastrados = []

    def cadastrar_cliente(self, cliente):
        if cliente.idade < 18:
            return "Cliente menor de idade"
        
        if "@" not in cliente.email:
            return "Email invalido"
        
        if len(cliente.nome) < 3:
            return "Nome invalido"
        
        self.clientes_cadastrados.append(cliente)
        
        if len(self.clientes_cadastrados) > 0:
            return "Cadastrado com sucesso"

