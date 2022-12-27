import sys
from os import getenv
from typing import List


# ignore_branches, last_commit_age_days, dry_run, github_token, github_base_url, github_repo, ignore_suffix =
# io.parse_input(),


def parse_input() -> (list, tuple, int, bool, str, str, str, str):
    args: List[str] = sys.argv

    if len(args) != 8:
        input_string = ' '.join(args)
        expected_string = f'{args[0]} ignore_branches prefixes_to_delete last_commit_age_days dry_run_yes_no github_token github_repo github_base_url, ignore_suffix'
        raise RuntimeError(f'Incorrect input: {input_string}. Expected: {expected_string}')

    branches_raw: str = args[1]
    ignore_branches = branches_raw.split(',')
    if ignore_branches == ['']:
        ignore_branches = []

    prefixes_raw: str = args[2]
    prefixes_to_delete = prefixes_raw.split(',')
    if prefixes_to_delete == ['']:
        raise RuntimeWarning('There are no prefixes to search.')

    last_commit_age_days = int(args[3])

    # Dry run can only be either `true` or `false`, as strings due to github actions input limitations
    dry_run = False if args[4] == 'no' else True

    github_token = args[5]

    github_repo = getenv('GITHUB_REPOSITORY')

    github_base_url = args[6]

    ignore_suffix = args[7]

    return ignore_branches, prefixes_to_delete, last_commit_age_days, dry_run, github_token, github_base_url, github_repo, ignore_suffix


def format_output(output_strings: dict) -> None:
    for name, value in output_strings.items():
        print(f'::set-output name={name}::{value}')
