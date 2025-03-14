tc_2:
	pytest src/test_tc2.py --browser chromium --headed

tc_1:
	pytest src/test_tc1.py -v --capture=no --tb=long --headed 

tc_1_all:
	pytest src/test_tc1.py --browser chromium --browser firefox --headed

login_top:
	pytest src/test_login.py -v --capture=no --headed 
