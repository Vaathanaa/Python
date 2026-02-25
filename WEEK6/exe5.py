class Logger:
    def log(self):
        return "Error"

class Log(Logger):
    def log(self):
        return "Log: System started."
    
class ErrorCode(Logger):
    def log(self):
        return "Error Code: 404, Details: {'url': '/not-found'}."

class Message(Logger):
    def log(self):
        return "Unknown log format."
# Polymorphism function 
def loggin(logger):
    print(logger.log())

L = Log()
E = ErrorCode()
M = Message()

#  Use Polymorphism
loggin(L)
loggin(E)
loggin(M)