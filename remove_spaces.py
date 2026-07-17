def remove_spaces(text):
    """Remove all spaces from the given string and return the result."""
    return text.replace(" ", "")


if __name__ == "__main__":
    sample = "hello world foo bar"
    print(remove_spaces(sample))  # -> helloworldfoobar
