#! python3
# budi.py

print("Hello World!")

valueHex = 0x1FAFAFAF1FAFAFAF
#0F1571C947D9E859
tidyHex = format(int('3B3898371520F75E', 16), '064b')
print('tidyHex = ' + tidyHex)

#m_real = 3
#m_arr = m_real-1
#print('m_real[' + str(int(m_real)) + '] = ' + tidyHex[m_arr])

_tidyHex_keyA = tidyHex[0] +tidyHex[1] +tidyHex[2] +tidyHex[3] +tidyHex[4] +tidyHex[5] +tidyHex[6]
_tidyHex_keyB = tidyHex[8] +tidyHex[9] +tidyHex[10]+tidyHex[11]+tidyHex[12]+tidyHex[13]+tidyHex[14]
_tidyHex_keyC = tidyHex[16]+tidyHex[17]+tidyHex[18]+tidyHex[19]+tidyHex[20]+tidyHex[21]+tidyHex[22]
_tidyHex_keyD = tidyHex[24]+tidyHex[25]+tidyHex[26]+tidyHex[27]+tidyHex[28]+tidyHex[29]+tidyHex[30]

_tidyHex_keyP = _tidyHex_keyA + _tidyHex_keyB + _tidyHex_keyC + _tidyHex_keyD

_tidyHex_keyE = tidyHex[32]+tidyHex[33]+tidyHex[34]+tidyHex[35]+tidyHex[36]+tidyHex[37]+tidyHex[38]
_tidyHex_keyF = tidyHex[40]+tidyHex[41]+tidyHex[42]+tidyHex[43]+tidyHex[44]+tidyHex[45]+tidyHex[46]
_tidyHex_keyG = tidyHex[48]+tidyHex[49]+tidyHex[50]+tidyHex[51]+tidyHex[52]+tidyHex[53]+tidyHex[54]
_tidyHex_keyH = tidyHex[56]+tidyHex[57]+tidyHex[58]+tidyHex[59]+tidyHex[60]+tidyHex[61]+tidyHex[62]

_tidyHex_keyQ = _tidyHex_keyE + _tidyHex_keyF + _tidyHex_keyG + _tidyHex_keyH

no_8thbit_key = _tidyHex_keyP + _tidyHex_keyQ
print('no_8thbit_key = ' + no_8thbit_key)

print(_tidyHex_keyA)
print(_tidyHex_keyB)
print(_tidyHex_keyC)
print(_tidyHex_keyD)
print(_tidyHex_keyE)
print(_tidyHex_keyF)
print(_tidyHex_keyG)
print(_tidyHex_keyH)

pc1_tidyHex = format(int('0x0000000000000000', 16), '064b')

_pc1_tidyHexA = [tidyHex[56], tidyHex[48], tidyHex[40], tidyHex[32], tidyHex[24], tidyHex[16], tidyHex[8]]
_pc1_tidyHexB = [tidyHex[0] , tidyHex[57], tidyHex[49], tidyHex[41], tidyHex[33], tidyHex[25], tidyHex[18]]
_pc1_tidyHexC = [tidyHex[9] , tidyHex[1] , tidyHex[58], tidyHex[50], tidyHex[42], tidyHex[34], tidyHex[27]]
_pc1_tidyHexD = [tidyHex[18], tidyHex[10], tidyHex[2] , tidyHex[59], tidyHex[51], tidyHex[43], tidyHex[35]]
_pc1_tidyHexE = [tidyHex[62], tidyHex[54], tidyHex[46], tidyHex[38], tidyHex[30], tidyHex[22], tidyHex[14]]
_pc1_tidyHexF = [tidyHex[7] , tidyHex[61], tidyHex[53], tidyHex[45], tidyHex[37], tidyHex[29], tidyHex[21]]
_pc1_tidyHexG = [tidyHex[13], tidyHex[5] , tidyHex[60], tidyHex[52], tidyHex[44], tidyHex[36], tidyHex[28]]
_pc1_tidyHexH = [tidyHex[20], tidyHex[12], tidyHex[4] , tidyHex[27], tidyHex[19], tidyHex[11], tidyHex[3]]

print('After PC1')
pc1_tidyHexA = str(''.join(_pc1_tidyHexA)); print(pc1_tidyHexA)
pc1_tidyHexB = str(''.join(_pc1_tidyHexB)); print(pc1_tidyHexB)
pc1_tidyHexC = str(''.join(_pc1_tidyHexC)); print(pc1_tidyHexC)
pc1_tidyHexD = str(''.join(_pc1_tidyHexD)); print(pc1_tidyHexD)
pc1_tidyHexE = str(''.join(_pc1_tidyHexE)); print(pc1_tidyHexE)
pc1_tidyHexF = str(''.join(_pc1_tidyHexF)); print(pc1_tidyHexF)
pc1_tidyHexG = str(''.join(_pc1_tidyHexG)); print(pc1_tidyHexG)
pc1_tidyHexH = str(''.join(_pc1_tidyHexH)); print(pc1_tidyHexH)

pc1_C = pc1_tidyHexA+pc1_tidyHexB+pc1_tidyHexC+pc1_tidyHexD ; print('pc1_C = ' + pc1_C) #; print(len(pc1_C))
pc1_D = pc1_tidyHexE+pc1_tidyHexF+pc1_tidyHexG+pc1_tidyHexH ; print('pc1_D = ' + pc1_D) #; print(len(pc1_D))

shift_keyC = pc1_C[1::]+pc1_C[:1:]
shift_keyD = pc1_D[1::]+pc1_D[:1:]
print('shift_keyC = ' + shift_keyC)
print('shift_keyD = ' + shift_keyD)


#pc2_map = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
pc2_map =  [13, 16, 10, 23, 0, 4, 2, 27, 14, 5, 20, 9,  22, 18, 11, 3, 25, 7, 15, 6, 26, 19, 12, 1, 40, 51, 30, 36, 46, 54, 29, 39, 50, 44, 32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31]


shift_key = shift_keyC + shift_keyD
int_shift_key = int(shift_key, base=2)
#print('shift_key')
#print(int_shift_key)

#pc2_map = [0, 1, 2, 3, 4, 5, 6, 7, 8]
bin_shift_key = bin(int_shift_key)[2:][::+1]
B = int(''.join(bin_shift_key[i] for i in pc2_map), 2)
print(bin(B))

key = format(B, '048b')
print('key = ' + key)

arr_key = [key[i:i+6] for i in range(0, len(key), 6)]
print(arr_key[0])

hexkey = format(arr_key[0], '08b')


