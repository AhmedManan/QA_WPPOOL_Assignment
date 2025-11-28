from playwright.sync_api import Page, expect
from conftest import base_url

class PluginPage:

    def __init__(self, page:Page):
        self.page = page
        self.plugin_page_url= f'{base_url}/wp-admin/plugins.php'
        self.test_plugin_name = 'FlexTable'
        self.test_plugin_locator= page.get_by_role("checkbox", name=f"Select {self.test_plugin_name}")
        self.deactivate_plugin_link = page.get_by_role("link", name="Deactivate FlexTable")
        self.skip_deactivate_plugin_popup = page.get_by_role("link", name="Skip & Deactivate")
        self.activate_plugin_link = page.get_by_role("link", name="Activate FlexTable")

    def goto(self):
        # Plugin Page URL
        self.page.goto(self.plugin_page_url)

    def is_plugin_visible(self):
        # Check Plugin Visibility
        expect(self.test_plugin_locator).to_be_visible()

    def deactivate_plugin(self):
        if self.deactivate_plugin_link.is_visible():
            # Navigate To Plugin Page
            self.deactivate_plugin_link.click()
            self.skip_deactivate_plugin_popup.click()

    def activate_plugin(self):
        if self.activate_plugin_link.is_visible():
            self.activate_plugin_link.click()

    def upload_plugin(self):
        self.plugin_page_url= f'{base_url}/wp-admin/plugin-install.php'
        self.page.get_by_role("button", name="Plugin zip file").click()