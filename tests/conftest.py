import pytest
import os
from typing import Generator
from playwright.sync_api import Browser, BrowserContext, Page

# --- CONFIGURACIÓN DE RUTAS ---
AUTH_FILE = "auth_state.json"

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,  
    }

@pytest.fixture(scope="session")
def session_context(browser: Browser) -> Generator[BrowserContext, None, None]:
    if os.path.exists(AUTH_FILE):
        context = browser.new_context(storage_state=AUTH_FILE)
    else:
        context = browser.new_context()
    
    yield context
    context.close()

@pytest.fixture
def page(session_context: BrowserContext) -> Generator[Page, None, None]:
    page = session_context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="function")
def save_auth_state():
    def _save(page: Page):
        page.context.storage_state(path=AUTH_FILE)
    return _save

# --- HOOKS DE REPORTE Y CAPTURAS ---

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=screenshot_path)
            print(f"\n[ERROR] Captura guardada en: {screenshot_path}")