from implementation.layout import Layout
from interfaces.protocol import Command


class SimplePrintCommand(Command):
    def execute(self):
        print("Executed.")


class LayoutCommand:
    def __init__(self, layout: Layout):
        self.layout = layout


class DrawCommand(LayoutCommand):
    def execute(self):
        self.layout.draw()


class TextCommand(LayoutCommand):
    def execute(self):
        self.layout.text()


class MacroCommand:
    def __init__(self):
        self._commands: list[Command] = []

    def add(self, command: Command):
        self._commands.append(command)

        return self  # allows chain call i.e. .add().add()

    def remove(self, command: Command):
        try:
            self._commands.remove(command)
        except ValueError:
            ...

    def execute(self):
        for cmd in self._commands:
            cmd.execute()
