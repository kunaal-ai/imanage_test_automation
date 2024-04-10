import os
from playwright.sync_api import Page


class ProdMenuItemsPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.doc_email_mgt_nav_item = page.get_by_role("button", name="Document & Email Management")
        self.work_submenu_of_doc_email_mgt = page.get_by_role("link", name="Work Protect information while driving productivity")
        self.share_submenu_of_doc_email_mgt = page.get_by_role("button", name="Shre")
        self.drive_submenu_of_doc_email_mgt = page.get_by_role("button", name="Drive")
        self.mobility_submenu_of_doc_email_mgt = page.get_by_role("button", name="Mobility")
        
        