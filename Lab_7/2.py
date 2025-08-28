class MenuDesigner:
    def __init__(self):
        self.appetizers = ['rau', 'salad']
        self.beverages = ['nuoc', 'soda', 'sua']
        self.main_courses = ['ca', 'bo', 'ga']
        self.desserts = ['tao', 'kem', 'che']

    def create_menu(self):
        print("Chon khai vi:")
        selected_appetizer = self.ask_choice("Khai vi", self.appetizers)

        print("\nChon do uong:")
        selected_beverage = self.ask_choice("Do uong", self.beverages)

        print("\nChon mon chinh (Neu ban la nguoi an chay, hay chon 'rau', 'ca', hoac 'ga'):")
        selected_main_course = self.ask_choice("Mon chinh", self.main_courses)

        print("\nChon trang mieng:")
        selected_dessert = self.ask_choice("Trang mieng", self.desserts)

        # Kiem tra dieu kien thuc don
        vegetarian_menu = ['rau', 'ca', 'ga']

        if selected_main_course not in vegetarian_menu:
            self.show_message("Chu y: Neu ban la nguoi an chay, ban can chon mon chinh tu rau, ca hoac ga.")

        if selected_beverage == 'sua' or selected_dessert in ['kem', 'che']:
            self.show_message("Thuc don da duoc thiet ke thanh cong!")
            self.show_message(f"Khai vi: {selected_appetizer}")
            self.show_message(f"Do uong: {selected_beverage}")
            self.show_message(f"Mon chinh: {selected_main_course}")
            self.show_message(f"Trang mieng: {selected_dessert}")
        else:
            self.show_message("Thuc don khong hop le: Ban can chon it nhat mot trong cac mon sua, kem hoac che.")

    def ask_choice(self, title, options):
        print(title + ":")
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        choice = int(input(f"Nhap so thu tu {title.lower()} ban chon: ")) - 1
        return options[choice]

    def show_message(self, message):
        print(message)

# Chay chuong trinh
if __name__ == "__main__":
    menu_designer = MenuDesigner()
    menu_designer.create_menu()
