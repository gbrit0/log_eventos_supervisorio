import struct

transactionId = 0
protocolId = 0
length = 6
unitId = 1
functionCode = 67
starting_address = 500
registerCount = 84


request = struct.pack('>HHHBBHH', 
    transactionId, 
    protocolId, 
    length, 
    unitId, 
    functionCode, 
    starting_address, 
    registerCount)

print(request.hex())    # 00 00 00 00 00 06 01 43 01 f4 00 54