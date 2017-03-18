S = []
T = []


# If the length of the key K is 256 bytes, then K is transferred to T. Otherwise,
# for a key of length keylen bytes, the first keylen elements of T are copied
# from K and then K is repeated as many times as necessary to fill out T.
def initialize(key):

    for i in range(255):
        S[i] = i
        T[i] = key[i % len(key)]


# starting with S[0] and going through to S[255], and, for each S[i],
# swapping S[i] with another byte in S according to a scheme dictated by T[i]
def initial_permutation():
    j = 0
    for i in range(255):
        j = ((j + S[i] + T[i]) % 256)
        # swap S[i] and S[j]
        S[i], S[j] = S[j], S[i]


def stream_generator():
    i, j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        # swap S[i] and S[j]
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = S[t]
        # To encrypt, XOR the value k with the next byte of plaintext.
        # To decrypt, XOR the value k with the next byte of ciphertext.
        return k
