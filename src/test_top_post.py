from playwright.sync_api import Page, expect
from src.web_elem  import Login
from src.web_elem  import Top_Post
import logging
import re

class Test_Top_Post:
    def test_top_post(self, login_page: Page):
        #locator classes initialization
        login_elem = Login() 
        top_post = Top_Post()

        # Navigate to Reddit login page
        login_page.fill(login_elem.email_locator, "spigorek@gmail.com")
        login_page.fill(login_elem.password_locator, "I1976oktrambler@")    
        login_page.locator(login_elem.login_btn_locator).click()
       
        # Select TOP tab from Homepage
        login_page.locator(top_post.top_post_tab).click()
        #validate the URL
        expect(login_page).to_have_url(re.compile(".*top"))
        logging.info("TOP tab clicked successfully.")
        
        # Select the first post from the list successfully
        first_article = login_page.locator(top_post.first_article).first
        href = first_article.get_attribute("href")
        logging.info(f"First article href: {href}")
        first_article.first.click()
        href_parts = href.split("/")
        #validate the first article href image is attached to the URL after clicking
        expect(login_page).to_have_url(re.compile(href_parts[-1]))