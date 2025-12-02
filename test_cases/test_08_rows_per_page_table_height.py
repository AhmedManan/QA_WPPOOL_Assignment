from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.flextable_dashboard import FlextableDashboard
from pages.shortcode_functionality_test_page import ShortcodeFunctionalityTestPage

class TestRowsPerPageTableHeight:

    def test_rows_per_page_table_height(self, page: Page):
        # ------------------------------------
        """Update 'Rows Per Page & Table Height'"""
        # ------------------------------------
        login = LoginPage(page)
        login.login()

        flextable_dashboard = FlextableDashboard(page)
        flextable_dashboard.goto()
        flextable_dashboard.navigate_to_table_customization_table_rows_height()

        shortcode_page = ShortcodeFunctionalityTestPage(page)
        shortcode_page.goto()
        shortcode_page.check_table_exist()