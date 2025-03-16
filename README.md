# install python 
python version minimum 3.12

# install playwright
pip install playwright 

# install browsers
playwright install

# how to run all test in Pytest folder using chromium and firefox browsers
pytest --headed --browser chromium --browser firefox
__________________________________________________ OLD ____________________

# Shell
install apps: 
Install WSL (Ubuntu)

# Create a Virtual Environment:
python3 -m venv <name of virtual env>
example: `python3 -m venv venv_linux`

# Activate the Virtual Environment:
Run: <name of virtual env>\Scripts\activate
Linux: source <name of virtual env>/bin/activate
example: `source venv_linux/bin/activate`

# Deactivate existing virtual env in the current folder:
Run: deactivate
example`pip freeze > requirements.txt`
example `pip install -r requirements.txt`

# create .env file, it must be in root of framework
REDDIT_USERNAME=<user/email>
REDDIT_PASSWORD=<password>
APP_USERNAME=<your_Username_for_REDDIT_App> e.g. https://ww.reddit.com/prefs/apps/ (not your email)
PYTHONPATH=<your_current_work_directory> e.g. /mnt/c/workspace/Playwright_Python
CLIENT_ID=<your_CLIENT_ID_for_REDDIT_App> e.g. https://ww.reddit.com/prefs/apps/
CLIENT_SECRET=<your_CLIENT_SECRET_for_REDDIT_App> e.g. https://ww.reddit.com/prefs/apps/
APP_PASSWORD=<your_APP_PASSWORD_for_REDDIT_App> e.g. https://ww.reddit.com/prefs/apps/
USER_AGENT=<your USER AGENT>

# check installed dependencies list 
Run: `pip list`

# chrominium install
`playwright install`
# edge install
`playwright install msedge`

# addition dependencies (linux)
`sudo apt-get install libnss3 libnspr4 libasound2t64`

# run tests
(root framework dir) `make <target>`
example: `make test_case1`

trigger test cases by Markers:
Based on Markers in pytest.ini file.
Update Makefile, 
Example before changes:
    test_case1:
        pytest src/test_tc1.py -v --capture=no --tb=long --headed
Example after changes:
    test_case1: 
        pytest src/test_tc1.py -m "regression" -v --capture=no --tb=long --headed
Run:
`make test_case1`
