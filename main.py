import hashlib

secret = "Jakies wymyslone haslo"

bsecret = secret.encode()

m = hashlib.md5()

m.update(bsecret)

print(m.digest())