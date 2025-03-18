from playwright.sync_api import Page, expect
from src.web_elem  import Login
from src.web_elem  import Search_Community
import logging
import re
import time

class Test_Join_Community:
    def test_join_community(self, login_page: Page):
        #locator classes initialization
        login_elem = Login() 
        search_elem = Search_Community()
        community_name = "r/eyebleach"

        # Navigate to Reddit login page
        login_page.fill(login_elem.email_locator, "spigorek@gmail.com")
        login_page.fill(login_elem.password_locator, "I1976oktrambler@")    
        login_page.locator(login_elem.login_btn_locator).click()

        # Search for a community
        login_page.fill(search_elem.search_field, community_name)
        login_page.locator(search_elem.search_btn).click()
        community_title_join_btn = login_page.locator(search_elem.EyeBleach_btn)
        
        #validate the community title and click join button
        expect(community_title_join_btn).to_be_visible()
        community_title_join_btn.click()
        time.sleep(5) # wait for the page to load, cuz the API is slow to response
        #class that looks red on the UI
        after_join_class = "option remove active" 
        community_title_after_join_btn = login_page.locator(search_elem.EyeBleach_btn_after_join)
        expect(community_title_after_join_btn).to_be_visible()
        expect(community_title_after_join_btn).to_have_class(after_join_class)
        
        # Leave the community or we will have trouble next run        
        community_title_after_join_btn.click()        
        time.sleep(5)# wait for the page to load, cuz the API is slow to response
        after_leave_class = "option add login-required active"
        expect(community_title_join_btn).to_have_class(after_leave_class)
        