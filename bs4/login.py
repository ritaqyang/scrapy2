import requests

# Define the login URL and credentials
login_url = "https://app.icatalog.cn/web/usermngt/user/tologin?account=true"
payload = {
    "identity": "jltrading1996@gmail.com",
    "password": "123456789"
}

# Start a session
session = requests.Session()

# Log in
response = session.post(login_url, data=payload)
if response.status_code == 200:
    print("Login successful!")

# Access protected pages
protected_url = "https://app.icatalog.cn/web/workbench/product/compropage"
protected_page = session.get(protected_url)

# Process the page content
print(protected_page.text)
