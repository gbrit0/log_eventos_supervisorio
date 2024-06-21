import struct
import socket
import time

transactionId = 0
PROTOCOL_ID = 0
LENGHT = 6
unitId = 1
FUNCTION_CODE = 67
REGISTER_COUNT = 84

requisicoes = []

for startingAddress in range(500,650):
   requisicao = struct.pack(
      '>HHHBBHH',
      transactionId,
      PROTOCOL_ID,
      LENGHT,
      unitId,
      FUNCTION_CODE,
      startingAddress,
      REGISTER_COUNT
   )

   requisicoes.append(requisicao)
   transactionId += 1

ip = '10.10.82.11'
porta = 502

con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
con.connect((ip, porta))

try:
   for requisicao in requisicoes:
      con.send(requisicao)
      time.sleep(0.1)
      print(requisicao.hex())
      data = con.recv(1024)
      # time.sleep(0.1)
      with open('logEventos.csv', 'a', encoding='utf-8') as file:
         file.write(data.hex(sep=' ') + '\n')
      # time.sleep(0.1)
except KeyboardInterrupt:
   pass
finally:
   con.close()