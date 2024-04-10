from playwright.sync_api import Page


def test_share_page_loaded(page: Page, home_page, prod_menu_items_page):
    page.goto("")
    home_page.close_cookies_if_visible()
    home_page.products_menu_item.click()
    prod_menu_items_page.doc_email_mgt_nav_item.click()
    prod_menu_items_page.share_submenu_of_doc_email_mgt.click()
