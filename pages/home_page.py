import os
from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.accept_all_cookies = page.get_by_role("button", name="Accept All Cookies")
        self.products_from_menu_items = page.get_by_role("link", name="Products")
        self.industry_department_menu_item = page.get_by_role("link", name="Industry & Department")
        self.resources_menu_item = page.get_by_role("link", name="Resources", exact=True)
        self.about_menu_item = page.get_by_role("link", name="About")


    def close_cookies_if_visible(self):
        if self.accept_all_cookies.is_visible():
            self.accept_all_cookies.click()