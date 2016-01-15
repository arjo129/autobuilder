class Object:
    def __init__(self):
        self.name = ""
        self.type = ""
class Class:
    def __init__(self):
        self.name = ""
        self.private = []
        self.public = []
class Function:
    def __init__(self):
        self.arguments = []
        self.returnType = ""
        self.name = ""
        self.functionCalls = []
class Parser:
    def __init__(self):
        self.filename = ""
        self.classes = []
        self.functions = []
        self.functionCalls = []
    def scan_file(fname):
        self.filename = fname
