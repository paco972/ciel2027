import socket
import time

ip_serveur = "192.168.1.241"
port = 2300

try:
    # Création d'une socket client en IPv4 et TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_serveur, port))
        print("Connecté au serveur teleinfo")
        time.sleep(4)
        trames = s.recv(1024).decode('ascii', errors='ignore')
        lignes = trames.split("\n")
        #print(lignes)
        for ligne in lignes:
            if ligne.find("ADCO") != -1:
                #print("Trouvé")
                positionNumeroSerie = ligne.find(' ') + 1
                numeroSerie = ligne[positionNumeroSerie:-3]
            if ligne.find("PAPP") != -1:
                #print("Trouvé")
                positionPuissanceApparente = ligne.find(' ') + 1
                puissanceApparente = ligne[positionPuissanceApparente:-3]
            if ligne.find("HCHC") != -1:
                #print("Trouvé")
                positionIndexHeuresCreuses = ligne.find(' ') + 1
                indexHeuresCreuses = ligne[positionIndexHeuresCreuses:-3]

        print(f"Numéro de série : {numeroSerie}")
        print(f"Puissance apparente : {puissanceApparente}")
        print(f"Index heures creuses : {indexHeuresCreuses}")

except(socket.timeout, socket.error) as e:
    print(f"Erreur de réseau : {e}")
 