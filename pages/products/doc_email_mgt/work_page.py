import json
from playwright.sync_api import Page


class WorkPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.secondary_heading_imanage = page.locator('#site-content')
        self.heading_drive_better_business = page.locator('h1')
        #self.text_paragraph_imanage_work_enables = page.locator('#site-content')
        self.text_paragraph_imanage_work_enables = page.get_by_text("iManage Work enables every organization to")

    def page_content(self, i, j):
        with open("app_contents.json") as f:
            pc = json.load(f)
            return pc[i][0][j]
    
    def page_url(self, i, j):
        with open("page_url.json") as f:
            url_data = json.load(f)
            return url_data[i][0][j]
