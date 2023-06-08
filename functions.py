def ask(options, prompt='Please choose one from above: ', reask_prompt='Error choice. Please choose again: '):
    """Ask the player to choose one option from a series of options

    :param options:The options to be chosen
    :param prompt:The prompt to be shown when asking occurs
    :param reask_prompt:The prompt to be shown when re-asking occurs
    :return:The index of the chosen option
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
