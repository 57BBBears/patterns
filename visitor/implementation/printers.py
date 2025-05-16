from interfaces.parcel import Parcel, ParcelVisitor


class QRPrinter(ParcelVisitor):
    def visit_letter(self, letter: Parcel):
        print(f"{letter} QR")

    def visit_box(self, box: Parcel):
        print(f"{box} QR")


class LabelPrinter(ParcelVisitor):
    def visit_letter(self, letter: Parcel):
        print(f"{letter} label")

    def visit_box(self, box: Parcel):
        print(f"{box} label")
