import autotester
class target:
    def __init__(self):
        self.name = ""
        self.libraries = []
        self.tests = []
        self.library = False
        self.dynamic = True
    def addLibrary(name,version):
        #TODO: implement
        self.libraries.add((name,version))
    def addTest(fname):
        testmod = autotester.testmodule();
        testmod.scan_testfile(fname)
        self.tests.add(testmod)
    def dep2str():
        depstr = ""
        if self.library and self.dynamic: depstr+= ""
        if self.library and not self.dynamic: depstr+= ""
        for library,version in self.libraries:
            depstr += " __"+library+"_cflags__"
            depstr += " __"+library+"_libs__"
        return depstr
    def getPreScript():
        return ""
    def getPostScript():
        self.postScript = ""
        if not self.dynamic:
            self.postScript += "\nar" #TODO implement correct command
        return self.postScript
    def getsources():
        return ""
    def getFlags():
        return ""
    def getTests():
        return ""
    def disableMain():
        pass
    def enableMain():
        pass
