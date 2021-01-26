from instagrambot import InstagramBot

CHROME_DRIVER_PATH = "YOUR_DRIVER_PATH_HERE"
SIMILAR_ACCOUNT = "YOUR_TARGET_ACCOUNT_HERE"
USERNAME = "YOUR_INSTAGRAM_USERNAME_HERE"
PASSWORD = "YOUR_INSTAGRAM_PASSWORD_HERE"

INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"

instaBot = InstagramBot(CHROME_DRIVER_PATH)
instaBot.login(INSTAGRAM_URL, USERNAME, PASSWORD)
instaBot.find_followers(SIMILAR_ACCOUNT)
instaBot.follow()
