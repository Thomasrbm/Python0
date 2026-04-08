


def NULL_not_found(object: any) -> int:
    x = type(object)
    if object is None:
        print(f"Nothing : {object} {x}")
    elif type(object) is float and object != object:
        print(f"Cheese: {object}  {x}")
    elif type(object) is int and object == 0:
        print(f"Zero: {object} {x}")
    elif type(object) is str and object == "":
        print(f"Empty: {object} {x}")
    elif type(object) is bool and object is False:
        print(f"Fake: {object} {x}")
    else:
        print("Type not Found")
        return 1

    return 1

