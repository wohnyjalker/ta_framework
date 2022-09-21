from os import getenv

from dotenv import load_dotenv


load_dotenv()

# site config
site_url = getenv("SITE_URL")
user_email = getenv("USER_EMAIL")
email_password = getenv("USER_EMAIL_PASSWORD")
site_login_page = (
    "http://automationpractice.com/index.php?controller=authentication&back=my-account"
)

# TA config
browser = getenv("BROWSER", "chrome")
is_remote = getenv("IS_REMOTE")
remote_address = getenv("REMOTE_ADDRESS", "http://selenium-hub:4444/wd/hub")
global_timeout = 15
