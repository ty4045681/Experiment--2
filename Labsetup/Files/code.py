def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))

iv = "46927409f4905cccfffe36f958406b89"
iv_next = "1096ce11f4905cccfffe36f958406b89"
iv_next_1 = "e6d64869f4905cccfffe36f958406b89"
iv_int = int(iv, base=16)
iv_next_int = int(iv_next, base=16)
iv_next_1_int = int(iv_next_1, base=16)
print(iv_int)
print(iv_next_int)
print(iv_next_1_int)