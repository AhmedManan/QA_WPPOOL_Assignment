import os
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.plugin_page import PluginPage
# from pages.admin_dashboard import AdminDashboard

class TestPluginPage:

    def test_flextable_plugin_activation_status(self, page: Page):
        # ------------------------------------
        """Verify FlexTable Plugin Activation Status"""
        # ------------------------------------

        login = LoginPage(page)
        login.login()

        # Simple validation: admin bar appears
        plugin_page = PluginPage(page)
        plugin_page.goto()

        if plugin_page.is_plugin_visible():

            if plugin_page.activate_plugin_link.is_visible():
                plugin_page.deactivate_plugin()
            elif plugin_page.deactivate_plugin_link.is_visible():
                plugin_page.activate_plugin()

        else:
            plugin_page.upload_plugin()

