class StringException(Exception):
    ...


class NegativeLengthString(StringException):
    ...


class ExceedLengthString(StringException):
    ...


try:
    raise ExceedLengthString
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")
