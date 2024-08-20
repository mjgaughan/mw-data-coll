import git 
import os
import shutil
from datetime import datetime

def clone_repo(project_name, vcs_link, date):
    temp_dir = '/tmp/' + project_name
    repo = git.Repo.clone_from(vcs_link,
                           temp_dir,
                           branch='master')
    branch_ref = repo.branches['master']
    target_datetime = datetime.strptime(date, '%Y-%m-%d')
    commits = list(repo.iter_commits(branch_ref, until=target_datetime))
    if commits:
        sha = commits[0].hexsha
    repo.git.checkout(sha)
    return temp_dir

def update_checkout(project_directory, date):
    repo = git.Repo(project_directory)
    branch_ref = repo.branches['master']
    target_datetime = datetime.strptime(date, '%Y-%m-%d')
    commits = list(repo.iter_commits(branch_ref, until=target_datetime))
    if commits:
        sha = commits[0].hexsha
    repo.git.checkout(sha)
    return project_directory


def delete_repo(temp_location):
    shutil.rmtree(temp_location)
    #os.rmdir(temp_location)