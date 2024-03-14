#1: O valor de soma será 91
indice, soma, K = 13, 0, 0
while K < indice:
    K += 1
    soma += K
print(soma)

#2:
def fibo(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num
print('Está!' if fibo(int(input('Digite um número: '))) else 'Não está!')

#3: 9 || 128 || 49 || 100 || 13 || 200

#4: Primeiramente, eu acionaria um interruptor i1 e esperaria alguns minutos. Após isso, desacionaria e ativaria outro, i2, e iria a alguma sala. Se a lâmpada estiver acesa, já posso atribuíla a i2. Se não, verifico se está quente. Se sim, atribuo-a ao i1, se não, a i3. Depois, com a mesma configuração dos interruptores, eu iria a alguma outra sala e verificaria novamente. Se estiver acesa, atribuo a i2, se estiver apagada e quente, a i1 e se estiver apagada e fria, a i3. Fazendo isso com apenas duas salas, já consigo descobrir qual interruptor controla a última por eliminação.

#5:
def inverte(string):
    return string[::-1]
print(inverte('Olá Mundo!'))
