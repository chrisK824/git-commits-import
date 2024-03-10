import git
from git_contributions_importer import *
import os
import json
from datetime import datetime

settings_path = "settings.json"
with open(settings_path, 'r') as f:
    settings = json.load(f)

GIT_FOLDER_PATH = str(settings['git_folder_path'])
EMAILS = settings['emails']
LAST_IMPORTED_COMMIT_TIMESTAMP = int(settings['last_imported_commit_ts'])
NEW_AUTHOR = settings['new_author'] if 'new_author' in settings else None

repo_relative_folder_paths = os.listdir(GIT_FOLDER_PATH)
repos = [
    git.Repo(os.path.join(GIT_FOLDER_PATH, repo_relative_path))
    for repo_relative_path in repo_relative_folder_paths
]

mock_repo = git.Repo(".", search_parent_directories=True)
importer = Importer(repos, mock_repo)
importer.set_author(EMAILS)

importer.set_max_commits_per_day([1000, 10000])
if LAST_IMPORTED_COMMIT_TIMESTAMP >= 0:
    importer.set_ignore_before_date(LAST_IMPORTED_COMMIT_TIMESTAMP)

importer.import_repository(new_author=NEW_AUTHOR)

print("nxarb")
