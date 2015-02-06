#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, over_flow, cycle_length, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

        s    = "40 50\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  40)
        self.assertEqual(j, 50)

        s    = "777 4444\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  777)
        self.assertEqual(j, 4444)

    # ----
    # cycle_length
    # ----

    def test_cycle_length_1(self):
        i = cycle_length(10)
        self.assertEqual(i, 7)

    def test_cycle_length_2(self):
        i = cycle_length(9)
        self.assertEqual(i, 20)

    def test_cycle_length_3(self):
        i = cycle_length(20)
        self.assertEqual(i, 8)


    # ----
    # over_flow
    # ----

    def test_over_flow_1(self):
        i = over_flow(2147483648)
        self.assertEqual(i, 1)

    def test_over_flow_2(self):
        i = over_flow(2147483657)
        self.assertEqual(i, 10)

    def test_over_flow_3(self):
        i = over_flow(2147483747)
        self.assertEqual(i, 100)


    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = collatz_eval(1, 999)
        self.assertEqual(v, 179)

    def test_eval_6 (self) :
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_7 (self) :
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 526)

    def test_eval_8 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)
        
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 999, 179)
        self.assertEqual(w.getvalue(), "1 999 179\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1000, 2000, 182)
        self.assertEqual(w.getvalue(), "1000 2000 182\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n1000 2000\n1 1\n10 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n1000 2000 182\n1 1 1\n10 1 20\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""# pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
