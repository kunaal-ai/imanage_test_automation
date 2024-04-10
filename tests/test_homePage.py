""" Test for Home Page only
"""

import re
from playwright.sync_api import Page, expect

def test_home_page_loaded(page: Page):
    """confirmation if home page loaded sucessfully before running following test cases

    Args:
        page (Page):page context
    """
    page.goto('')
    expect(page).to_have_title(re.compile("iManage"))


def test_site_header_main_menu_items_clickable(page: Page, home_page):
    """Verify - if main header items are clickable - no page confirmation

    Args:
        page (Page): page context
        home_page (fixture): Home page new context object
    """
    page.goto('')
    home_page.close_cookies_if_visible()
    home_page.products_menu_item.click()
    home_page.industry_department_menu_item.click()
    home_page.resources_menu_item.click()
    home_page.about_menu_item.click()
