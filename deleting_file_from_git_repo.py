from github import Github
import os
g=Github(os.environ.get('access_token'))
#authenticating the user
print(g.get_user().login)
print(type(g.get_user()))#authenticated user object

repo_name=input("Enter your github repo name")
file_name=input("Enter file name you want to create on the github repo")
branch=input("Enter branch Name")
# message=input("Enter Text into the file")

repo=g.get_repo(f"psarangi550/{repo_name}")

for file in repo.get_contents(""):
    if file_name==file.name:
        content=repo.get_contents(file_name,ref=branch)
        repo.delete_file(file_name,"deleted",content.sha,branch=branch)
        