class Menu:
    def __init__(self, text, drink=False):
        self.text = text
        self.drink = drink
        self.yes = None
        self.no = None


class ExpertSuggestor:
    def __init__(self, raiz):
        self.root = raiz

    def suggest(self, step=None):
        if step is None:
            step = self.root

        if step.drink:
            print()
            print(f"Suggest choice: {step.text}!")
            return

        answer = input(f"{step.text} (yes/s or no/n): ").strip().lower()

        if answer == "yes" or answer == "s":
            self.suggest(step.yes)
        elif answer == "no" or answer == "n":
            self.suggest(step.no)

    def showTree(self, step=None, level=0):
        if step is None:
            step = self.root

        indent = "    " * level
        if step.drink:
            print(f"{indent} Drink: {step.text}")
        else:
            print(f"{indent} {step.text}")
            if step.yes:
                print(f"{indent}  [Yes] branches to:")
                self.showTree(step.yes, level + 1)
            if step.no:
                print(f"{indent}  [No] branches to:")
                self.showTree(step.no, level + 1)

    def drinksCount(self, step=None):
        if step is None:
            step = self.root

        if step.drink:
            return 1

        total = 0
        if step.yes:
            total += self.drinksCount(step.yes)
        if step.no:
            total += self.drinksCount(step.no)

        return total


def menuTree():
    raiz = Menu("Do you want an alcoholic drink?")

    raiz.yes = Menu("Do you mention something refreshing?")
    raiz.yes.yes = Menu("Lime Caipirinha", drink=True)
    raiz.yes.no = Menu("Dry red wine", drink=True)

    raiz.no = Menu("Do you prefer a hot drink?")
    raiz.no.yes = Menu("Coffee", drink=True)
    raiz.no.no = Menu("Orange juice", drink=True)

    return raiz


def main():
    raiz = menuTree()
    menu = ExpertSuggestor(raiz)

    print("Menu Tree:")
    menu.showTree()

    print(f"\nAll drinks available: {menu.drinksCount()}")

    print("\nService counter:")
    menu.suggest()


if __name__ == "__main__":
    main()
