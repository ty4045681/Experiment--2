

# XOR two bytearrays
def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))

MSG   = "Yes"
HEX_1 = "a469b1c502c1cab966965e50425438e1bb1b5f9037a4c159"
HEX_2 = "bf73bcd3509299d566c35b5d450337e1bb175f903fafc159"

ciphertext_1 = "d1380b1aa9cb6a4213865286df8b1a2fc7c58f5cbc9e009ce7a54f17a7a1e027"
ciphertext_2 = "b41da6066a8083974677b5ee7d0a9e9fa621dcfba141122e832558bc9f8ecff7"

# Convert ascii string to bytearray
D1 = bytes(MSG, 'utf-8')
MSG_HEX = D1.hex()
print(MSG_HEX)

# Convert hex string to bytearray
D2 = bytearray.fromhex(HEX_1)
D3 = bytearray.fromhex(HEX_2)

iv = "a366e96067bbfffdea08e67374f2150b"
iv_2 = "4ce9916567bbfffdea08e67374f2150b"
iv_bytes = bytearray.fromhex(iv)
iv2_bytes = bytearray.fromhex(iv_2)

ciphertext = xor(D1, iv2_bytes)
ciphertext_hex = ciphertext.hex()
print(ciphertext_hex)
# iv = xor(D1, D2)
# MSG2 = xor(iv, D3)
# print(bytes(MSG2))
# f70e801347d28cdd8b288d1d1b857b2b
# 1881f81647d28cdd8b288d1d1b857b2b
# 5965730d0d0d0d0d0d0d0d0d0d0d0d0c