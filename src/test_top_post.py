import pytest
from playwright.sync_api import Page, expect
from src.web_elem  import Login
from src.web_elem  import Top_Post
import logging
import re
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@pytest.mark.regression
class Test_Top_Post:
    def test_top_post(self, login_page: Page):
        
        #locator classes initialization
        login_elem = Login() 
        top_post = Top_Post()

        # Navigate to Reddit login page
        USERNAME = os.getenv("REDDIT_USERNAME") # Load the username from the environment variable
        PSW = os.getenv("REDDIT_PASSWORD") # Load the password from the environment variable
        
        login_page.fill(login_elem.email_locator, USERNAME) 
        login_page.fill(login_elem.password_locator, PSW)    
        login_page.locator(login_elem.login_btn_locator).click()
        
        # Select TOP tab from Homepage
        login_page.locator(top_post.top_post_tab).click()
        #validate the URL
        expect(login_page).to_have_url(re.compile(".*top"))
        logging.info("TOP tab clicked successfully.")
        
        # Select the first post from the list successfully
        first_article = login_page.locator(top_post.first_article).first # get the first post
        href = first_article.get_attribute("href") # get the href attribute of the first post
        logging.info(f"First article href: {href}") 
        first_article.first.click() # click the first post
        href_parts = href.split("/") # split the href to get the last part
        
        expect(login_page).to_have_url(re.compile(href_parts[-1])) #validate the first article href image is attached to the URL after clicking

        logging.info("Test passed successfully")