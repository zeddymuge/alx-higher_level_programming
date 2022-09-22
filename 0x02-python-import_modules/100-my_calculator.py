#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    match op:
      case "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
      case "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
      case "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
      case "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
      case_:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
