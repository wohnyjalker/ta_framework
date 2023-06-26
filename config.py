from os import getenv

from dotenv import load_dotenv

load_dotenv()

# site config
site_url = getenv("SITE_URL")
site_login_page = f"{site_url}/customer/account/login"
user_email = getenv("USER_EMAIL")
email_password = getenv("USER_EMAIL_PASSWORD")
user_first_name = getenv("USER_NAME")
user_last_name = getenv("USER_LAST_NAME")

# TA config
browser = getenv("BROWSER", "chrome")
is_remote = getenv("IS_REMOTE", "")
remote_address = getenv("REMOTE_ADDRESS", "http://selenium-hub:4444/wd/hub")
global_timeout = 15
