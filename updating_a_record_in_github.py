from github import Github
import os
g=Github(os.environ.get('access_token'))
#authenticating the user
print(g.get_user().login)
print(type(g.get_user()))#authenticated user object

repo_name=input("Enter your github repo name")
file_name=input("Enter file name you want to create on the github repo")
branch=input("Enter branch Name")
message=input("Enter Text into the file")
repo=g.get_repo("psarangi550/{}".format(repo_name))
# print(repo.get_contents(""))
# for file in repo.get_contents(""):
#     if "test.py"==file.name:
#         print("yes")
    # if "test.py" in file.path:
    #     print(file.path)
    # print("f**k off")

for file in repo.get_contents(""):
    if file_name==file.name:
        content=repo.get_contents(file_name,ref=branch)
        repo.update_file(file_name,"update",message,content.sha,branch=branch)