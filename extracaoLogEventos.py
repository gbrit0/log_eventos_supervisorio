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

for startingAddress in range(0,13):
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
      # print(requisicao.hex())
      data = con.recv(1024)
      # time.sleep(0.1)
      # with open('logEventos.csv', 'a', encoding='utf-8') as file:
      #    file.write(data.hex(sep=' ') + '\n')
      # time.sleep(0.1)
      # print(data.hex())
         
      
      data = struct.unpack(
         """>3H83B29H30B""",
         # ">HH6sHBBHHHHHHHIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIBBBBBBBBBBBBB",
         data
      )
      # print(data)
      text = [chr(x) for x in data[6:86] if x != 0]

      # Juntar a lista de caracteres em uma string
      text = ''.join(text)

      # Dividir a string no caractere '\xa0' e selecionar a parte antes do primeiro '\xa0'
      text = text.split('\xa0')[0]

      
      
      dados = {
         "transactionId": data[0],
         "protocolId": data [1],
         "unitId": data[3],
         "functionCode": data[4],
         "byteCount": data[5],
         "text": text,
         "year": data[86],
         "month": data[87],
         "day": data[88],
         "hour": data[89],
         "minute": data[90],
         "second": data[91],
         "channel": data[92],
         "ppower": data[93],
         "qpower": data[94],
         "pf": data[95],
         "genU1": data[96],
         "genU2": data[97],
         "genU3": data[98],
         "genI1": data[99],
         "genI2": data[100],
         "genI3": data[101],
         "genF": data[102],
         "busU1": data[103],
         "busU2": data[104],
         "busU3": data[105],
         "busF": data[106],
         "df/dt": data[107],
         "vector": data[108],
         "multiInput46": data[109],
         "multiInput47": data[110],
         "multiInput48": data[111],
         "tacho": data[112],
         "alarmValue": data[113]
      }
      print(dados)
      # print(data.decode(encoding='latin-1'))
except KeyboardInterrupt:
   pass
finally:
   con.close()
