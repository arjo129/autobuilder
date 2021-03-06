import autotest, os, json

cmdlets = {'init': initNewProject , 'help': help, 'version': version}
defaultmodule = "help"

def help():
	print "Autobuilder - Project management and unit testing for C/C++"
	print ""
	print "To create a new project:\n\tautobuilder init"
	print "To package as a nice gnu project:\n\tautobuilder export"
	print "To update unit tests:\n\tautobuilder test"
def version():
	print "0.0.1"
def initNewProject():
	schema = {"projectname": raw_input("Name Of Project:"),
	"lisence": raw_input("Lisence type e.g MIT:"),
	"author": raw_input("Author's name e.g Arjo Chakravarty <arjo129@gmail.com>:")
	"targets": [ {"name":raw_input("Name of first target"),"type":raw_input("Type of output (static library, dynamic library, executable, pymod, etc.):")} ]}
	try:
		os.makedirs("src")
	except OSError:
		if not os.path.isdir("src"):
			raise
	testingenabled = raw_input('Enable Testing (y/n):')
	if testingenabled == "y":
		try:
			os.makedirs("tests")
		except:
			if not os.path.isdir("tests"):
				raise
		schema["tests"] = []
def addTarget():
	print "adding targets..."
