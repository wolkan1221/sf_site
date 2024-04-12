import time

def main() -> None:
    for i in "Hello World":
        print(i +" ", end=" ", flush=True)
        time.sleep(0.3)


if __name__ == "__main__":
    main()