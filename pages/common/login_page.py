from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "placeholder=usuario@consultorio.com"
        self.password_input = "placeholder=••••••••"
        self.login_button = "text=Iniciar sesión"
        self.user_profile_icon = "#radix-\:r0\:"

    def login_to_application(self, user, password):
        self.fill_input(self.username_input, user)
        self.fill_input(self.password_input, password)
        self.click_element(self.login_button)
        print(self.get_locator(self.user_profile_icon))
        self.get_locator(self.user_profile_icon).wait_for(state="visible")