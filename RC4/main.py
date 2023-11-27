def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

str_key = "Key"
key = []
for k in str_key:
    key.append(ord(k))
key_len = len(key)

S = []
for i in range(256):
    S.append(i)

j = 0
for i in range(256):
    j = (j + S[i] + key[i % key_len]) % 256
    swap(S, i, j)

i = 0
j = 0
for o in range(256):
    i = (i + 1) % 256
    j = (j + S[i]) % 256
    swap(S, i, j)
    K = S[(S[i] + S[j]) % 256]
    print(K, end=",")