import download_repo
import run_metrics
import roster_demo

def main(project_name, project_vcs, first_date, second_date):
    clone_location = download_repo.clone_repo(project_name, project_vcs, first_date)
    #run for first date we're looking at
    print(first_date)
    roster_demo.list_roster(clone_location)
    run_metrics.run_ast_metrics(clone_location, first_date)
    #switch over and run for second date that we're looking at
    '''
    print(second_date)
    download_repo.update_checkout(clone_location, second_date)
    roster_demo.list_roster(clone_location)
    run_metrics.run_ast_metrics(clone_location, second_date)
    '''
    #clean up
    download_repo.delete_repo(clone_location)
    print("all pau with " + project_name)

if __name__ == "__main__":
    #main("Echo", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/Echo", "d9aef933bb2f580fb646f33c131b559b3cec1552")
    main("ConfirmEdit", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/ConfirmEdit", "2022-07-01",  "2024-08-01")
    #main("AbuseFilter", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/AbuseFilter", "ad732457f02053cb30feef369e88dca215a5b073")
    #main("OAuth", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/OAuth", "b820d2ad1361c240b7b5c3e8e5e9691f4b98f50a")
    #main("CheckUser", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/CheckUser", "a3443da5504e660687b9363ff47c09b27d51b7ca")