def filter_strings(strings, to_remove):
    def should_remove(string):
        for item in to_remove:
            if item in string:
                return True
        return False

    return [string for string in strings if not should_remove(string)]
