import os

def finalPass:
	autotest_files = os.listdir("tests/ab")
	headerfile = open("tests/tests.h","w")
	valgrindscript = open("tests/run_valgrind.sh","w")
	testsscript = open("tests/run_tests.sh","w")
	for file in autotest_files:
		fname = os.path.basename(file)
		name,ext = os.path.splittext(fname)
		if ext == ".h":
			headerfile.write("#include \"ab/"+fname+"\")
		if ext == ".c":
			testsscript.write("./"+name+">> test_results.rslt")
	headerfile.close()
	valgrindscript.close()
	testscript.close()
class testmodule:
	def __init__(self):
		self.listOfTests = []
		self.listOfValgrind = []
		self.listOfBenchMarks = []
		self.includes = []
		self.modulename = ""
	def scan_testfile(file):
		name = os.path.basename(file)
		self.modulename = os.path.splittext(name)[0]
		comment = false
		braces = 0
		lastlinemmode = False
		for line in open(file):
			lasttoken = ""
			inlinecomment = False
			potentialtest = False
			potentialbenchmark = False
			potentialmemtest = False
			potentialcomment = False
			potentialmacro = False
			for c in line:
				if potentialcomment:
					potentialcomment = False
					if c == '*':
						comment = True
					if c == '/':
						inlinecomment = True
				if not comment and not inlinecomment:
					if c == '{':
						braces = braces + 1
					if c == '}':
						braces = braces - 1
					if c == '/':
						potentialcomment = True
					if c in set(" \"'<>({}*)=[]&+-\/#"):
						# Process last token here
						if braces==0 and lasttoken=="_test_results_t" and commentoff:
							potentialtest = True
						if braces==0 and lasttoken=="_valgrind_results_t" and commentoff:
							potentialmemtest = True
							#print "found test"
						if braces==0 and lasttoken=="_benchmark_timer_t" and commentoff:
							potentialbenchmark = True
						if braces==0 and potentialmemtest and lasttoken.startswith("LEAK_TEST_"):
							self.listOfValgrind.append(lasttoken)
							potentialmemtest = False
						if braces==0 and potentialtest and lasttoken.startswith("TEST_"):
							self.listOfTests.append(lasttoken)
							potentialtest = False
						if braces==0 and potentialbenchmark and lasttoken.startswith("BENCHMARK_"):
							self.listOfBenchMarks.append(lasttoken)
							potentialbenchmark = False
						lasttoken = ""
				if comment:
					if c == '*':
						potentialcomment = True
					if potentialcomment and c == '/':
						comment = False

	def generateSrcFiles():
		headerfile = open("tests/ab/benchmark.h","w")
		for b in self.listOfBenchMarks:
			headerfile.write("\n_benchmark_timer_t "+b+"(benchmark_timer_t t);")
		headerfile.close()
		headerfile = open("tests/ab/tests_"++".h","w")
		for t in self.listOfTests:
			headerfile.write("\n_test_results_t "+t+"();")
		headerfile.close()
		main = open("tests/ab/tests_"+self.modulename+"_main.cpp","w")
		main.write("include \"tests.h\"")
		main.write("int main(int argc, char** argv) {")
		main.write("\t_result_reporter_t rep;")
		for t in self.listOfTests:
			main.write("\t_report_results(rep,"+t+"());")
		for b in self.listOfBenchMarks:
			main.write("\t_report_results(rep,"+b+"());")
		main.close();
		for memtest in self.listOfValgrind:
			main = open("tests/ab/valgrind/_"+self.modulename+"_"+memtest+".cpp")
			main.write("#include \"../valgrind_"+self.modulename+".h\"")
			main.write("int main(int argc, char** argv) {")
			main.write("\t"+memtest+"();")
			main.write("\treturn 0;")
			main.write("}")
			main.close()

def scan_testfile(file):
	listOfTests = []
	listOfBenchMarks = []
	listOfValgrind = []
	includes = []
	braces = 0
	for line in open(file):
		lasttoken = ""
		commentoff = True
		potentialtest = False
		potentialbenchmark = False
		potentialmemtest = True
		if line.startswith("#include"):
			includes.append(line)
		for c in line:
			#print lasttoken
			if c=='{':
				braces = braces + 1
			if c=='}':
				braces = braces - 1
			if c in set(" ({}*)[]&+-/#"):
				if braces==0 and lasttoken=="_test_results_t" and commentoff:
					potentialtest = True
				if braces==0 and lasttoken=="_valgrind_results_t" and commentoff:
					potentialmemtest = True
					#print "found test"
				if braces==0 and lasttoken=="_benchmark_timer_t" and commentoff:
					potentialbenchmark = True
				if braces==0 and potentialmemtest and lasttoken.startswith("LEAK_TEST_"):
					listOfValgrind.append(lasttoken)
					potentialmemtest = False
				if braces==0 and potentialtest and lasttoken.startswith("TEST_"):
					listOfTests.append(lasttoken)
					potentialtest = False
				if braces==0 and potentialbenchmark and lasttoken.startswith("BENCHMARK_"):
					listOfBenchMarks.append(lasttoken)
					potentialbenchmark = False
				lasttoken=""
			else:
				lasttoken+=c
	return listOfTests, listOfBenchMarks

def genTestHeaders(tests):
	headerfile = open("tests/tests.h","w")
	headerfile.write("#include <autobuildpy/autotester>");
	headerfile.write("#include \"benchmarks.h\"")
	for t in tests:
		headerfile.write("\n_test_results_t "+t+"();")
	headerfile.close()

def genBMHeaders(benchmarks):
	headerfile = open("tests/benchmark.h","w");
	headerfile.write("#include \"test_includes.h\"")
	for b in benchmarks:
		headerfile.write("\n_benchmark_timer_t "+t+"(benchmark_timer_t t);")
	headerfile.close()

def genMemTests(tests, includes):
	for test in tests:
		tname = test.strip("(){} ")
		mainfile = open("tests/.bm/"+tname+".cpp")
		for test in includes:

def genMainTestFile(tests,benchmarks):
	main = open("tests/testsmain.c","w")
	main.write("include \"tests.h\"")
	main.write("int main(int argc, char** argv) {")
	main.write("\t_result_reporter_t rep;")
	for t in tests:
		main.write("\t_report_results(rep,"+t+"());")
	for b in benchmarks:
		main.write("\t_report_results(rep,"+b+"());")
	main.close()
