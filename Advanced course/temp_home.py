def merge(dict_in):
    # result = {k : v for k, v in dict_in.items()}
    result = {}
    for i in dict_in:
        for k, v in i.items():
            # result.setdefault(k, '').join(str(v))
            result[k] = result.get(k, '') + str(v)
    return result

print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))