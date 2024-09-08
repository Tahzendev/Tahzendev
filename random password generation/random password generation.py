import random
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Tahzen Developer Password Generation	")
print(ascii_banner)

password_len = int(input("how many charaters should the password consist of:"))
password_count = int(input("how many passwords to create:"))

chars =  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

for _ in range(password_count):
    password = "".join(random.choice(chars)for _ in range(password_len))
    print("your random password:", password)

    #By Tahzen Developer 