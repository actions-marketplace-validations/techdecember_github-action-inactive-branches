from src import actions, io

if __name__ == '__main__':
    ignore_branches, last_commit_age_days, dry_run, github_token, github_base_url, github_repo, ignore_suffix, prefixes_to_delete = io.parse_input()
    print(ignore_suffix)
    print(ignore_branches)
    print(last_commit_age_days)
    print(dry_run)
    print(github_token)
    print(github_base_url)
    print(github_repo)
    print(prefixes_to_delete)
    deleted_branches = actions.run_action(
        ignore_branches=ignore_branches,
        prefixes_to_delete=prefixes_to_delete,
        last_commit_age_days=last_commit_age_days,
        dry_run=dry_run,
        github_repo=github_repo,
        github_token=github_token,
        github_base_url=github_base_url,
        ignore_suffix=ignore_suffix,
    )

    io.format_output({'deleted_branches': deleted_branches})
