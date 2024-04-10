import os
from playwright.sync_api import Page


class SharePage:

    def __init__(self, page: Page) -> None:
        self.page = page
