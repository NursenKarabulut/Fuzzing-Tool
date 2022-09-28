import requests
dosya=open("fuzzing.txt","r")
icerik=dosya.read()
dosya.close()

for i in icerik.split()