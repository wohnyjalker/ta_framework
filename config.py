from os import getenv

# site config
site_url = getenv("SITE_URL", "http://automationpractice.com")
user_email = getenv("USER_EMAIL", "asddsa@asd.asd")
email_password = getenv("USER_EMAIL_PASSWORD", "asdasdasd")
site_login_page = "http://automationpractice.com/index.php?controller=authentication&back=my-account"

# TA config
global_timeout = 15
