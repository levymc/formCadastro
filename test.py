import hashlib

password = input("digite sua senha:")
passwordCod = hashlib.md5(password.encode()).hexdigest()

print(passwordCod)