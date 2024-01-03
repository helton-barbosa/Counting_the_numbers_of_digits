aux = number = int(input('Entre com um número inteiro: '))
count = 0

while number != 0:
    number //= 10
    count += 1

print(f'O número {aux} tem {count} dígitos')
