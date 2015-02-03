all:

Collatz.html: Collatz.py
	pydoc3 -w Collatz

Collatz.log:
	git log > Collatz.log

RunCollatz.tmp: RunCollatz.py RunCollatz.in
	RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	diff RunCollatz.tmp RunCollatz.out

TestCollatz.out: TestCollatz.py
	coverage3 run    --branch TestCollatz.py >  TestCollatz.out 2>&1
	coverage3 report -m                      >> TestCollatz.out

clean:
	rm -f .coverage
	rm -f *.pyc
	rm -f RunCollatz.tmp
	rm -f TestCollatz.out
	rm -rf __pycache__
