from interfaces.protocol import Command


class MenuItem:
    """Command invoker."""

    def __init__(self, command: Command):
        self.command = command

    def click(self):
        self.command.execute()
