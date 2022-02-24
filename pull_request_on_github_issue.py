import github
import os

g=github.Github(os.environ.get("access_token"))
print(g.get_user().login)
repo_name=input("please provide the repo name")
repo=g.get_repo(f"{repo_name}")
# issue_number=input(" please provide the issue number")
# pull_request_detail=repo.get_pull(int(issue_number))
# print(pull_request_detail)

###o/p####
# psarangi550
# please provide the repo nameCoreyMSchafer/code_snippets
#  please provide the issue number174
# PullRequest(title="using the profile decorator for memory_profiler instead of mem_profil…", number=174)
#####


################################################################
#generating a new pull request
################################################################

# title=input("please enter the title of the pull request")
# body=input("please enter the body of the pull request")
# head=input("from which branch you want to create the pull request")
# base=input("please enter the base branch to create the pull request")
new_pull_rq=repo.create_pull(title="title",body="body",head="main",base="main")
print(new_pull_rq)