from playwright.sync_api import Page, expect
import re
from conftest import base_url

class OrdersPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_url = '/wp-admin/admin.php?page=wc-orders'

        # Locators
        self.newest_order_link = page.locator("#the-list tr:first-child .column-order_number a").first

        # User Locators

    def goto(self):
        self.page.goto(base_url+self.page_url)

    def view_order(self):
        expect(self.newest_order_link).to_be_visible()
        self.newest_order_link.click()


    def confirm_order(self):
        return


