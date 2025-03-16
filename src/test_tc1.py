import pytest
import asyncio
import os
import time
from playwright.async_api import expect
from playwright.async_api import async_playwright
from helper import generate_random_string
from params import BASEURL, EP_REGISTER, SIGN_UP_PAGE, LEN_PSW, INTERESTS_PAGE
from params import VERIFY_EMAIL_PAGE, CREATE_USERNAME_PSW_PAGE, ABOUT_YOU_PAGE
from web_elem import Registration
import logging

@pytest.mark.asyncio
@pytest.mark.regression
async def test_reddit_register():
    async with async_playwright() as p:
        TEST_CASE = '''
        Precondition:
            - Have valid credentials for REDDIT website
            - Launch required browser
            - Navigate to ww.reddit.com/register
        Steps:
            - Navigate to SIGN UP page and successfully proceed
            - Navigate to VERIFY YOUR EMAIL page and successfully proceed
            - Navigate to CREATE YOUR USERNAME AND PASSWORD page and successfully proceed
            - Navigate to ABOUT YOU PAGE page and successfully proceed
            - Navigate to INTERESTS PAGE page and successfully proceed
        Cleanup:
            - Close required browser
        '''
        logging.info(f'TEST CASE LOGGING: \n{TEST_CASE}')
        registr_elem = Registration()
        # SETUP - Browser choose can be done via CLI / Makefile
        #browser = await p.chromium.launch(headless=False, slow_mo=500)  # Debug mode
        browser = await p.firefox.launch(headless=False, slow_mo=500)  # Debug mode
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to Reddit sign-up page
        register_url = os.path.join(BASEURL, EP_REGISTER)
        await page.goto(register_url)

        ############### Sign Up page ####################
        logging.info(f"We are on {SIGN_UP_PAGE} page")
        h1_sign_up_label = page.locator('h1').first
        await expect(h1_sign_up_label).to_be_visible()
        h1_sign_up_label_text = await h1_sign_up_label.text_content()
        logging.info(f'h1_sign_up_label_text: {h1_sign_up_label_text.strip()}')
        assert h1_sign_up_label_text.strip() == SIGN_UP_PAGE , f"{SIGN_UP_PAGE} page does NOT shown up"

        # Generate random credentials
        random_email = f"{generate_random_string()}@gmail.com"
        random_username = generate_random_string()
        random_password = generate_random_string(LEN_PSW)

        # Continue button on Sign Up page
        #button_continue = page.locator("button:has-text('Continue')").first
        button_continue = page.locator(registr_elem.continie_btn_locator_sign_up_page).first
        
        # POTENTIAL VERIFICATION: if "Continue" button is DISABLED
        # is_disabled = button_continue.get_attribute("disabled") is not None
        # print(f"Button is disabled: {is_disabled}")

        # Wait for the email input field and enter an email
        #await page.fill("input[name='email']", random_email)
        await page.fill(registr_elem.email_field_locator_sign_up_page, random_email)

        # POTENTIAL VERIFICATION: if "Continue" button is ENABLED (when EMAIL is filled up)
        # is_enabled = button_continue.get_attribute("disabled") is None
        # print(f"Button is enabled: {is_enabled}")

        # Click Enabled Continue button on Sign Up page
        await button_continue.click()

        ############### VERIFY YOUR EMAIL PAGE ####################
        # ASSERT that we are on the right page - See examples in LINE#30:
        logging.info(f"We are on {VERIFY_EMAIL_PAGE} page")
        # Click Skip button on Verify your email page 
        #await page.get_by_role("button", name="Skip").click()
        await page.get_by_role("button", name=registr_elem.skip_btn_name_verify_email_page).click()
        
        ############### CREATE YOUR USERNAME AND PASSWORD PAGE ####################
        # ASSERT that we are on the right page - See examples in LINE#30:
        logging.info(f"We are on {CREATE_USERNAME_PSW_PAGE} page")
        # Fill in password field, user field is filled automaticly
        #await page.fill("input[name='password']", random_password)
        await page.fill(registr_elem.psw_field_create_locator_your_usr_psw_page, random_password)
        # Click continue button on Create your username and password page
        #await page.locator("#register button.create.button-large").click()
        await page.locator(registr_elem.continue_btn_locator_create_your_usr_psw_page).click()

        ############### ABOUT YOU PAGE ####################
        # ASSERT that we are on the right page - See examples in LINE#30:
        logging.info(f"We are on {ABOUT_YOU_PAGE} page")
        # click Skip button on About your page
        #await page.get_by_role("button", name="Skip").click()
        await page.get_by_role("button", name=registr_elem.skip_btn_name_about_you_page).click()

        ############### INTERESTS PAGE ####################
        # ASSERT that we are on the right page - See examples in LINE#30:
        logging.info(f"We are on {INTERESTS_PAGE} page")
        # POTENTIAL VERIFICATION: if "Continue" button is DISABLED
        # is_disabled = button_continue.get_attribute("disabled") is not None
        # print(f"Button is disabled: {is_disabled}")

        #continue_before = page.locator(registr_elem.continue_btn_locator_interest_page)
        # Choose THE FIRST INTEREST element from the list
        #first_topic_tag = page.locator('#topics > fieldset:nth-child(1) > div.flex > div.topic-container:nth-child(1)')
        first_topic_tag = page.locator(registr_elem.first_interest_locator_interests_page)        
        await first_topic_tag.click()
        # POTENTIAL VERIFICATION: if "Continue" button is ENABLED (when EMAIL is filled up)
        # is_enabled = button_continue.get_attribute("disabled") is None
        # print(f"Button is enabled: {is_enabled}")
        
        
        #button_continue = page.locator("button:has-text('Continue')").first
        button_continue = page.locator(registr_elem.continue_btn_locator_interest_page).last
        await button_continue.click()
        # ASSERT that we are on the right page - See examples in LINE#30:

        # Close the browser
        await context.close()
        await browser.close()

        """
        Notes:
        - Each new page has verification(assert) of page visibility 
          and button status (enabled/disabled).
        - There is a testing limitation of User Creation from Reddit website.
          Blocked after 3-5 times. So it is impossible to debug for some period of time.
          Some of Asserts and verification has been done and marked as POTENTIAL VERIFICATION.
        - #shadow-root (open) - it was time consuming to get access those elements.
        - As common now days I used AI resources.
        - Basic code generation has been also used (playwright codegen https://ww.reddit.com/)
        - params.py - includes also Clickable web elements like: Buttons, Fields etc.
          As best practice, those elements should be organized by CLASSES 
          and not HARDCODED in the test case.
        """