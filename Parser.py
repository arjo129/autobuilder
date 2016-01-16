class Object:
    def __init__(self):
        self.name = ""
        self.type = ""
class Class:
    def __init__(self):
        self.name = ""
        self.private = []
        self.public = []
        self.docString = ""
class Function:
    def __init__(self):
        self.arguments = []
        self.returnType = ""
        self.name = ""
        self.functionCalls = []
        self.docString = ""
class Parser:
    def __init__(self):
        self.filename = ""
        self.classes = []
        self.functions = []
        self.functionCalls = []
    def scan_file(fname):
        self.filename = fname
        #Step 1: tokenize
        tokens = []
        lasttoken = ""
        for line in open(fname):
            tokens.push(lasttoken)
            tokens.push("\n")
            lasttoken = ""
            for c in line():
                if c in set("{}[]()/<>.*+-=\|&*^% "):
                    tokens.push(lasttoken)
                    tokens.push(c)
                    lasttoken = ""
                else:
                    lasttoken += ""
            
