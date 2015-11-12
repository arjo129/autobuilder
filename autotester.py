def scan_testfile(file):
	listOfTests = []
	listOfBenchMarks = []
	braces = 0
	for line in open(file):
		lasttoken = ""
		commentoff = True
		potentialtest = False
		potentialbenchmark = False
		for c in line:
			if c=='{':
				braces++
			if c=='}':
				braces--	
			if c in set(" ({}*)_[]&+-/#"):
				if braces==0 and lasttoken=="_test_results_t" and commentoff:
					potentialtest = True
				if braces==0 and lasttoken=="_benchmark_timer_t" and commentoff:
					potentialbenchmark = True
				if braces==0 and potentialtest and lasttoken.startsWith("TEST_"):
					listOfTests.append(lasttoken)
					potentialtest = False
				if braces==0 and potentialbenchmark and lasttoken.startsWith("BENCHMARK_"):
					listOfBenchMarks.append(lasttoken)
					potentialbenchmark = False
				lasttoken=""
			else:
				lasttoken+=c
	return listOfTests, listOfBenchMarks
