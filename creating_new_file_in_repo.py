from github import Github
import os
g=Github(os.environ.get('access_token'))
#authenticating the user
print(g.get_user().login)
print(type(g.get_user()))#authenticated user object

#now here creating a new_file in the repo
repo_name=input("Enter your github repo name")
file_name=input("Enter file name you want to create on the github repo")
branch=input("Enter branch Name")
message=input("Enter Text into the file")
repo=g.get_repo("psarangi550/{}".format(repo_name))
repo.create_file(file_name,message="testing_commit",content=message,branch=branch)
print("file created successfully")