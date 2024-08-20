#TODO:
# [x ] split the overall number of contributors by the emails of their commits 
# [ ] add to the json file presented by the AST analysis
# [ ] (in different file) summarize the report information into CSV form for entire collection?

from git import Repo

def list_roster(repo_path):
    repo = Repo(repo_path)
    commits = repo.iter_commits()
    bots = set()
    wmf_authors = set()
    volunteers = set()
    for commit in commits:
        author_info = {"name": commit.author.name, "email":commit.author.email}
        if "-bot@" in author_info['email']:
            bots.add(author_info['email'])
        elif "@wikimedia.org" in author_info['email']:
            wmf_authors.add(author_info['email'])
        else:
            volunteers.add(author_info['email'])
    print("BOTS: " + str(len(bots)))
    print("ALL CONT: " + str(len(wmf_authors) + len(volunteers)))
    print("WMF: " + str(len(wmf_authors)))
    print("VOLS: " + str(len(volunteers)))
        