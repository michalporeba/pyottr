import logging

from ottrlib.Ottr import Ottr


def main():
    logging.basicConfig(level=logging.DEBUG)
    sut = Ottr()
    sut.parse("ex:T[?a, ?b] :: { ottr:Triple(?a, rdfs:label, ?b) } .")
    errors = sut.validate(
        """
        ex:T(p:Test, "test") .
        ex:T(p:Test) .
        ex:T() .
        ex:T(p:Test, "test") .
        """
    )

    for e in errors:
        print(e)


if __name__ == "__main__":
    main()
