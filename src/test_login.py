import pytest
import asyncio
from playwright.async_api import async_playwright
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")

# Single self-contained test
@pytest.mark.asyncio
async def test_login_and_select_top_post():
    """Test login to Reddit and select the top post."""
    
    # Skip if no credentials
    if not REDDIT_USERNAME or not REDDIT_PASSWORD:
        pytest.skip("Reddit credentials not provided")
    
    # Setup playwright and browser
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        try:
            # Navigate to Reddit
            await page.goto("https://www.reddit.com/")
            
            # Handle cookie banner if present
            try:
                await page.click("button:has-text('Accept all')", timeout=5000)
                print("Accepted cookies")
            except:
                print("No cookie banner found")
            
            
            # Click login button
            await page.click("button:has-text('Log In')")
            

            
            
            # Get the login iframe
            login_frame = page.frame_locator("xpath=//iframe[contains(@src, 'https://www.reddit.com/login')]")
            
            # Fill login form
            await login_frame.locator("input[name='username']").fill(REDDIT_USERNAME)
            await login_frame.locator("input[name='password']").fill(REDDIT_PASSWORD)
            await login_frame.locator("button[type='login']").click()
            

            # Wait for login to complete
            await page.wait_for_selector("button[aria-label='Open user menu']")
            await page.wait_for_selector("button[aria-label='Open user menu']")
            print("Successfully logged in")
        

            # Go to top posts
            await page.goto("https://www.reddit.com/r/all/top/")
            
            # Wait for posts to load
            await page.wait_for_selector("div[data-testid='post-container']")
            
            # Select first post
            first_post = page.locator("div[data-testid='post-container']").first
            post_title = await first_post.locator("h3").text_content()
            print(f"Selected top post: {post_title}")
            
            # Click on post
            await first_post.click()
            
            # Verify we're on the post page
            current_url = page.url
            assert "/comments/" in current_url, f"Expected to be on post page, but URL was {current_url}"
            
            # Try to logout
            try:
                await page.click("button[aria-label='Open user menu']")
                await page.click("text=Log Out")
                await page.click("button:has-text('Log Out')")  # Confirm logout
                print("Successfully logged out")
            except:
                print("Logout failed or already logged out")
                
        finally:
            # Always clean up
            await context.close()
            await browser.close()