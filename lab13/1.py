class LowerUp:
    def __init__(self):
        self.text = ""

    def get_input(self):
        self.text = input("Введіть рядок: ")

    def print(self):
        print(self.text.upper())

lower_up = LowerUp()
lower_up.get_input()
lower_up.print()
