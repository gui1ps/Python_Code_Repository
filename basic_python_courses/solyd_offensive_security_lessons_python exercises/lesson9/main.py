from clientes import Cliente
from contas import conta

c1=Cliente('1236456789',18,'Guilherme')
conta1=conta(c1,18000,200)

print('CLIENTE: ',conta1.cliente)
print('SALDO: ',conta1.saldo)

conta1.sacar(18200)

print('SALDO: ',conta1.saldo)
conta1.sacar(18200)
print('SALDO: ',conta1.saldo)