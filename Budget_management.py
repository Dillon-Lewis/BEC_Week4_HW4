#Problem Statement: You are required to build a Personal Budget Management application. The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

class BudgetCatagory():
    def __init__(self, Name, category, alloted_budget):
        self.Name = Name
        self.category = category
        self.__alloted_budget = alloted_budget
    
    def set_budget(self, bigger_budget):
        self.__alloted_budget = bigger_budget

    def get_budget(self):
        return self.__alloted_budget

    def new_budget(self):
        change_budget = input("Would you like to ADD or SUBTRACT from your budget:\n").upper()
        if change_budget == "ADD":
            amount_add = int(input("How much would you like to add: \n"))           
            self.set_budget(self.get_budget() + amount_add)
            print(f'{self.Name} can now spend {self.get_budget()} on {self.category}.')
        elif change_budget == "SUBTRACT":
            amount_sub = int(input("How much would you like to take off:\n"))
            self.set_budget(self.get_budget() - amount_sub)
            print(f'{self.Name} can now spend {self.get_budget()} on {self.category}.')

    def get_info(self):
        print(f"{self.Name} has {self.__alloted_budget}$ to spend on {self.category}.")

Johnny = BudgetCatagory('Johnny', 'Groceries', 50)
Ben = BudgetCatagory('Ben', 'Date Night', 100)
Dan = BudgetCatagory('Dan', 'Car Parts', 1200)

print(Johnny.get_info())
print(Johnny.new_budget())
print(Johnny.get_info())

# print(Ben.get_info())
# print(Ben.new_budget())
# print(Ben.get_info())

# print(Ben.get_info())
# print(Ben.new_budget())
# print(Ben.get_info())

