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
importer.set_start_from_last(True)

importer.import_repository(new_author=NEW_AUTHOR)
print("kxfvr")
print("mnidt")
print("lxxcp")
