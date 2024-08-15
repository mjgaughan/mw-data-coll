import download_repo
import run_metrics
import roster_demo

def main(project_name, project_vcs, commit_hash):
    clone_location = download_repo.clone_repo(project_name, project_vcs, commit_hash)
    roster_demo.list_roster(clone_location)
    run_metrics.run_ast_metrics(clone_location, commit_hash)
    download_repo.delete_repo(clone_location)

if __name__ == "__main__":
    #main("Echo", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/Echo", "d9aef933bb2f580fb646f33c131b559b3cec1552")
    main("ConfirmEdit", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/ConfirmEdit", "2a09d9fa2390ec2d18fff8b9a5af742818e68a31")
    #main("AbuseFilter", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/AbuseFilter", "ad732457f02053cb30feef369e88dca215a5b073")
    #main("OAuth", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/OAuth", "b820d2ad1361c240b7b5c3e8e5e9691f4b98f50a")
    #main("CheckUser", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/CheckUser", "a3443da5504e660687b9363ff47c09b27d51b7ca")