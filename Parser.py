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
        self.virtual = False
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
        #Step 2: detect token type
        tokType = [None]*len(tokens)
        for i in range(0,len(tokens)):
            if i > 0:
                if tokens[i] == "/" and tokens[i-1] == "/":
                    tokType[i] = "inlinecomment"
                    tokType[i-1] = "inlinecomment"
                if tokType[i-1] == "inlinecomment":
                    if tokens[i] == "\n":
                        tokType[i] = "endl"
                    else:
                        tokType[i] = "inlinecomment"
