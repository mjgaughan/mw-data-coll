#TODO:
# [x ] split the overall number of contributors by the emails of their commits 
# [ ] add to the json file presented by the AST analysis

from git import Repo

def list_roster(repo_path):
    repo = Repo(repo_path)
    commits = repo.iter_commits()
    bots = {}
    wmf_authors = {}
    volunteers = {}
    for commit in commits:
        #print(commit.tree)
        #added_lines, removed_lines, files_changed = get_diff_count(commit)
        commit_author_info = {"name": commit.author.name, "email":commit.author.email, 'commits': 1, 'added_lines': 0, 'removed_lines': 0, "files_changed": 0}
        if "-bot@" in commit_author_info['email']:
            if commit_author_info['email'] not in bots.keys():
                bots[commit_author_info['email']] = commit_author_info
            else:
                bots[commit_author_info['email']]['commits'] += commit_author_info['commits']
                bots[commit_author_info['email']]['added_lines'] += commit_author_info['added_lines']
                bots[commit_author_info['email']]['removed_lines'] += commit_author_info['removed_lines']
                bots[commit_author_info['email']]['files_changed'] += commit_author_info['files_changed']
        elif "@wikimedia." in commit_author_info['email']:
            if commit_author_info['email'] not in wmf_authors.keys():
                wmf_authors[commit_author_info['email']] = commit_author_info
            else: 
                wmf_authors[commit_author_info['email']]['commits'] += commit_author_info['commits']
                wmf_authors[commit_author_info['email']]['added_lines'] += commit_author_info['added_lines']
                wmf_authors[commit_author_info['email']]['removed_lines'] += commit_author_info['removed_lines']
                wmf_authors[commit_author_info['email']]['files_changed'] += commit_author_info['files_changed']
        else:
            if commit_author_info['email'] not in volunteers.keys():
                volunteers[commit_author_info['email']] = commit_author_info
            else:
                volunteers[commit_author_info['email']]['commits'] += commit_author_info['commits']
                volunteers[commit_author_info['email']]['added_lines'] += commit_author_info['added_lines']
                volunteers[commit_author_info['email']]['removed_lines'] += commit_author_info['removed_lines']
                volunteers[commit_author_info['email']]['files_changed'] += commit_author_info['files_changed']
    print("BOTS: " + str(len(bots)))
    print("ALL CONT: " + str(len(wmf_authors) + len(volunteers)))
    print("WMF: " + str(len(wmf_authors)))
    print("VOLS: " + str(len(volunteers)))
    roster_dict = {'bots': bots, 'wmf_authors':wmf_authors, 'volunteers': volunteers}
    return roster_dict

def get_diff_count(commit):
    diffs = commit.diff(create_patch=True)
    added_lines = 0
    removed_lines = 0
    for diff in diffs:
        diff_lines = diff.diff.decode('utf-8').splitlines()
        for line in diff_lines:
            if line.startswith('+') and not line.startswith('+++'):
                added_lines += 1
            elif line.startswith('-') and not line.startswith('---'):
                removed_lines += 1
    return added_lines, removed_lines, len(diffs)
