def get_int(value):
    try:
        result = int(value)
        return result
    except ValueError:
        return