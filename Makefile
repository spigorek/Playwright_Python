tc_1_demo:
	pytest src/test_reddit_register.py -s -v -m "regression" --capture=no --tb=long --headed
tc_2:
	pytest src/test_top_post.py -s -m "regression" -v --capture=no --tb=long --headed --browser chromium
tc_3:
	pytest src/test_join_community.py -s -m "smoke" -v --capture=no --tb=long --headed --browser chromium
	

all:
	pytest src/ -s -m "regression or smoke" -v --capture=no --tb=long --headed --browser chromium 