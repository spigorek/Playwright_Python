# install python 
python version minimum 3.12

# install playwright
pip install playwright 

# install browsers
playwright install

# Terminal
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

# check installed dependencies list 
Run: `pip list`

# chrominium install
`playwright install`

# run tests
(root framework dir) `make <target>`
example: `make tc_1`

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
