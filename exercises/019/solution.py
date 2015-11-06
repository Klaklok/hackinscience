import sys
import operator

if len(sys.argv) < 2:
    print("usage : python3 solution.py OP1 OP2")
else:
    sys.argv[1] = int(sys.argv[1])
    sys.argv[2] = int(sys.argv[2])
    print(operator.add(sys.argv[1], sys.argv[2]))
