def math_operations(*args, **kwargs):
    counter = 1
    args = list(args)
    for num in args:
        if counter == 1:
            kwargs["a"] += num
            counter += 1

        elif counter == 2:
            kwargs["s"] -= num
            counter += 1

        elif counter == 3:
            try:
                kwargs["d"] /= num
                counter += 1
            except ZeroDivisionError:
                counter += 1

        elif counter == 4:
            kwargs["m"] *= num
            counter = 1

    return kwargs
