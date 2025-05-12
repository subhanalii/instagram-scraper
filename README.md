# 🔍 Instagram Email Scraper (Bing + Selenium)

This is a Python-based web automation script that:

- Logs into Instagram using your credentials
- Uses Bing to search public Instagram profiles of fitness coaches with emails
- Extracts public details from profiles like name, bio, posts, followers, and following
- Searches bios for public email addresses
- Saves results to a CSV file

## 📽️ Demo
> 📌 Watch it in action below 👇 > *(Full source code available upon request — email me at [isubhanali3@gmail.com](mailto:isubhanali3@gmail.com) or contact me on [Upwork](https://www.upwork.com/freelancers/~01b6c1b6819be875f2?mp_source=share))*
![Demo](assets/demo.gif)

---

## ⚙️ Features

✅ Logs in to Instagram  
✅ Bing search automation with pagination  
✅ Profile scraping (Name, Bio, Posts, Followers, Following)  
✅ Email detection from bio  
✅ CSV export

---

## 📋 Sample Code

```python
# Bing search for Instagram profiles
query = 'site:instagram.com "fitness coach" "email"'
search_url = f"https://www.bing.com/search?q={query}"
driver.get(search_url)

# Login to Instagram
driver.get("https://www.instagram.com/accounts/login/")
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys("your_username")
password_input.send_keys("your_password")
password_input.send_keys(Keys.ENTER)
