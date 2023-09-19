from cli.command import Command


def run_exit(args, item_list):
    quit()


exit_command = Command('в', 'в - выход из приложения', run_exit)

