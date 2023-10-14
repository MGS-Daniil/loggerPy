def main():
    print("hello, world!")


def run_test() -> bool:
    try:
        main()
        return True
    except Exception:
        return False

