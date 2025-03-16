tc_1:
	pytest src/test_tc1.py -m "regression" -v --capture=no --tb=long --headed

tc_2:
	pytest src/test_tc2.py -s -v --capture=no --tb=long --headed --browser chromium

tc_3:
	pytest src/test_tc3.py -v --capture=no --tb=long --headed --browser firefox


tc_1_all:
	pytest src/test_tc1.py --browser chromium --browser firefox --headed

login_top:
	pytest src/test_login.py -v --capture=no --headed 
