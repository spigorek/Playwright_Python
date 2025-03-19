import pytest
from playwright.sync_api import Page, expect
from src.web_elem  import Login
from src.web_elem  import Search_Community
import logging
import re
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

@pytest.mark.smoke
class Test_Join_Community:
    def test_join_community(self, login_page: Page): 
        #locator classes initialization
        login_elem = Login() 
        search_elem = Search_Community()
        community_name = "r/eyebleach"
        
        USERNAME = os.getenv("REDDIT_USERNAME")
        PSW = os.getenv("REDDIT_PASSWORD")

        # Login to reddit
        login_page.fill(login_elem.email_locator, USERNAME) # Load the username from the environment variable
        login_page.fill(login_elem.password_locator, PSW) # Load the password from the environment variable    
        login_page.locator(login_elem.login_btn_locator).click() # Click the login button

        # Search for a community
        login_page.fill(search_elem.search_field, community_name) # Fill in the search field
        login_page.locator(search_elem.search_btn).click() # Click the search button
        community_title_join_btn = login_page.locator(search_elem.EyeBleach_btn) # Get the community title locator
        
        # Validate the community title and click join button
        expect(community_title_join_btn).to_be_visible() # Check if the community title is visible
        community_title_join_btn.click() # Click the join button
        time.sleep(5) # wait for the page to load, cause the API request is slow to response
        
        # Class that looks red on the UI
        after_join_class = "option remove active" # Get the class name after joining the community 
        community_title_after_join_btn = login_page.locator(search_elem.EyeBleach_btn_after_join) # Get the community title locator after joining the community
        expect(community_title_after_join_btn).to_be_visible() # Check if the community title is visible
        expect(community_title_after_join_btn).to_have_class(after_join_class) # Check if the class name is the same as the expected class name
        
        # Leave the community or we will have trouble next run        
        community_title_after_join_btn.click() # Click the leave button       
        time.sleep(5) # wait for the page to load, cause the API request is slow to response
        after_leave_class = "option add login-required active" # Get the class name after leaving the community
        expect(community_title_join_btn).to_have_class(after_leave_class) # Check if the class name is the same as the expected class name
        
        logging.info("Test passed successfully")