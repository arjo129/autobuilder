def scan_testfile(file):
	listOfTests = []
	listOfBenchMarks = []
	braces = 0
	for line in open(file):
		lasttoken = ""
		commentoff = true
		potentialtest = false
		potentialbenchmark = false
		for c in line:
			if c=='{':
				braces++
			if c=='}':
				braces--	
			if c in set(" ({}*)_[]&+-/#"):
				if braces==0 and lasttoken=="_test_results_t" and commentoff:
					potentialtest=true
				if braces==0 and lasttoken=="_benchmark_timer_t" and commentoff:
					potentialbenchmark
				lasttoken=""
			else:
				lasttoken+=c
