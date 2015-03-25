""" custom """
from threatconnect.Config.ResourceRegexes import indicators_regex


def validate_confidence(confidence):
    """ """
    if not isinstance(confidence, int):
        return False

    # todo - 0?
    return confidence in range(1, 101)


def validate_indicator(indicator):
    """ """
    for indicator_type, regex in indicators_regex.items():
        for rex in regex:
            if rex.match(indicator):
                return True
    return False


def validate_rating(rating):
    """ """
    if rating in ["1.0", "2.0", "3.0", "4.0", "5.0", 0, 1, 2, 3, 4, 5]:
        return True

    # todo - make this a bit more robust, 0?
    return False
