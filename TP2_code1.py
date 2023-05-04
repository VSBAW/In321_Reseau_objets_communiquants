import socket

# Configuration des paramètres de connexion
IP = "127.0.0.1"  # Adresse IP locale pour tester sur une seule machine
PORT = 50000     # Numéro de port choisi

# Création de la socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

# Boucle principale
while True:
    # Attente de réception d'un message
    data, addr = sock.recvfrom(1024)
    print("Reçu :", data.decode())

    # Vérification si l'utilisateur souhaite quitter le programme
    if data.decode() == "exit":
        break

    # Envoi d'un message
    message = input("Envoyer un message : ")
    sock.sendto(message.encode(), addr)

    # Vérification si l'utilisateur souhaite quitter le programme
    if message == "exit":
        break

# Fermeture de la socket
sock.close()
