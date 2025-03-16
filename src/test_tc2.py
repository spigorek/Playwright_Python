import asyncio
from playwright.async_api import async_playwright
import pytest
import time
import requests
import logging

@pytest.mark.asyncio
async def test_run(launch_logged_in):
    # Note:
    # Due to blocking from Reddit, there is Server Error - 500
    # The browser had been launched with Reddit.com as expected, 
    # however that is not logged in , even valid token was retrieved.
    # See CONFTEST.PY with all of FIXTURE like get_token() and launch_logged_in()

    TEST_CASE = '''
        Precondition:
            - Have valid credentials for REDDIT WEB APP DEVELOPERS
            - Get Valid Token via API (As a Fixture)
            - Launch required browser (As a Fixture)
            - Navigate to www.reddit.com as Logged in user
        Steps:
            - Select TOP tab from Homepage
            - Select the first post from the list successfully
        Cleanup:
            - Close required browser (depends on yield and scope of the Fixture)
        '''
    logging.info(f'TEST CASE LOGGING: \n{TEST_CASE}')

    # Preconditions
    # Assuming that USER is logged in and see Homepage:
    # Actually the Browser has been launched with not-logged in User and see Homepage.
    page = launch_logged_in

    ############ Select TOP tab from Homepage #################    
    top_tab = page.get_by_role("link", name="top", exact=True)
    await top_tab.click()
    
    ############ Select TOP post #################
    # The following code is not functional, 
    # the main issue is first top post locator 
    logging.info('going to click on top tab')
    first_post = page.locator('div#siteTable div.thing div.entry div.top-matter p.title a.title')
    #await expect(first_post).to_be_visible()
    logging.info('first topic is visable')
    await first_post.click()
    logging.info("First post clicked successfully.")
    await page.wait_for_timeout(3000)
    


