# run: (args[], item_list) -> None
class Command:
    def __init__(self, name, help, run):
        self.name = name
        self.help = help
        self.run = run

