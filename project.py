import configuration
class Project:
    __init__(self):
        self.projectname = ""
        self.lisence = ""
        self.author = ""
        self.configuration = configuration.configuration()
        self.targets = {}
        self.Embedded = False
    def addDependency(target,name, version):
        self.configuration.addLibrary(name,version)
        self.targets[target].addLibrary(name,version)
    def generateMakefile():
        makefile = open("makefile.wrk")
        for target in self.targets:
            makefile.write(target.name+":"+target.dep2str())
            makefile.write(target.getPreScript())
            makefile.write("\t$(TARGETCC) "+target.getsources()+" "+target.getFlags())
            makefile.write(target.getPostScript())
            if not self.Embedded and target.library:
                makefile.write(target.name+"-tests:"+target.name)
            else:
                makefile.write(target.name+"-tests:")
                if target.library:
                    makefile.write("\t$(HOSTCC) "+target.getsources()+" "+target.getFlags())
                else:
                    for test in target.getTests():
                        makefile.write("\t$(HOSTCC) "+test+" "+target.getsources()+" "+target.getFlags())
            makefile.write(target.name)