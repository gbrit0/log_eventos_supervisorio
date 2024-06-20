import socket, struct

ip = '10.10.82.11'
porta = 502

# construir a requisição:
transactionId = 0
protocolId = 0
length = 6
unitId = 1
functionCode = 67
startingAddress = 500
registerCount = 84

requisicao = struct.pack(
   '>HHHBBHH', 
    transactionId, 
    protocolId, 
    length, 
    unitId, 
    functionCode, 
    startingAddress, 
    registerCount,
   )

# construir a conexão:
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((ip, porta))

socket.sendall(requisicao)

resposta = socket.recv(1024)

print(resposta.hex())

socket.close()