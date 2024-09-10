import download_repo
import run_metrics
import roster_demo
import json

def main(project_name, project_vcs, first_date, second_date):
    clone_location = download_repo.clone_repo(project_name, project_vcs, first_date)
    #run for first date we're looking at
    print(first_date)
    roster_dict = roster_demo.list_roster(clone_location)
    print("done with getting the first roster")
    metrics_filename = run_metrics.run_ast_metrics(clone_location, first_date)
    print("dont with getting the first set of metrics")
    join_metrics(metrics_filename, roster_dict)
    #switch over and run for second date that we're looking at
    download_repo.update_checkout(clone_location, second_date)
    second_roster_dict = roster_demo.list_roster(clone_location)
    second_metrics_filename = run_metrics.run_ast_metrics(clone_location, second_date)
    join_metrics(second_metrics_filename, second_roster_dict)
    #clean up
    download_repo.delete_repo(clone_location)
    print("done with information collection")
    run_metrics.roster_between_two_dates(project_name, first_date, second_date)
    print("all pau with " + project_name)

def join_metrics(filename, roster):
    with open(filename, 'r') as openfile:
        read_json = json.load(openfile)
    read_json['rosterInformation'] = roster
    with open(filename, 'w') as outfile:
        json.dump(read_json, outfile)


if __name__ == "__main__":
    #main("Echo", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/Echo", "2024-06-08",  "2024-09-08")
    #main("ConfirmEdit", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/ConfirmEdit", "2024-06-08",  "2024-09-08")
    #main("CheckUser", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/CheckUser", "2024-06-08",  "2024-09-08")
    #main("Thanks", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/Thanks", "2024-06-08",  "2024-09-08")
    #main("Gadgets", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/Gadgets", "2024-06-08",  "2024-09-08")
    #main("AbuseFilter", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/AbuseFilter", "2024-06-08",  "2024-09-08")
    #main("Cite", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/Cite", "2024-06-08",  "2024-09-08")
    main("WikiLove", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/WikiLove", "2024-06-08",  "2024-09-08")
    main("VisualEditor", "https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/VisualEditor", "2024-06-08",  "2024-09-08")