import autotest, os, json
cmdlets = {'init': initNewProject , 'add-pkg:': addPkg}

def addPkg(packagename):
	
def initNewProject():
	schema = {"projectname": raw_input('Name Of Project:')}
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
