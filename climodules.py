import autotest, os
cmdlets = {'init': initNewProject}
def initNewProject():
	try:
		os.makedirs("src")
	except OSError:
		if not os.path.isdir("src"):
			raise
	testingenabled = raw_input('Enable Testing (y/n):')
	if testingenabled == "y":
		try:
			os.makedirs("test")
		except:
			if not os.path.isdir("src"):
				raise
	
