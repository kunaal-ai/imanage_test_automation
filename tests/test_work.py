import re
from playwright.sync_api import Page, expect


def test_work_page_loaded(page: Page, goto, home_page, prod_menu_items_page):
    page.wait_for_load_state("domcontentloaded")
    home_page.close_cookies_if_visible()
    home_page.products_from_menu_items.click()
    prod_menu_items_page.doc_email_mgt_nav_item.click()
    prod_menu_items_page.work_submenu_of_doc_email_mgt.click()
    expect(page).to_have_url(re.compile("/.*document-email-management/work/"))


def test_screen1_text_verification(page: Page, goto, prod_doc_email_mgt_subpages):
    work_page = prod_doc_email_mgt_subpages["work_page"]

    page.goto(work_page.page_url("doc_email_mgt", "work"))
    expect(page).to_have_url(re.compile("/.*document-email-management/work/"))

    expect(work_page.secondary_heading_imanage).to_contain_text(
        work_page.page_content("work_screen_01", "secondary_heading_imanage")
    )

    expect(work_page.heading_drive_better_business).to_contain_text(
        work_page.page_content("work_screen_01", "heading_drive_better_business")
    )

    expect(work_page.text_paragraph_imanage_work_enables).to_contain_text(
        work_page.page_content("work_screen_01", "text_paragraph_imanage_work_enables")
    )
    print(work_page.text_paragraph_imanage_work_enables.inner_text())