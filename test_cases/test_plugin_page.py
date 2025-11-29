from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.plugin_page import PluginPage

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

        # --- Check Status and Toggle Logic ---

        if plugin_page.activate_plugin_link.is_visible():
            print("Plugin is Inactive. Activating...")
            # Use the corrected method name
            plugin_page.activate_plugin()

            # If the 'Deactivate' link is visible, the plugin is ACTIVE. We must DEACTIVATE it.
        # Uses the corrected attribute name 'deactivate_link'
        elif plugin_page.deactivate_plugin_link.is_visible():
            print("Plugin is Active. Deactivating...")
            # Use the corrected method name
            plugin_page.deactivate_plugin()

        # If neither link is visible, the plugin may not be present on the page.
        else:
            print("Plugin status links not found. Attempting to upload...")
            plugin_page.upload_plugin()
            # Ideally, you'd add steps here to check visibility and activate after upload

