import sys


if sys.argv.count("-git") > 0:
    sys.path.append(__file__.rstrip("main.py"))


def main():
    print("hello, world!")


def run_test() -> bool:
    try:
        print("")
        main()
        return True
    except Exception:
        return False

