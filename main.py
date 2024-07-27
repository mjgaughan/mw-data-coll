import download_repo
import run_metrics

def main(project_name, project_vcs, commit_hash):
    clone_location = download_repo.clone_repo(project_name, project_vcs, commit_hash)
    run_metrics.run_ast_metrics(clone_location, commit_hash)
    download_repo.delete_repo(clone_location)

if __name__ == "__main__":
    main("ConfirmEdit", "https://gerrit.wikimedia.org/r/mediawiki/extensions/ConfirmEdit", "92bcb7f2a288")