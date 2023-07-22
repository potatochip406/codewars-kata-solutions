import re


def to_camel_case(text):
    new_text = re.split("[-_]", text)

    final_string = new_text[0]
    for x in range(1, len(new_text)):
        final_string += new_text[x].capitalize()

    return final_string
