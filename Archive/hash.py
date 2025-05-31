import hashlib

def brute_force(hash):
    for num in range(1000000):
        num_str = str(num).zfill(6)
        if hashlib.md5(num_str.encode()).hexdigest() == hash:
            return num_str

# hash = '3cc6520a6890b92fb55a6b3d657fd1f6'
# print(brute_force(hash))

secret = '123456'
text = 'hello'
for i in range(1, len(secret)+1):
    letter = ord(list(secret)[i]) + ord(list(plain_text)[i])