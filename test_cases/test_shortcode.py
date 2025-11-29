from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.flextable_dashboard import FlextableDashboard
from pages.shortcode_functionality_test_page import ShortcodeFunctionalityTestPage

class TestShortcode:

    def test_shortcode(self, page: Page):
        # ------------------------------------
        """Verify Table Display Using Shortcode"""
        # ------------------------------------

        # First Perform Login
        login = LoginPage(page)
        login.login()

        flextable_dashboard = FlextableDashboard(page)
        shortcode = flextable_dashboard.copy_shortcode()

        shortcode_page = ShortcodeFunctionalityTestPage(page)

        page_is_missing = shortcode_page.page_not_exists()

        if page_is_missing:
            shortcode_page.create_page()
            shortcode_page.create_shortcode(shortcode)
            shortcode_page.goto()
        else:
            shortcode_page.create_shortcode(shortcode)
            shortcode_page.goto()

