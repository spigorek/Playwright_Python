tc_1:
    pytest src/test_reddit_register.py -m "regression" -v --capture=no --tb=long --headed

tc_2:   
    pytest src/test_top_post.py -s -v --capture=no --tb=long --headed --browser chromium

tc_3:
    pytest src/test_join_community.py -v --capture=no --tb=long --headed --browser chromium