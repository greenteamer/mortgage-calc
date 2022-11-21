def take_input(data_name, sign="", hint=""):
    value = 0
    hint_text = "({})".format(hint) if hint != "" else hint
    prompt = "* Type {name}{hint}: {sign}".format(
        name=data_name, hint=hint_text, sign=sign
    )
    while value == 0:
        try:
            value = int(input(prompt))
        except ValueError:
            print("{} should be a number".format(data_name.title()))
    return value
