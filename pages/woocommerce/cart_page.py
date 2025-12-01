import re
from playwright.sync_api import Page, expect
from conftest import base_url

class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_url = '/cart'

        # Locators
        self.proceed_to_checkout_button = page.get_by_role("link", name="Proceed to Checkout")
        # self.cart_total_locator = page.locator('//span[contains(@class, "wc-block-components-totals-footer-item-tax-value")]')
        self.cart_total_locator = page.locator("xpath=/html/body/div[4]/div/div/div/main/article/div/div[4]/div[3]/div[1]/div[3]/div/div[1]/span")

    def goto(self):
        self.page.goto(base_url+self.page_url)

    def proceed_to_checkout(self):
        expect(self.proceed_to_checkout_button).to_be_visible()
        self.proceed_to_checkout_button.click()

    def get_cart_total_amount(self) -> float:
        # Fetches the total amount from the cart, cleans it

        # Wait for the element to be visible and stable
        expect(self.cart_total_locator).to_be_visible()

        # Extract the raw text content
        raw_text = self.cart_total_locator.text_content()

        cleaned_text = re.sub(r'[^\d.]', '', raw_text)

        try:
            # Convert the cleaned string to a float
            total_amount = float(cleaned_text)
            return total_amount
        except ValueError:
            print(f"Error: Could not convert '{raw_text}' to a number.")
            return 0.0

