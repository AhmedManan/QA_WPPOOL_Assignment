from playwright.sync_api import Page, expect

from conftest import base_url, admin_username, admin_password


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.url = base_url
        self.username = admin_username
        self.password = admin_password

    def open_login(self, url):
        self.page.goto(url+'/wp-login.php')

    def enter_username(self, username):
        self.page.fill('#user_login', username)

    def enter_password(self, password):
        self.page.fill('#user_pass', password)

    def click_login(self):
        self.page.click('#wp-submit')

    def login(self):
        self.open_login(self.url)
        self.enter_username(self.username)
        self.enter_password(self.password)
        self.click_login()
