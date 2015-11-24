class makefileTemplateGenerator:
	def dep2str(deps):
		outstr = ""
		for dep in deps:
			outstr+=dep
			outstr+=" "
	def generate(targets, targetfiles, dependencies):
		makefile = open("makefile.in")
		for target in targets:
			makefile.write(target+": "+dep2str(dependencies))
			makefile.write(target+": "+)
		makefile.write(check+": "+dep2str(targets))
		makefile.write("\t$CC tests/*.c tests/*.cpp $CFLAGS $LDFLAGS -Iautotester/include -o autotester/bin/tests.bin")
		makefile.write("autotester/bin/tests.bin")