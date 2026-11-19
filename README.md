#P2 - SISTEMAS DISTRIBUIDOS

ALUNO: Wanderley Goncalves junior
PROFESSORA SIMONE TATIANE DO CANTO
DATA: 18/11/2026

1. SITUAÇÃO-PROBLEMA
Apenas 2 pontos funcionavam ao invés dos 3.
Após o processamento do estoque a réplica não alterava o valor.

2 primeira execução
Apenas 2 pedidos eram aceitos ao invés dos 3.


##. evidencia 1 - primeira execução
![evidencai 1] (evidencias/evidencia1.png


## 3. problema A - concorrencia

Qual problema foi identificado?

 Antes, a réplica copiava o próprio estoque, ou seja, não recebia nenhuma atualização. Foi alterado para copiar o estoque do servidor principal para a réplica. Também foi utilizado o Lock para proteger o acesso durante a sincronização.


 evidencia 2 - concorrencia
!{[evidencia2]

## 4 PROBLEMA B REPLICAÇÃO E CONSISTENCIA

QUAL PROBLEMA FOI IDENTIFICADO? 

Antes, o programa verificava novamente se o servidor principal estava online, em vez de verificar a disponibilidade da réplica. Com a alteração, quando o servidor principal falhar, o sistema verifica se a réplica está online e utiliza seu estoque para continuar realizando consultas.


evidencia 3 - sincronização

1[evdiencia3] 

## 5 problema C

Essa parte já estava correta no código original. O semáforo permite limitar a quantidade de execuções simultâneas a três, enquanto as threads permitem processar os três pedidos de forma concorrente.


