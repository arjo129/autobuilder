#!/usr/bin/python

import sys, json, autotester

def splitverno(version):
	comparator = ""
	vstring = ""
	for v in version:
		if v in set("gelt"):
			comparator +=v
		else:
			vstring += v
	return comparator, vstring


with open("configure.ab") as data_file:    
	    data = json.load(data_file)
	    #projectname = data["projectname"];
	    targets = data["targets"]
	    for t in targets:
		    for test in t["tests"]:
			    print test
			    testmethods = autotester.scan_testfile(test)
			    print testmethods
		    libraries = t["libs"]
		    for lib in libraries:
			    l,v = lib.items()[0]
			    print "#checking for: "+l+v
			    print l + "_version=`pkg-config --modversion "+l+"`"
			    comp,ver = splitverno(v)
			    print "if [ \"$(perl -e '($x,$y)=@ARGV; print $x "+comp+" $y' "+l+"_version "+ver+")\" != \"1\" ]"
			    print "then"
			    print "\techo \"FATAL: "+l+"-"+v+" not found\""
			    print "fi"
			    print l+"_cflags=`pkg-config --cflags "+l
			    print "sed -i \"s|__"+l+"_cflags__|$"+l+"_cflags|g\" makefile.wrk"
			    print l+"_linkflags=`pkg-config --libs "+l
			    print "sed -i \"s|__"+l+"_libs__|$"+l+"_linkflags|g\" makefile.wrk"
