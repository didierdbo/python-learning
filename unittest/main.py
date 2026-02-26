def do_stuff(num: int = 0):
    try:
        if num:
            return int(num) + 5
        else:
            return "please enter number"
    except ValueError as err:
        return err
