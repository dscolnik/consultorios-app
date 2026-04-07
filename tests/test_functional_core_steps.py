from pytest_bdd import scenarios, given, when, then
from pages.common.login_page import LoginPage

scenarios('../features/functional_core.feature')

@given("the user navigates to the login page")
def navigate_to_login(page):
    login_page = LoginPage(page)
    login_page.navigate_to("https://consultoriook.vercel.app/")

@when("the user enters valid credentials")
def enter_credentials(page):
    login_page = LoginPage(page)
    login_page.login_to_application("superadmin@consultorio.app", "SuperAdmin1234!")

@then("the user should be redirected to the dashboard")
def verify_dashboard(page):
    assert "/consultorios" in page.url

@then("the session state is saved")
def save_session(page, save_auth_state):
    save_auth_state(page)