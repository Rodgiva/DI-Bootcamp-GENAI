from menu_manager import MenuManager

def load_manager()->MenuManager:
    return MenuManager()

def show_user_menu(menu_manager:MenuManager):
    menu = menu_manager.menu
    for k,v in menu.items():
        print()

