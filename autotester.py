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
