import os
from playwright.sync_api import Page


class MobilityPage:

    def __init__(self, page: Page) -> None:
        self.page = page
