def sort_by_age(tuples):
    """Sorts a list of tuples by age in ascending order."""
    def key_function(tuple_item):
        return tuple_item[1]
    
    return sorted(tuples, key=key_function) 