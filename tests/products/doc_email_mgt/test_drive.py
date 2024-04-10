from playwright.sync_api import Page, expect


def test_drive_page_loaded(
    page: Page, home_page, prod_menu_items_page, prod_doc_email_mgt_subpages
):
    # work_page = prod_doc_email_mgt_subpages["work_page"]
    page.goto('')
    home_page.close_cookies_if_visible()
    home_page.products_menu_item.click()
    prod_menu_items_page.doc_email_mgt_nav_item.click()
    prod_menu_items_page.drive_submenu_of_doc_email_mgt.click()
