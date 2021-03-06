#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import time
import datetime

from selenium.webdriver.common.by import By
from selenium import webdriver
from base import Base
from page import PageRegion
from home import HomePage

class GithubPage(Base):
    """This Page Object models the Github Issues Page (https://bitgeeky.github.io/bugbin/github)."""

    # The title of this page, which is used by is_the_current_page() in page.py
    _page_title = u'Github Issues'

    # Locators for the home page
    _navbar_locator = (By.ID, 'navbar')
    _issue_table_locator = (By.ID, 'issuetable')

    def go_to_page(self):
        """Open the github page."""
        self.open()

    def click_on_navbar_logo(self):
        self.selenium.find_element(*self._navbar_locator).click()
        from pages.home import HomePage
        return HomePage(self.testsetup)
    
    def check_for_issue_table(self):
        return self.is_element_visible(_issue_table_locator)

