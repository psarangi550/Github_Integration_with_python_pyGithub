from github import Github
import os
# print(os.environ.get("access_token"))
#importing the Github Class from guithub Module 
#now we have to create the github object as 
g=Github(os.environ.get("access_token")) #accessing through the token
#this provide the username of the user thats been logged in 
# print(g.get_user().login)
#for the outside user we can use get_user() as 
outer_user=g.get_user("CoreyMSchafer")
# print(outer_user.login)
#fetching out the repos from me first
all_repos_pratik=g.get_user().get_repos()
#fetching out the repo name
for repo in all_repos_pratik:
    print(repo.name)
#accessing all the repo of corey 
# for repo in outer_user.get_repos():
#     print(repo.name)
#searching for a particular repo
# repo=g.search_repositories(query="WFMTDB-SQLPLSQL-BINDS")
# print(type(repo))
# for item in repo:
#     print(item.name)

#searching for a particular repo from others 
# repo=g.search_repositories(query="CoreyMS-Genesis-Theme")
# print(type(repo))
# for item in repo:
#     print(item.name)

