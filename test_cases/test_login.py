import os
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.admin_dashboard import AdminDashboard

class TestLogin:

    def test_verify_wordpress_login_functionality(self, page: Page):
        # ------------------------------------
        """Verify WordPress Login Functionality"""
        # ------------------------------------

        login = LoginPage(page)
        login.login()

        # Simple validation: admin bar appears
        admin_dashboard = AdminDashboard(page)
        admin_dashboard.is_dashboard_visible()
