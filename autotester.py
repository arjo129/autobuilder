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
			#print lasttoken
			if c=='{':
				braces = braces + 1
			if c=='}':
				braces = braces - 1	
			if c in set(" ({}*)[]&+-/#"):
				if braces==0 and lasttoken=="_test_results_t" and commentoff:
					potentialtest = True
					#print "found test"
				if braces==0 and lasttoken=="_benchmark_timer_t" and commentoff:
					potentialbenchmark = True
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
