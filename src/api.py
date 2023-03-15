from bitstring import BitArray
import os
if os.path.split(os.getcwd())[1] == "src":
    from des import DES
else:
    from .des import DES

def call(action, encoding, inText, key):
    des = DES()
    if action == "encrypt":
        x = BitArray(hex=inText, length=64)
        k = BitArray(hex=key, length=64)
        des.encrypt(x, k)
    return des.data
