class CoffeeMachine:

    def __init__(self, water_: int, milk_: int, coffee_beans_: int, disposable_cups_: int, money_: int, exit_: bool):
        self.water = water_
        self.milk = milk_
        self.coffee_beans = coffee_beans_
        self.disposable_cups = disposable_cups_
        self.money = money_
        self.actual_state = 0
        # 0 - choosing option, 1 - printing ingredient to add, 2 - adding ingredient
        # 3 - print with coffee to serve, 4 - serve coffee , 5 - back to options
        self.added_ingredients = 0  # status in order of added ingredient
        self.exit = exit_

    def check_resources(self, water_c, milk_c, coffee_beans_c, disposable_cups_c) -> bool:
        """
        Checking coffee machine if it has enough resources to server coffee
        :param water_c: int
        :param milk_c: int
        :param coffee_beans_c:int
        :param disposable_cups_c:int
        :return: bool
        """
        if self.water < water_c:
            print("Sorry, not enough water!")
            return False
        elif self.milk < milk_c:
            print("Sorry, not enough milk!")
            return False
        elif self.coffee_beans < coffee_beans_c:
            print("Sorry, not enough coffee beans!")
            return False
        elif self.disposable_cups < disposable_cups_c:
            print("Sorry, not enough disposable cups!")
            return False
        else:
            return True

    def choose_option(self, option) -> None:
        """
        Main menu
        """
        if option == "buy":
            self.actual_state = 3
            self.serve_coffee(option)
        elif option == "fill":
            self.actual_state = 1
            self.print_ingredient_to_add()
        elif option == "take":
            self.take_money()
        elif option == "remaining":
            self.print_eq()
        elif option == "exit":
            self.on_off_machine()
        else:
            print("I don't know that command")
            self.print_menu()

    def fill_coffee_machine(self, option_) -> None:
        """
        Fill coffee machine
        """
        option = int(option_)
        if self.added_ingredients == 0:
            self.water += option
            self.added_ingredients += 1
            self.print_ingredient_to_add()
        elif self.added_ingredients == 1:
            self.milk += option
            self.added_ingredients += 1
            self.print_ingredient_to_add()
        elif self.added_ingredients == 2:
            self.coffee_beans += option
            self.added_ingredients += 1
            self.print_ingredient_to_add()
        elif self.added_ingredients == 3:
            self.disposable_cups += option
            self.added_ingredients = 0
            self.print_menu()
            self.actual_state = 0
        else:
            self.added_ingredients = 0
            self.print_menu()
            self.actual_state = 0

    def on_off_machine(self):
        """
        Switching state of the machine
        """
        if not self.exit:
            self.exit = True
        else:
            self.exit = False

    def operate(self, user_input: str):
        """
        Main operate function changing state of machine, and passing input
        """
        if self.actual_state == 0:
            self.choose_option(user_input)
        elif self.actual_state == 1:
            self.print_ingredient_to_add()
        elif self.actual_state == 2:
            self.fill_coffee_machine(user_input)
        elif self.actual_state == 3 or 4:
            self.serve_coffee(user_input)
        else:
            self.actual_state = 0

    @staticmethod
    def print_choose_coffee():
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

    def print_eq(self) -> None:
        print(f"""The coffee machine has:
    {self.water}, of water
    {self.milk}, of milk
    {self.coffee_beans}, of coffee beans
    {self.disposable_cups}, of disposable cups
    {self.money}, of money""")
        self.print_menu()

    def print_ingredient_to_add(self):
        if self.added_ingredients == 0:
            print("Write how many ml of water do you want to add:")
        elif self.added_ingredients == 1:
            print("Write how many ml of milk do you want to add:")
        elif self.added_ingredients == 2:
            print("Write how many grams of coffee beans do you want to add:")
        elif self.added_ingredients == 3:
            print("Write how many disposable cups of coffee do you want to add:")
        else:
            print("Unknown error in 'print_ingredient_add'")
        self.actual_state = 2

    @staticmethod
    def print_menu():
        print("Write action (buy, fill, take, remaining, exit):")

    def serve_coffee(self, coffee_t_) -> None:

        if self.actual_state == 3:
            self.print_choose_coffee()
            self.actual_state = 4

        elif self.actual_state == 4:
            if coffee_t_ == "back":
                self.actual_state = 0
                self.print_menu()
            else:
                coffee_t = int(coffee_t_)
                cups = 1  # temporary
                if coffee_t == 1:  # espresso
                    if self.check_resources(250, 0, 16, cups):
                        print("I have enough resources, making you a coffee!")
                        self.water -= 250 * cups
                        self.coffee_beans -= 16 * cups
                        self.disposable_cups -= 1
                        self.money += 4
                        self.print_menu()
                        self.actual_state = 0
                    else:
                        self.print_menu()
                        self.actual_state = 0
                elif coffee_t == 2:  # latte
                    if self.check_resources(350, 75, 20, cups):
                        print("I have enough resources, making you a coffee!")
                        self.water -= 350 * cups
                        self.milk -= 75 * cups
                        self.coffee_beans -= 20 * cups
                        self.money += 7
                        self.disposable_cups -= 1
                        self.print_menu()
                        self.actual_state = 0
                    else:
                        self.print_menu()
                        self.actual_state = 0
                elif coffee_t == 3:  # cappuccino
                    if self.check_resources(200, 100, 12, cups):
                        print("I have enough resources, making you a coffee!")
                        self.water -= 200 * cups
                        self.milk -= 100 * cups
                        self.coffee_beans -= 12 * cups
                        self.money += 6
                        self.disposable_cups -= 1
                        self.print_menu()
                        self.actual_state = 0
                    else:
                        self.print_menu()
                        self.actual_state = 0
                else:
                    print("No such coffee")
                    self.print_menu()
                    self.actual_state = 0

    def take_money(self):
        print("I gave you", self.money)
        self.money = 0
        self.print_menu()


coffee_m = CoffeeMachine(400, 540, 120, 9, 550, False)

print("Write action (buy, fill, take, remaining, exit):")
while not coffee_m.exit:
    u_input = input()
    coffee_m.operate(u_input)
