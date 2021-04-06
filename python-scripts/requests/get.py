import requests

# API request to Gitlab
response = requests.get("https://api.github.com/users/kumarr4794/repos")
my_repos = response.json()
print(my_repos)