# ==========================================================
# Month 7 - Day 24
# Python Networking & REST APIs
#
# Topics Covered:
# 1. HTTP GET Request
# 2. HTTP POST Request
# 3. JSON Handling
# 4. API Authentication (Headers)
# 5. Error Handling
# 6. Downloading Data from API
# ==========================================================

import requests
import json

print("=" * 60)
print("1. HTTP GET REQUEST")
print("=" * 60)

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("Title :", data["title"])
    print("Body  :", data["body"])


print("\n" + "=" * 60)
print("2. HTTP POST REQUEST")
print("=" * 60)

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Python",
    "body": "Learning REST APIs",
    "userId": 1
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)

print("Response:")

print(response.json())


print("\n" + "=" * 60)
print("3. JSON HANDLING")
print("=" * 60)

student = {
    "name": "Vikhyath",
    "age": 20,
    "branch": "CSE"
}

json_string = json.dumps(student, indent=4)

print("Dictionary → JSON")
print(json_string)

python_object = json.loads(json_string)

print("\nJSON → Dictionary")
print(python_object)


print("\n" + "=" * 60)
print("4. API AUTHENTICATION (HEADERS)")
print("=" * 60)

headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Accept": "application/json"
}

print("Sample Headers:")

for key, value in headers.items():
    print(key, ":", value)


print("\n" + "=" * 60)
print("5. ERROR HANDLING")
print("=" * 60)

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/10000",
        timeout=5
    )

    response.raise_for_status()

    print(response.json())

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.ConnectionError:
    print("Connection Failed")

except requests.exceptions.Timeout:
    print("Request Timed Out")

except requests.exceptions.RequestException as e:
    print("Request Error:", e)


print("\n" + "=" * 60)
print("6. DOWNLOADING DATA FROM API")
print("=" * 60)

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:

    users = response.json()

    print("User List:\n")

    for user in users:
        print(f"Name  : {user['name']}")
        print(f"Email : {user['email']}")
        print(f"City  : {user['address']['city']}")
        print("-" * 40)


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ REST API

REST = Representational State Transfer

Used for communication
between applications.

--------------------------------------------------

✔ HTTP Methods

GET
→ Read Data

POST
→ Create Data

PUT
→ Update Entire Resource

PATCH
→ Partial Update

DELETE
→ Delete Resource

--------------------------------------------------

✔ requests Module

Install

pip install requests

Import

import requests

--------------------------------------------------

✔ GET Request

response = requests.get(url)

--------------------------------------------------

✔ POST Request

response = requests.post(url, json=data)

--------------------------------------------------

✔ JSON

Dictionary → JSON

json.dumps()

JSON → Dictionary

json.loads()

--------------------------------------------------

✔ Authentication

Common Header

Authorization

Bearer TOKEN

--------------------------------------------------

✔ Common Status Codes

200 OK

201 Created

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

500 Server Error

--------------------------------------------------

✔ Error Handling

try

except

response.raise_for_status()

--------------------------------------------------

Interview Tip

Most Asked Questions

✔ REST API

✔ HTTP Methods

✔ JSON

✔ API Authentication

✔ requests Module

✔ Status Codes

✔ Exception Handling
""")