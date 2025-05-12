

---

## ✅ `scraper_preview.py`

This is a lightweight preview to share publicly:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Instagram login
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("your_username")
driver.find_element(By.NAME, "password").send_keys("your_password" + Keys.ENTER)
time.sleep(10)

# Sample Bing search
query = 'site:instagram.com "fitness coach" "email"'
driver.get(f"https://www.bing.com/search?q={query}")
time.sleep(5)

# Extract links (example)
links = driver.find_elements(By.CSS_SELECTOR, "div.b_tpcn a.tilk")
for link in links:
    print(link.get_attribute("href"))

driver.quit()
