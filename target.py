import autotester
class target:
    def __init__(self):
        self.name = ""
        self.libraries = []
        self.tests = []
    def addLibrary(name,version):
        #TODO: implement
        self.libraries.add((name,version))
    def addTest(fname):
        testmod = autotester.testmodule();
        testmod.scan_testfile(fname)
        self.tests.add(testmod)
    def dep2str():
        depstr = ""
        for library,version in self.libraries:
            depstr += " __"+library+"_cflags__"
            depstr += " __"+libraty+"_libs__"
        return depstr
    def getPreScript():
        return ""
    def getPostScript():
        return ""
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
