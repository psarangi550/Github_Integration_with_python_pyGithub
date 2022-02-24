import github
from github.GithubException import GithubException
import os
g=github.Github(os.environ.get('access_token'))
print(g.get_user().login)

#fetching all the branched present in an repo by get_branches() on get_user() Authenticated object

repo_name=input("please provide the repo name")
repo=g.get_repo(f"psarangi550/{repo_name}")

# all_branches=repo.get_branches()

# print(all_branches)#<github.PaginatedList.PaginatedList object at 0x7fee7d146e50> object

# for branch in all_branches:
#     print(branch.name)#fetching the branch name

#for a perticular branch if we want to fetch then
branch_name=input("please provide Branch Name")
# try:
#     spec_branch=repo.get_branch(branch_name)
# except GithubException as e:
#     print("Branch %s not found" % branch_name)
# else:
#     print(spec_branch.name)#fetching the branch name

#fetching the commits on a branch 

# branch=repo.get_branch(branch_name)
# last_commit=branch.commit
# print(last_commit)#this will display the commit # thats been mase on the last

#fetch the branch is protected or not 

branch=repo.get_branch(branch_name)
print(branch.protected)#True/False
#using the get_required_status_check() to check the status of the branch
try:
    print(branch.get_required_status_checks())
except GithubException:
    print(f"branch {branch_name} is not protected")
    



