import os
from playwright.sync_api import Page


class DrivePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        
