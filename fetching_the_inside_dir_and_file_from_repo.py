from github import Github
import os
# print(os.environ.get("access_token"))
#importing the Github Class from guithub Module 
#now we have to create the github object as 
g=Github(os.environ.get("access_token")) #accessing through the token
my_repo=g.get_user().login

repo=g.get_repo("psarangi550/All-New-Featured-Blog")
def get_all_dir_file():
    repo_content=repo.get_contents("")
    print(repo_content)
    while repo_content:
        repo_all_content=repo_content.pop(0)
        if repo_all_content.content=="dir":
            repo_content.extend(repo.get_contents(repo_all_content))
        else:
            print(repo_all_content)

get_all_dir_file()
        