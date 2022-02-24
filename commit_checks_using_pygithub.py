import github
import os
g=github.Github(os.environ.get('access_token'))
print(g.get_user().login)

repo_name=input("Provide Repo Name")

repo=g.get_repo(repo_name)
commit_hash=input("please provide commit Commit Hash")
commit=repo.get_commit(sha=commit_hash)
print(commit.commit.author.date)#author date
print(commit.commit.committer.date)#committer date
