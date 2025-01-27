# Auto GitHub Status Updater

This script allows you to automatically cycle through different GitHub status messages using the [GitHub API](https://docs.github.com/en/rest). The status is updated every 2 minutes, giving you a dynamic and fun way to change your profile bio on GitHub.

### 🛠️ **How it Works**

1. **GitHub Token**: The script authenticates using your personal GitHub token, which gives it access to edit your profile information.
2. **Status Cycle**: The script cycles through a list of predefined statuses (`"Status 1"`, `"Status 2"`, and `"Status 3"`) and updates your profile bio accordingly.
3. **Time Delay**: The status is updated every 2 minutes, creating a continuous loop of fun messages.

---
###  **Code Overview**

```python
import time
from github import Github

# Replace with your GitHub token
GITHUB_TOKEN = 'your_github_token_here'

# Initialize GitHub instance
g = Github(GITHUB_TOKEN)

# List of statuses to cycle through
statuses = ["Status 1", "Status 2", "Status 3"]

def update_status(status):
    user = g.get_user()
    user.edit(bio=status)
    print(f"Status updated to: {status}")

while True:
    for status in statuses:
        update_status(status)
        time.sleep(120)  # Wait for 2 minutes
