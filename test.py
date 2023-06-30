import hashlib

password = '302911'
passwordCod = hashlib.md5(password.encode()).hexdigest()

print(passwordCod)