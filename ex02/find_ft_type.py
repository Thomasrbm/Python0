# https://stackoverflow.com/questions/2225038/determine-the-type-of-an-object


# special attributes : https://docs.python.org/3/reference/datamodel.html#index-55

# Conditional expressions : https://docs.python.org/3/reference/expressions.html#conditional-expressions

def all_thing_is_obj(object: any) -> int:
    x = type(object)
    print(f"{x.__name__.capitalize()} : {x}" if x.__name__ not in ("int" ,"str") 
    else f"{object} is in the kitchen : {x}"  if x.__name__ == "str" 
    else "Type not found")

    return 42
