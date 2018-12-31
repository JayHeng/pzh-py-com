import sys, os
import binascii
import string

# usage:
#   charToHex():
#     in:  'abcdefg'
#     out: '61 62 63 64 65 66 67'
#
#   hexToChar():
#     in:  '31 32 33 34 35 36 37'
#     out: '1234567'

class formatter(object):

    def __init__(self):
        pass

    def charToHex( self, charStr ):
        hexStr = binascii.hexlify(charStr)
        result = ''
        for i in range(len(hexStr)):
            result += hexStr[i]
            if (i != 0) and (i % 2):
                result += ' '

        return result

    def hexToChar( self, hexStr ):
        status = True
        result = ''
        for i in range(len(hexStr)):
            if ((i + 1) % 3) == 0:
                if hexStr[i] != ' ':
                    status = False
                    break
                else:
                    continue
            else:
                if (('A' <= hexStr[i] <= 'F') or ('a' <= hexStr[i] <= 'f') or ('0' <= hexStr[i] <= '9')):
                    result += hexStr[i]
                else:
                    status = False
                    break
        if status:
            result = binascii.unhexlify(result)
        else:
            result = ''

        return status, result

