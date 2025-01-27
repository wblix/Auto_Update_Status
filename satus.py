import time
from github import Github

# Replace with your GitHub token
GITHUB_TOKEN = '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'

# Initialize GitHub instance
g = Github(GITHUB_TOKEN)

# List of statuses to cycle through
statuses = ["Free Malone", "Carti drop please", "RIP kingvon"]

def update_status(status):
    user = g.get_user()
    user.edit(bio=status)
    print(f"Status updated to: {status}")

while True:
    for status in statuses:
        update_status(status)
        time.sleep(120)  # Wait for 2 minutes
