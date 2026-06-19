from numbers import Real

CLASSES = [
    "backward",
    "bed",
    "bird",
    "cat",
    "dog",
    "down",
    "eight",
    "five",
    "follow",
    "forward",
    "four",
    "go",
    "happy",
    "house",
    "learn",
    "left",
    "marvin",
    "nine",
    "no",
    "off",
    "on",
    "one",
    "right",
    "seven",
    "sheila",
    "six",
    "stop",
    "three",
    "tree",
    "two",
    "up",
    "visual",
    "wow",
    "yes",
    "zero",
]

CLASS_TO_INDEX = {label: index for index, label in enumerate(CLASSES)}
INDEX_TO_CLASS = {index: label for index, label in enumerate(CLASSES)}


def adapter(value):
    if isinstance(value, Real):
        return INDEX_TO_CLASS[int(value)]
    return CLASS_TO_INDEX[value]
