import pandas as pd
import numpy as np
import requests

# Task 1
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent" : "TrendPulse/1.0"}

# Pulling Story IDs through API
try:
  response = requests.get(url, headers = headers)
  response.raise_for_status()
  print(response.status_code)
  if response.status_code == 200:
    story_IDs = response.json()
    print(type(story_IDs))
except requests.exceptions.ConnectionError:
  print("Connection Error")
except requests.exceptions.HTTPError as e:
  print(f"HTTP Error: {e}")
except requests.exceptions.Timeout:
  print("Time Out")

# Print Story ID data, length and type
story_IDs = story_IDs[0:500]
print(len(story_IDs))
print(story_IDs)

#Store the Story data of first 500 Story IDs
result = []   # Empty list
for i in range(len(story_IDs)):   # loop through id count i.e. 500
  url2 = f"https://hacker-news.firebaseio.com/v0/item/{story_IDs[i]}.json"  # Id changes for every loop and pulls that id's data
  try:
    response2 = requests.get(url2, headers = headers, timeout = 2)
    response2.raise_for_status()
    # print(f"Id {i}: response code is {response2.status_code}.")
    if response2.status_code == 200:    #If pull request is success then it saves the data into 'result' list
      data = response2.json()
      result.append(data)
  except requests.exceptions.ConnectionError:
    print(f"Id {i}: Connection Error")
  except requests.exceptions.HTTPError as e:
    print(f"ID {i}: HTTP Error '{e}'")
  except requests.exceptions.Timeout:
    print(f"Id {i}: Time Out")
#   time.sleep(2)

print(result)
print(len(result))
print(type(result))