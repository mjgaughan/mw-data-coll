import download_repo
import run_metrics

def main(project_vcs):
    clone_location = download_repo.clone_repo("placeholder", project_vcs)
    run_metrics.run_ast_metrics(clone_location)
    download_repo.delete_repo(clone_location)

if __name__ == "__main__":
    main("https://gerrit-replica.wikimedia.org/r/mediawiki/extensions/ConfirmEdit")