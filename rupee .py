#Write a GUI-based program that allows the user to convert Rupees to Euro and vice versa. 【19】
from breezypythongui import EasyFrame

class CurrencyConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="INR to Euro Converter")

        self.addLabel(text="Amount in INR:", row=0, column=0)
        self.inrField = self.addFloatField(value=0.0, row=0, column=1)

        self.addLabel(text="Amount in Euro:", row=1, column=0)
        self.euroField = self.addFloatField(value=0.0, row=1, column=1, state="readonly")

        self.convertButton = self.addButton(text="Convert INR to Euro", row=2, column=0, command=self.convertToEuro)
        self.reverseButton = self.addButton(text="Convert Euro to INR", row=2, column=1, command=self.convertToINR)

    def convertToEuro(self):
        inr = self.inrField.getNumber()
        euro = inr * 0.011  # Example conversion rate
        self.euroField.setNumber(euro)

    def convertToINR(self):
        euro = self.euroField.getNumber()
        inr = euro / 0.011  # Reverse conversion
        self.inrField.setNumber(inr)

if __name__ == "__main__":
    CurrencyConverter().mainloop()

