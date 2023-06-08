def ask(options, prompt='Please choose one from above: ', reask_prompt='Error choice. Please choose again: '):
    """

    :param options:
    :param prompt:
    :param reask_prompt:
    :return:
    """
    choice = None
    for i, option in enumerate(options):
        print(str(i + 1) + '. ' + option)

    while True:
        reask = False
        try:
            choice = int(input(prompt))

            if choice <= 0 or choice > len(options):
                reask = True
        except ValueError:
            reask = True

        if not reask:
            break

        prompt = reask_prompt

    return choice - 1
