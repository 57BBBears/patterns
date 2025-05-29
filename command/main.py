from implementation.command import (
    DrawCommand,
    MacroCommand,
    SimplePrintCommand,
    TextCommand,
)
from implementation.layout import Layout, Shape
from implementation.menu import MenuItem

if __name__ == "__main__":
    print_command = SimplePrintCommand()
    print_item = MenuItem(print_command)

    layout = Layout("Wellcome!")

    text_command = TextCommand(layout)
    text_item = MenuItem(text_command)
    draw_command = DrawCommand(layout)
    draw_item = MenuItem(draw_command)

    print("Menu:")
    menu = (print_item, text_item, draw_item)
    for item in menu:
        item.click()

    macro_command = MacroCommand()
    macro_command.add(print_command).add(text_command).add(draw_command)
    macro_command.remove(print_command)  # removes
    macro_command.remove(macro_command)  # does nothing
    macro_item = MenuItem(macro_command)
    layout.current_element = Shape.STAR

    print("Macro:")
    macro_item.click()
