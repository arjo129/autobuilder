import configuration
class Project:
    __init__(self):
        self.projectname = ""
        self.lisence = ""
        self.author = ""
        self.configuration = configuration.configuration()
        self.targets = {}
        self.tests = []

    def addDependency(target,name, version):
        self.configuration.addLibrary(name,version)
        self.targets[target].addLibrary(name,version)
    def generateMakefile():
        makefile = open(makefile.wrk)
