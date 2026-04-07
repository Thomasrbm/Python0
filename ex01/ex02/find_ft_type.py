# https://stackoverflow.com/questions/2225038/determine-the-type-of-an-object


# special attributes : https://docs.python.org/3/reference/datamodel.html#index-55


def all_thing_is_obj(object: any) -> int:
    x = type(object)
    print(x)


    return 42
