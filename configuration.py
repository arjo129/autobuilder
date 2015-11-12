def splitverno(version):
	comparator = ""
	vstring = ""
	for v in version:
		if v in set("gelt"):
			comparator +=v
		else:
			vstring += v
	return comparator, vstring

class configuration:
	def __init__(self):
		self.libraries = []
		self.programs = []
	def addLibrary(lib, version):
		libObject = (lib,version)
		self.libraries.add(libObject)
	def generate():
		configw = open("configure.funcs","w")
		argparser = open("configure.argparser","w")
		for l,v in self.libraries:
			configw.write( "function checkFor"+l+v+"{");
			configw.write( l + "_version=`pkg-config --modversion "+l+"`")
			comp,ver = splitverno(v)
			configw.write( "if [ \"$(perl -e '($x,$y)=@ARGV; print $x "+comp+" $y' "+l+"_version "+ver+")\" != \"1\" ]")
			configw.write( "then" )
			configw.write( "\techo \"Check for "+l+"... [FAILED]")
			configw.write( "\techo \"FATAL: "+l+"-"+v+" not found\"" )#TODO: Provide further debugging as to why check failed
			configw.write( "\texit")
			configw.write( "fi" )
			configw.write( l+"_cflags=`pkg-config --cflags "+l )
			configw.write( "sed -i \"s|__"+l+"_cflags__|$"+l+"_cflags|g\" makefile.wrk" )
			configw.write( l+"_linkflags=`pkg-config --libs "+l)
			configw.write( "sed -i \"s|__"+l+"_libs__|$"+l+"_linkflags|g\" makefile.wrk" )
			configw.write( "echo \"Check for "+l+"... [OK]")
			configw.write( "}" )
		for prgm in self.programs:
			configw.write( "function checkPgm"+prgm+"{")
			configw.write( "hash "+prgm+" 2>/dev/null || || { echo >&2 \"I require foo but it's not installed.  Aborting.\"; exit 1; }")
			configw.write( "}")
		for prgm in self.programs:
			configw.write( "if [ -z ${"+prgm+"_path+x}];then function checkPgm; else alias "+prgm+"=$"+prgm+"_path;" )
		for l,v in self.libraries:
			configw.write( "if [ -z ${"+l+"_headers+x} ] || [ -z ${"+l+"_ldflags+x} ] ; then checkFor"+l+v+"; else echo \"Check for "+l+"...[skipped]\"; fi")
		configw.close()
		argparser.write("#!/bin/bash")
		argparser.write("hash perl 2>/dev/null || { echo >&2 \"./configure: Could not find perl. Aborting.\"; exit 1; }")
		argparser.write("hash sed 2>/dev/null ||{ echo >&2 \"./configure: Could not find sed  Aborting.\"; exit 1; }")
		argparser.write("for i in \"$@\"\ndo")
		argparser.write("case $i in")
		argparser.write("-h|--help)\necho \"Autobuild.py generated script\"\n;;")
		argparser.write("esac")
		argparser.close()
