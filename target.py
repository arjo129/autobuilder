import autotester

class target:
    def __init__(self):
        self.name = ""
        self.libraries = []
        self.tests = []
        self.type = ""
        self.library = False
        self.dynamic = True
        self.mainenabled = True
        self.sources = []
        self.dependencies = []
    def addLibrary(name,version):
        #TODO: implement
        self.libraries.add((name,version))
    def addTest(fname):
        testmod = autotester.testmodule();
        testmod.scan_testfile(fname)
        self.tests.add(testmod)
    def dep2str():
        deps = ""
        for dep in dependencies
            deps += " "+dep
        return deps
    def getPreScript():
        prescr = self.prescript
        #TODO perform main removal
        if self.mainenabled:
            return prescr
        return prescr
    def getPostScript():
        self.postScript = ""
        if not self.dynamic:
            self.postScript += "\nar" #TODO implement correct command
        return self.postScript
    def getsources():
        src = ""
        for source in sources:
            src = " "+source
        return src
    def getFlags():
        depstr = ""
        if self.library and self.dynamic: depstr+= ""
        if self.library and not self.dynamic: depstr+= ""
        for library,version in self.libraries:
            depstr += " __"+library+"_cflags__"
            depstr += " __"+library+"_libs__"
        return depstr
    def getTests():
        return ""
    def findMain():

    def disableMain():
        pass
    def enableMain():
        pass
