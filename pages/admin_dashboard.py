from playwright.sync_api import Page, expect

from conftest import base_url


class AdminDashboard:

    def __init__(self, page:Page):
        self.page = page
        self.admin_dashboard_url="/wp-admin"

    def goto(self):
        # Admin Dashboard URL
        self.page.goto(base_url+self.admin_dashboard_url)

    def is_dashboard_visible(self):
        # Check Dashboard Widgets Wrap Visibility
        return self.page.locator("#dashboard-widgets-wrap").is_visible()

    def navigate_to_plugins(self):
        # Navigate To Plugin Page
        self.page.click("#menu-plugins a")
        self.page.wait_for_url("**/wp-admin/plugins.php")