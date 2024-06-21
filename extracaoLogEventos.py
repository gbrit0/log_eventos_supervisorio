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

for startingAddress in range(0,1):
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
      # with open('logEventos.csv', 'a', encoding='utf-8') as file:
      #    file.write(data.hex(sep=' ') + '\n')
      # time.sleep(0.1)
      print(data.hex())
         
      
      data = struct.unpack(
         """>3H4B12c67B1H20B3H6B5H44B""",
         # ">HH6sHBBHHHHHHHIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIBBBBBBBBBBBBB",
         data
      )
      print(data)
      
      dados = {
         "transactionId": data[0],
         "protocolId": data [1],
         "unitId": data[3],
         "functionCode": data[4],
         "byteCount": data[5],
         "year": data[86],
         "month": data[88],
         "day": data[90],
         "hour": data[92],
         "minute": data[94],
         "second": data[96],
         "channel": data[98],
         "ppower": data[100],
         "qpower": data[102],
         "pf": data[104],
         "genU1": data[106],
         "genU2": data[108],
         "genU3": data[110],
         "genI1": data[112],
         "genI2": data[114],
         "genI3": data[116],
         "genF": data[118],
         "busU1": data[119],
         "busU2": data[120],
         "busU3": data[121],
         "busF": data[122],
         "df/dt": data[124],
         "vector": data[126],
         "multiInput46": data[128],
         "multiInput47": data[130],
         "multiInput48": data[132],
         "tacho": data[134],
         "alarmValue": data[136]
      }
      print(dados)
      # print(data.decode(encoding='latin-1'))
except KeyboardInterrupt:
   pass
finally:
   con.close()
