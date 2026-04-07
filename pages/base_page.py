from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 5000

    def navigate_to(self, url: str):
        self.page.goto(url, wait_until="networkidle")
    
    def get_locator(self, selector: str) -> Locator:
        
        strategies = {
            "text=": self.page.get_by_text,
            "label=": self.page.get_by_label,
            "placeholder=": self.page.get_by_placeholder,
            "alt=": self.page.get_by_alt_text,
            "title=": self.page.get_by_title,
            "test_id=": self.page.get_by_test_id
        }
        
        found_method = None
        clean_selector = selector

        for prefix, method in strategies.items():
            if selector.startswith(prefix):
                found_method = method
                clean_selector = selector.replace(prefix, "", 1)
                break

        if found_method:
            locator = found_method(clean_selector)
        else:
            locator = self.page.locator(selector)

        locator.wait_for(state="visible", timeout=self.timeout)
        
        return locator

    def click_element(self, selector: str):
        self.get_locator(selector).click()

    def fill_input(self, selector: str, text: str):
        element = self.get_locator(selector)
        element.fill(text)