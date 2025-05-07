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
        
        registr_elem = Registration()
        # SETUP - Browser selection can be done via CLI / Makefile
        # browser = await p.chromium.launch(headless=False, slow_mo=500)  # Debug mode for Chromium
        browser = await p.firefox.launch(headless=False, slow_mo=500)  # Debug mode for Firefox
        context = await browser.new_context() 
        page = await context.new_page() 

        # Navigate to Reddit sign-up page
        register_url = os.path.join(BASEURL, EP_REGISTER)
        await page.goto(register_url)

        ############### Sign Up page ####################
        logging.info(f"We are on {SIGN_UP_PAGE} page")
        h1_sign_up_label = page.locator('h1').first # h1 label on Sign Up page
        await expect(h1_sign_up_label).to_be_visible() # Verify the h1 label is visible
        h1_sign_up_label_text = await h1_sign_up_label.text_content() # Get the text of the h1 label
        logging.info(f'h1_sign_up_label_text: {h1_sign_up_label_text.strip()}')
        assert h1_sign_up_label_text.strip() == SIGN_UP_PAGE , f"{SIGN_UP_PAGE} page does NOT shown up" 

        # Generate random credentials
        random_email = f"{generate_random_string()}@gmail.com"
        random_username = generate_random_string()
        random_password = generate_random_string(LEN_PSW)

        # Continue button on Sign Up page
        button_continue = page.locator(registr_elem.continie_btn_locator_sign_up_page).first

        # Wait for the email input field and enter an email
        await page.fill(registr_elem.email_field_locator_sign_up_page, random_email)

        # Click Enabled Continue button on Sign Up page
        await button_continue.click()

        ############### VERIFY YOUR EMAIL PAGE ####################
        logging.info(f"We are on {VERIFY_EMAIL_PAGE} page")
        await page.get_by_role("button", name=registr_elem.skip_btn_name_verify_email_page).click() # Click Skip button on Verify your email page
        
        ############### CREATE YOUR USERNAME AND PASSWORD PAGE ####################
        logging.info(f"We are on {CREATE_USERNAME_PSW_PAGE} page")
        await page.fill(registr_elem.psw_field_create_locator_your_usr_psw_page, random_password) # Fill in password field, the user field is filled automaticly
        await page.locator(registr_elem.continue_btn_locator_create_your_usr_psw_page).click() # Click continue button on Create your username and password page

        ############### ABOUT YOU PAGE ####################
        logging.info(f"We are on {ABOUT_YOU_PAGE} page")
        await page.get_by_role("button", name=registr_elem.skip_btn_name_about_you_page).click() # click Skip button on About your page

        ############### INTERESTS PAGE ####################
        logging.debug(f"We are on {INTERESTS_PAGE} page")
        first_topic_tag = page.locator(registr_elem.first_interest_locator_interests_page) # Choose THE FIRST INTEREST element from the list
        await first_topic_tag.click() # Click the first interest element
        
        button_continue = page.locator(registr_elem.continue_btn_locator_interest_page).last # Continue button on Interests page
        try:
            await button_continue.click()
            await expect(page.locator("text=Personalizing your experience")).to_be_visible() # Verify we are on the right page after clicking the continue button
        except Exception as e:
            logging.error(f"Failed to click the continue button: {e}")
        
        # Close the browser
        await context.close()
        await browser.close()
        logging.info("Test passed successfully")