from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.flextable_dashboard import FlextableDashboard

class TestFlextableDashboard:


    def test_navigate_to_flextable_dashboard(self, page: Page):
        # ------------------------------------
        """Navigate to FlexTable Dashboard"""
        # ------------------------------------

        # First Perform Login
        login = LoginPage(page)
        login.login()


        # Navigate to Flextable page
        flextable_dashboard = FlextableDashboard(page)
        flextable_dashboard.page_fully_loaded()

        flextable_dashboard.is_dashboard_visible()
        flextable_dashboard.is_dashboard_visible()