def merge_dicts(dict1, dict2):
    """Merges two dictionaries"""
    return(dict2.update(dict1))


""" Example code"""
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}


print(Merge(dict1, dict2))

""" changes made in dict2 """
print(dict2) 

