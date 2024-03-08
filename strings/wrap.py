
def wrap(string, max_width):
    wrapped_string = textwrap.wrap(string, max_width)
    return '\n'.join(wrapped_string)
