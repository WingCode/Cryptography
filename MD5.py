import array
import binascii

s=[-1 for i in range(0,64)]
K=[-1 for i in range(0,64)]

s[0:16]   = [ 7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22 ]
s[16:32]  = [ 5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20 ]
s[32:48]  = [ 4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23 ]
s[48:64]  = [ 6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21 ]

'''
print(len(s[0:16]))
print(s[0:16])
print(len(s[16:32]))
print(s[16:32])
print(len(s[32:48]))
print(s[32:48])
print(len(s[48:64]))
print(s[48:64])
'''
K[ 0: 4] = [ 0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee ]
K[ 4: 8] = [ 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501 ]
K[ 8:12] = [ 0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be ]
K[12:16] = [ 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821 ]
K[16:20] = [ 0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa ]
K[20:24] = [ 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8 ]
K[24:28] = [ 0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed ]
K[28:32] = [ 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a ]
K[32:36] = [ 0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c ]
K[36:40] = [ 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70 ]
K[40:44] = [ 0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05 ]
K[44:48] = [ 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665 ]
K[48:52] = [ 0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039 ]
K[52:56] = [ 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1 ]
K[56:60] = [ 0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1 ]
K[60:64] = [ 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391 ]

a0 = 0x67452301   #A
b0 = 0xefcdab89   #B
c0 = 0x98badcfe   #C
d0 = 0x10325476   #D

l=bin(int(binascii.hexlify("a"),16))
print(l)
print(len(l))

# msg_len % 512 = 448