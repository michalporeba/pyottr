import logging

from .ottr import tryit


def main():
    logging.basicConfig(level=logging.ERROR)
    tryit()


if __name__ == "__main__":
    main()
