class Registration:
    def __init__(self):
        ############### Sign Up page ####################
        self.continie_btn_locator_sign_up_page = "button:has-text('Continue')"
        self.email_field_locator_sign_up_page = "input[name='email']"

        ############### VERIFY YOUR EMAIL PAGE ####################
        self.skip_btn_name_verify_email_page = 'Skip'
        
        ############### CREATE YOUR USERNAME AND PASSWORD PAGE ####################
        self.psw_field_create_locator_your_usr_psw_page = "input[name='password']"
        self.continue_btn_locator_create_your_usr_psw_page = "#register button.create.button-large"
        
        ############### ABOUT YOU PAGE ####################
        self.skip_btn_name_about_you_page = 'Skip'

        ############### INTERESTS PAGE ####################
        self.first_interest_locator_interests_page = '#topics > fieldset:nth-child(1) > div.flex > div.topic-container:nth-child(1)'
        self.continue_btn_locator_interest_page = "button:has-text('Continue')"