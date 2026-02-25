class Malware:
    def describe(self):
        return "This is a malware."
    
class ransomware(Malware): #ransomware inherit from Malware
    def encrypt_files(self):
        return "File are being encrypted."
    
class virus(Malware):#virus inherit from Malware
    def replicate(self):
        return "Virus is replicating."
    
class trojan(Malware):#trojan inherit from Malware
    def hide_in_file(self):
        return "Hiding in files."
    
class keyLogger(trojan): #keylogger inherit from trojan
    def describe(self):
        return "This a keylogger. Capturing k`eystrokes."

m = Malware()
r = ransomware()
v = virus()
t = trojan()
k = keyLogger()

print(f"Virus Description: {v.describe()}")
print(f"Virus Action: {v.replicate()}")
print(f"Trojan Description: {t.describe()}")
print(f"Trojan Action: {t.hide_in_file()}")
print(f"Keylogger Description: {k.describe()}")
print(f"keylogger Action: {k.hide_in_file()}")