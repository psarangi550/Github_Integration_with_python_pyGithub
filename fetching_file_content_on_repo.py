from github import Github
from github.GithubException import UnknownObjectException
import os 
g=Github(base_url='https://api.github.com',login_or_token=os.environ.get('access_token'))
print(g.get_user().login)

repo_name=input("Provide Your repo Name")
file_name=input("Provide File Name")

repo=g.get_repo("psarangi550/{repo_name}".format(repo_name=repo_name))
try:
    content=repo.get_contents(file_name)
except UnknownObjectException as e:
    print("file not present in the directory")
else:
    print(content.name)
    print(content.path)
    print(content)