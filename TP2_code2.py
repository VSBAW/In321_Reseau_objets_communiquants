"""print("les cours de reseaux c'est super")
a = "fabien"
# string to bytes with ascii encoding:
b = a.encode('ascii')
c = b"fabien"
# bytes containing ascii are automaticaly decoded by print
print(b)
print(b.decode('ascii'))
# to utf-8
d = "éàç"
e = d.encode("utf-8")
# bytes containing utf8 are not automaticaly decoded by print
# to convert to string
print(e.decode("utf-8"))
"""
""" Code 2"""

import socket

# Configuration des paramètres de connexion
IP = "127.0.0.1"  # Adresse IP locale pour tester sur une seule machine
PORT = 50000     # Numéro de port choisi

# Création de la socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Boucle principale
while True:
    # Envoi d'un message
    message = input("Envoyer un message : ")
    sock.sendto(message.encode(), (IP, PORT))

    # Vérification si l'utilisateur souhaite quitter le programme
    if message == "exit":
        break

    # Attente de réception d'un message
    data, addr = sock.recvfrom(1024)
    print("Reçu :", data.decode())

    # Vérification si l'utilisateur souhaite quitter le programme
    if data.decode() == "exit":
        break

# Fermeture de la socket
sock.close()
