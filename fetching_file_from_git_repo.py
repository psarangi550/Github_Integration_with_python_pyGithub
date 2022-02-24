from github import Github
import os
# print(os.environ.get("access_token"))
#importing the Github Class from guithub Module 
#now we have to create the github object as 
g=Github(os.environ.get("access_token")) #accessing through the token
my_repo=g.get_user().login

repo=g.get_repo("psarangi550/WFMTDB-SQLPLSQL-BINDS")
print(dir(repo))
repo_content=repo.get_contents("")
print(repo_content)
for content in repo_content:
    # print(content.name)
    # print(content.path)
    print(content)
# print(repo_content)
