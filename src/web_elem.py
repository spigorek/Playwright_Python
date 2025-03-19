class Login:
    def __init__(self):
        self.email_locator = "input[name='username']"
        self.password_locator = "input[name='password']"
        self.login_btn_locator = "button:has-text('Log in')"
       
class Top_Post:
    def __init__(self):
        self.top_post_tab = "a[class='choice']:has-text('top')"
        self.first_article = "[class='top-matter'] a"

class Search_Community:
    def __init__(self):
        self.search_field = "input[name='q']"
        self.search_btn = "[type='submit']"
        self.EyeBleach_title = "a[href='https://ww.reddit.com/r/Eyebleach/']"
        self.EyeBleach_btn = "[data-sr_name='Eyebleach'] a:has-text('join')"
        self.EyeBleach_btn_after_join = "[data-sr_name='Eyebleach'] a:has-text('leave')"

class  Registration:
    def __init__(self):
        self.continie_btn_locator_sign_up_page = "button:has-text('Continue')"
        self.email_field_locator_sign_up_page = "input[name='email']"

        self.skip_btn_name_verify_email_page = 'Skip'
        
        self.psw_field_create_locator_your_usr_psw_page = "input[name='password']"
        self.continue_btn_locator_create_your_usr_psw_page = "#register button.create.button-large"
        
        self.skip_btn_name_about_you_page = 'Skip'

        self.first_interest_locator_interests_page = '#topics > fieldset:nth-child(1) > div.flex > div.topic-container:nth-child(1)'
        self.continue_btn_locator_interest_page = "button:has-text('Continue')"