from github import Github
import os
# g=Github(os.environ.get("access_token"))
g=Github(base_url="https://api.github.com",login_or_token=os.environ.get("git_other_token"))
print(g.get_user())
user=g.get_user()
print(user.login)