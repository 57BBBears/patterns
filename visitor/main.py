from implementation.parcels import Box, Letter
from implementation.posts import StandardPost
from implementation.printers import LabelPrinter, QRPrinter

if __name__ == "__main__":
    box = Box(width=1, length=1, height=1)
    letter = Letter()
    # Single dispatch
    post = StandardPost()
    print("Box price is ", post.calculate_price(box))
    print("Letter price is ", post.calculate_price(letter))
    # Visitor - Double dispatch
    printers = [LabelPrinter(), QRPrinter()]
    for printer in printers:
        box.accept(printer)
        letter.accept(printer)
