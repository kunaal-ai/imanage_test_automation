"""Fixtures"""

import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.products.prod_menu_items_page import ProdMenuItemsPage

from pages.products.doc_email_mgt import (
    drive_page,
    mobility_page,
    share_page,
    work_page,
)

@pytest.fixture(scope="function")
def goto(page: Page):
    page.goto('')

@pytest.fixture(scope="function")
def home_page(page: Page):
    return HomePage(page)


@pytest.fixture(scope="function")
def prod_menu_items_page(page: Page):
    return ProdMenuItemsPage(page)


@pytest.fixture(scope="function")
def prod_doc_email_mgt_subpages(page: Page):
    return {
        "drive_page": drive_page.DrivePage(page),
        "mobility_page": mobility_page.MobilityPage(page),
        "share_page": share_page.SharePage(page),
        "work_page": work_page.WorkPage(page),
    }
