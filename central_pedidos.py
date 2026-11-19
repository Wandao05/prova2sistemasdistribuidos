
import threading
import time

# Servidores
principal = {
    "online": True,
    "estoque": 10
}

replica = {
    "online": True,
    "estoque": 10
}

# Controle de concorrencia
MAXIMO_SIMULTANEO = 3

semaforo = threading.Semaphore(MAXIMO_SIMULTANEO)
trava = threading.Lock()

pedidos_confirmados = []


# Processamento dos pedidos
def processar_pedido(numero):
    with semaforo:
        time.sleep(0.1)

        with trava:
            if principal["online"] and principal["estoque"] > 0:

                principal["estoque"] -= 1

                # Atualizar replica apos cada pedido
                replica["estoque"] = principal["estoque"]

                pedidos_confirmados.append(numero)


# Sincronizacao dos servidores
def sincronizar():
    with trava:
        if principal["online"] and replica["online"]:
            replica["estoque"] = principal["estoque"]


# Consulta de estoque
def consultar_estoque():

    with trava:

        # Consultar primeiro o servidor principal
        if principal["online"]:
            return (
                "PRINCIPAL",
                principal["estoque"]
            )

        # Se o principal estiver offline,
        # consultar automaticamente a replica
        elif replica["online"]:
            return (
                "REPLICA",
                replica["estoque"]
            )

        # Se os dois servidores estiverem offline
        else:
            return (
                "INDISPONIVEL",
                None
            )


# Inicio do sistema
print("=== CENTRAL DE PEDIDOS ===")

print(
    "Limite simultaneo:",
    MAXIMO_SIMULTANEO
)

print(
    "Estoque inicial principal:",
    principal["estoque"]
)

print(
    "Estoque inicial replica:",
    replica["estoque"]
)


# Criar tres pedidos
trabalhadores = [
    threading.Thread(
        target=processar_pedido,
        args=(numero,)
    )
    for numero in [101, 102, 103]
]


# Iniciar os pedidos
for trabalhador in trabalhadores:
    trabalhador.start()


# Esperar os pedidos terminarem
for trabalhador in trabalhadores:
    trabalhador.join()


# Mostrar pedidos confirmados
print(
    "Pedidos confirmados:",
    sorted(pedidos_confirmados)
)


# Mostrar estoque dos servidores
print(
    "Estoque principal:",
    principal["estoque"]
)

print(
    "Estoque replica:",
    replica["estoque"]
)


# Sincronizar os estoques
sincronizar()

print(
    "Replica apos sincronizacao:",
    replica["estoque"]
)


# Simulacao de falha do servidor principal
print("\n=== SIMULACAO DE FALHA ===")

principal["online"] = False

print("Servidor principal: OFFLINE")
print("Servidor replica:", "ONLINE" if replica["online"] else "OFFLINE")


# Consultar estoque apos a falha
nome, estoque = consultar_estoque()

print(
    "Consulta apos a falha:",
    nome,
    estoque
)
