import socket
import struct
import pymodbus

# Parâmetros de conexão
ip = "10.10.82.11"
porta = 502
slave_id = 1
starting_address = 0
quantity = 10

transactionId = 0
protocolId = 0
length = 6
unitId = 1
functionCode = 43
starting_address = 500
registerCount = 84


# Criação da requisição Modbus
# pdu_request = struct.pack('>HHHHHHH', 
#                           transactionId, 
#                           protocolId, 
#                           length, 
#                           unitId, 
#                           functionCode, 
#                           starting_address, 
#                           registerCount)
pdu_request = ( b"\x00\x00\x00\x00\x00\x06\x01\x43\x01\xf4\x00\x54")

# pdu_request = "061600000006014301f40054"
print(pdu_request)


# Criação do socket TCP
try:
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.connect((ip, porta))

   sock.sendall(pdu_request)

   # ... (código de comunicação Modbus)

   pdu_response = sock.recv(1024)

   # Extração do código de retorno
   code = pdu_response[0]

   if code != 0:
      # Verifique o código de retorno e lance uma exceção personalizada ou tome outras medidas
      if code == 1:
         print("Erro de função Modbus")
      elif code == 2:
         print("Endereço de dados ilegal")
      else:
         print(f"Código de retorno Modbus desconhecido: {code}")

   # Decodificação da resposta Modbus
   data = pdu_response[7:]
   coils = []
   for i in range(quantity):
       coils.append(data[i] & 1)

   # Impressão dos valores dos coils
   print("Valores dos coils:")
   for coil in coils:
       print(coil)

except socket.error as err:
   print(f"Erro de socket: {err}")
except socket.gaierror as err:
   print(f"Erro de resolução de nome: {err}")
except socket.timeout as err:
   print(f"Tempo limite de conexão: {err}")


# Fechamento do socket
sock.close()