import re


def validate(regex, text):
    result = re.search(regex, text)
    return False if result is None or result.group() != text else True
