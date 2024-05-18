import random

def calcular_nivel(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif 10 <= saldo_vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= saldo_vitorias <= 50:
        nivel = "Prata"
    elif 51 <= saldo_vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= saldo_vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= saldo_vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo_vitorias, nivel

vitorias = random.randint(0,150)
derrotas = random.randint(0,vitorias)

saldo,nivel = calcular_nivel(vitorias,derrotas)
print(f"O Herói tem saldo de {saldo} vitórias e está no nível de {nivel}")