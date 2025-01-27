import time
from github import Github

#change to your token
GITHUB_TOKEN = 'UR_GITHUB_TOKEN'

g = Github(GITHUB_TOKEN)

statuses = ["Status 1", "Status 2", "Status 3"]

def update_status(status):
    user = g.get_user()
    user.edit(bio=status)
    print(f"Status updated to: {status}")

while True:
    for status in statuses:
        update_status(status)
        time.sleep(120)  # change time
