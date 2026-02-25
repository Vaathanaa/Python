# Base class for cyber tools
class SecurityTool:
    def __init__(self, target):
        self.target = target
    def validate(self):
        print(f" Validating target: {self.target}")
    def log(self, message):
        print(f"[STATUS]: {message}")
# Child 1: Port Scanner 
class PortScanner(SecurityTool):
    def scan(self):
        self.validate()
        self.log("Scanning ports...")
        print(" - Port 22: open")
        print(" - Port 80: open")
# Child 2: Web Scanner 
class WebScanner(SecurityTool):
    def scan(self):
        self.validate()
        self.log("Checking for web vulnerabilities...")
        print(" - No XSS detected")
        print(" - No SQLi detected")
# Child 3: Malware Analyzer 
class MalwareAnalyzer(SecurityTool):
    def scan(self):
        self.validate()
        self.log("Analyzing file...")
        print(" - Hash: 21F3A1...")
        print(" - No known malware signature found")

port = PortScanner("192.168.1.10")
web  = WebScanner("http://www.facebook.com")
mal  = MalwareAnalyzer("pythonattack.exe")

port.scan()
web.scan()
mal.scan()
