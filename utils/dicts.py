def get_val(collection, key, default='default value'):
    if key not in collection:
        return default
    return collection[key]