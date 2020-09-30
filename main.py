import socket        # importeer librarys
import subprocess

hostname = socket.gethostname()     # laat socket de hostname van mijn laptop vinden
IPaddr = socket.gethostbyname(hostname)# laat socket het ip adres van mijn laptop vinden met de hostnaam als argument
y = subprocess.getstatusoutput("arp -a")   # om de daadwerkelijke dingen te vinden op mijn netwerk gebruik in een terminal command: apr -a, deze zoekt de gebruikers en sorteert ze
x = y[1] # neem uit de tuple "y" alleen de strings, dus op de 2e plaats van de tuple [1] dus
alladdr = x.replace("\n", "\ndevice: ") # zet voor elke nieuwe regel "device: "
print("your computers hostname is:" + hostname) # print de hostnaam
print("your computers ip address is:"  + IPaddr) # print het ip adres, hetzelfde maar op een andere manier, want dat is leuker
print("device: " + alladdr) # laat de gevonden devices zien!
