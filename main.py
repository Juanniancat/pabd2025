## Programação com Acesso a Banco de Dados
# Revisão de Orientação a Objetos
# Prof. Guilherme Leal Santos

from empresa.config.database import SupabaseConnection
from empresa.dao.funcionario_dao import FuncionarioDAO
from empresa.dao.departamento_dao import DepartamentoDAO
from empresa.models.funcionario import Funcionario
from empresa.models.departamento import Departamento
from datetime import date

client = SupabaseConnection().client

# Criando DAOs para acessar as tabelas
funcionario_dao = FuncionarioDAO(client)
departamento_dao = DepartamentoDAO(client)

print("=" * 80)
print("CRUD - FUNCIONÁRIO")
print("=" * 80)

# ===== READ ALL - FUNCIONÁRIO =====
print("\n--- READ ALL (Funcionários) ---")
for funcionario in funcionario_dao.read_all():
    print(funcionario)

# ===== READ - FUNCIONÁRIO =====
print("\n--- READ (Funcionário específico) ---")
f = funcionario_dao.read('cpf', '11122233344')
print(f)

# ===== CREATE - FUNCIONÁRIO =====
print("\n--- CREATE (Novo Funcionário) ---")
novo_funcionario = Funcionario(
    _cpf='99988877766',
    _pnome='João',
    _unome='Silva',
    _data_nasc=date(1995, 8, 15),
    _endereco='Natal-RN',
    _salario=5500.00,
    _sexo='m',
    _cpf_supervisor='55566677788',
    _numero_departamento=101
)
funcionario_criado = funcionario_dao.create(novo_funcionario)
print(f"Funcionário criado: {funcionario_criado}")

# ===== UPDATE - FUNCIONÁRIO =====
print("\n--- UPDATE (Atualizar Funcionário) ---")
funcionario_atualizado = Funcionario(
    _cpf='99988877766',
    _pnome='João',
    _unome='Santos',
    _data_nasc=date(1995, 8, 15),
    _endereco='Parnamirim-RN',
    _salario=6000.00,
    _sexo='m',
    _cpf_supervisor='55566677788',
    _numero_departamento=102
)
sucesso = funcionario_dao.update('cpf', '99988877766', funcionario_atualizado)
print(f"Atualização bem-sucedida: {sucesso}")

# ===== DELETE - FUNCIONÁRIO =====
print("\n--- DELETE (Deletar Funcionário) ---")
sucesso = funcionario_dao.delete('cpf', '99988877766')
print(f"Deleção bem-sucedida: {sucesso}")

print("\n" + "=" * 80)
print("CRUD - DEPARTAMENTO")
print("=" * 80)

# ===== READ ALL - DEPARTAMENTO =====
print("\n--- READ ALL (Departamentos) ---")
for departamento in departamento_dao.read_all():
    print(departamento)

# ===== READ - DEPARTAMENTO =====
print("\n--- READ (Departamento específico) ---")
d = departamento_dao.read('numero', 101)
print(d)

# ===== CREATE - DEPARTAMENTO =====
print("\n--- CREATE (Novo Departamento) ---")
novo_departamento = Departamento(
    _numero=999,
    _nome='Desenvolvimento',
    _cpf_gerente='55566677788'
)
departamento_criado = departamento_dao.create(novo_departamento)
print(f"Departamento criado: {departamento_criado}")

# ===== UPDATE - DEPARTAMENTO =====
print("\n--- UPDATE (Atualizar Departamento) ---")
departamento_atualizado = Departamento(
    _numero=999,
    _nome='Desenvolvimento e Inovação',
    _cpf_gerente='55566677788'
)
sucesso = departamento_dao.update('numero', 999, departamento_atualizado)
print(f"Atualização bem-sucedida: {sucesso}")

# ===== DELETE - DEPARTAMENTO =====
print("\n--- DELETE (Deletar Departamento) ---")
sucesso = departamento_dao.delete('numero', 999)
print(f"Deleção bem-sucedida: {sucesso}")

print("\n" + "=" * 80)
print("FIM DA DEMONSTRAÇÃO CRUD")
print("=" * 80)

"""
from conta import Conta
from cliente import Cliente
from empresa.config.database import SupabaseConnection
from funcionario.controle_de_bonificacoes import ControleDeBonificacoes
# from funcionario.funcionario import Funcionario
from funcionario.gerente import Gerente
from ifrn.pessoa import Pessoa
from ifrn.funcionario import Funcionario

# Aula 17/10 - Polimorfismo, Classes Abstratas, Supabase

client = SupabaseConnection().client

# pessoa = Pessoa('Guilherme', '111.222.333-44')
# print(pessoa)

# f = Funcionario('Guilherme', '111.222.333-44', '1886519')
# print(f)

# f = Funcionario('Bartô Galeno', '111.222.333-44', 50000)
# print(f.get_bonificacao())
# print(f)
# g = Gerente('Reginaldo Rossi', '777.222.333-88', 250000, 1234, 10)
# print(g.get_bonificacao())
# print(g)

# controle = ControleDeBonificacoes()
# controle.registra(f)
# controle.registra(g)
# print(f'Total = R$ {controle.total:.2f}')

# cliente1 = Cliente("Elvis Presley", "111.222.333-44")
# controle.registra(cliente1)



# Aula 10/10 - Métodos estáticos, métodos de classe
# Herança e Reescrita de métodos

f = Funcionario('Bartô Galeno', '111.222.333-44', 50000)
print(f.get_bonificacao())
print(f)
g = Gerente('Reginaldo Rossi', '777.222.333-88', 250000, 1234, 10)
print(g.get_bonificacao())
print(g)

#  cliente1 = Cliente("Elvis Presley", "111.222.333-44")
# conta1 = Conta(cliente1, 1, 123, "elvis@gmail.com", 10000)
# print(Conta.total_contas())
# cliente2 = Cliente("Jonhny Cage", "222.333.444-55")
# conta2 = Conta(cliente2, 2, 234, "jonhnny@outlook.com", 5000)
# print(Conta.total_contas())

# print(Conta.lista_contas()[0].saldo)
# print(Conta.lista_contas()[1].saldo)

# print(Conta.get_saldo_total())

# print(Conta.total_contas_cm())


# Aula 26/09 - Agregação, Composição, Modificadores de Acesso
cliente1 = Cliente("Elvis Presley", "111.222.333-44")
conta1 = Conta(cliente1, 1, 123, "elvis@gmail.com", 10000)
conta1.extrato()
conta1.saca(500)
conta1.deposita(300)

cliente2 = Cliente("Jonhny Cage", "222.333.444-55")
conta2 = Conta(cliente2, 2, 234, "jonhnny@outlook.com", 5000)
conta2.extrato()
conta2.saca(100)
conta2.deposita(600)

conta1.transfere(conta2, 2000)
conta2.saca(10000)

conta1.historico.imprime()
conta2.historico.imprime()

# sem decorator
conta1.set_saldo(-100)
print(conta1.get_saldo()) #getter
print(conta1.get_saldo()*1.1 + conta2.get_saldo()*0.9)

# com decorator
conta1.saldo = -100
print(conta1.saldo) #getter
print(conta1.saldo*1.1 + conta2.saldo*0.9)

# Aula 19/09 - Orientação a Objetos


cliente1 = Cliente('Elvis Presley', '111.222.333-44')
conta1 = Conta(cliente1, 1, 123, 'elvis@gmail.com', 12345678)
conta1.extrato()
# conta1.deposita(100)
# conta1.extrato()

# conta2 = conta1
# conta2.extrato()
# conta2.saca(100)
# conta2.extrato()
# conta1.extrato()

# if(conta1.saca(1000)):
#     print('OK')
# else:
#     print('Tá Liso')

cliente2 = Cliente('Jonhny Cage', '222.333.444-55')
conta2 = Conta(cliente2, 2, 234, 'jonhnny@outlook.com', 234567)
conta2.extrato()

if(conta2.transfere(conta1, 1000)):
    print('OK')
else:
    print('Tá liso')

"""

"""
# Aula 12/092023 - Listas e Funções Lambda
frutas = ['Maçã', 'Banana', 'Laranja']
print(frutas)
print(frutas[0])
print(f'Tamanho: {len(frutas)}')

frutas.append('Uva')
print(frutas)

frutas.insert(0, 'Abacaxi')
print(frutas)

# -> Remove último elemento da lista
# fruta = frutas.pop() 
# -> Remove elemento do índice 0
# fruta = frutas.pop(0)
frutas.remove('Laranja')
# print(f'Removido: {fruta}')
print(frutas)

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numeros)

# Ordenar - crescente
numeros_ord_c = sorted(numeros)
print(f'Lista ordenada (c): {numeros_ord_c}')

# Ordenar - decrescente
numeros_ord_d = sorted(numeros, reverse=True)
print(f'Lista ordenada (d): {numeros_ord_d}')

# numeros_dobrados = []
# for n in numeros:
#     numeros_dobrados.append(n*2)
numeros_dobrados = list(map(lambda n: n*2, numeros))
print(numeros_dobrados)

# numeros_filtrados = []
# for n in numeros:
#     if n > 4:
#         numeros_filtrados.append(n)
numeros_filtrados = list(filter(lambda n: n > 4, numeros))
print(numeros_filtrados)

soma = 0
for n in numeros:
    soma += n
print(soma)

from functools import reduce

soma = reduce(lambda soma, n: soma + n, numeros)
print(soma)
"""