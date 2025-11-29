from playwright.sync_api import Page, expect
from conftest import base_url

class FlextableDashboard:

    def __init__(self, page: Page):
        self.page = page
        self.page_url = '/wp-admin/admin.php?page=gswpts-dashboard'

        # Locators
        self.button_locator = page.get_by_role("button", name="Create new table")
        self.dashboard_heading = page.get_by_role("heading", name="All Tables")

        self.dashboard_sub_heading = page.locator("text=Manage, create and track all")
        self.dashboard_help_link = page.get_by_role("link", name="Help")
        self.dashboard_upgrade_link = page.get_by_role("link", name="Upgrade", exact=True)

    def goto(self):
        # Navigates To Dashboard
        self.page.goto(base_url+self.page_url)

    def page_fully_loaded(self):
        # Switched to 'networkidle' for better stability on dynamic content, for fully load page
        self.page.goto(base_url+self.page_url, wait_until="networkidle")

    def is_dashboard_visible(self):
        # Checks are chained for clear verification
        expect(self.dashboard_heading).to_be_visible()
        expect(self.dashboard_sub_heading).to_be_visible()
        expect(self.dashboard_help_link).to_be_visible()
        expect(self.dashboard_upgrade_link).to_be_visible()