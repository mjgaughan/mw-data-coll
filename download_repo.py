import git 
import os
import shutil

def clone_repo(project_name, vcs_link, commit_hash):
    temp_dir = '/tmp/' + project_name
    repo = git.Repo.clone_from(vcs_link,
                           temp_dir,
                           branch='master')
    repo.git.checkout(commit_hash)
    return temp_dir

def delete_repo(temp_location):
    shutil.rmtree(temp_location)
    #os.rmdir(temp_location)