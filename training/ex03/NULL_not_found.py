def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif type(object) is float:
        print(f"Cheese: {object} {type(object)}")
    elif type(object) is int and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif type(object) is str and object == "":
        print(f"Empty: {type(object)}")
    elif type(object) is bool:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")

    return 1
