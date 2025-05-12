# iinstagram-scraper-tutorial
A Python automation tool that logs into Instagram, searches profiles via Bing, scrapes public data like bio, followers, and emails, and saves the results. Demo included. Full script available on request.

# 🔍 Instagram Email Scraper (Bing + Selenium)

This is a Python-based automation tool that:

- Logs into Instagram
- Uses Bing to search fitness coaches with emails
- Scrapes public profile data (name, bio, followers, etc.)
- Extracts emails from bio (if present)

## 📽️ Demo

> 📌 Watch it in action below 👇  
> *(Full source code available upon request — email me on [Gmail](isubhanali3@gmail.com) or [Upwork](https://www.upwork.com/freelancers/~01b6c1b6819be875f2?mp_source=share))*  

![Demo](assets/demo.gif)

## 📋 Features

- Login automation using Selenium
- Bing search pagination handling
- Instagram profile parsing
- Email detection in bios
- CSV export of collected data

## 📂 Sample Code

Here’s a small part of the full script:

```python
driver.get("https://www.instagram.com/accounts/login/")
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys("your_username")
password_input.send_keys("your_password")
