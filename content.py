import git
from git_contributions_importer import *
import os
import json
from datetime import datetime

bitbucket_folder_path = "/Users/chriskarvouniaris/workspace_local/Bitbucket/"
repo_relative_foler_paths = os.listdir(bitbucket_folder_path)
repos = [git.Repo(os.path.join(bitbucket_folder_path, repo_relative_path)) for repo_relative_path in repo_relative_foler_paths]
emails = [
    'christos.karvouniaris247@gmail.com',
    'c.karvouniaris@trebbble.co',
    'christos.karvouniaris@lightsourcelabs.com'
]

last_import_ts_file_path = "settings.json"
with open(last_import_ts_file_path, 'r') as f:
    json_data = json.load(f)




mock_repo = git.Repo(".", search_parent_directories=True)
importer = Importer(repos, mock_repo)
importer.set_author(emails)

if 'last_commit_git_import_ts' in json_data:
    LAST_COMMIT_GIT_IMPORT_TS = int(json_data["last_commit_git_import_ts"])
    importer.set_ignore_before_date(LAST_COMMIT_GIT_IMPORT_TS)


importer.import_repository()

with open(last_import_ts_file_path, "w") as outfile:
    body = {
        "last_commit_git_import_ts" : datetime.utcnow().strftime('%s')
    }
print("vhmow")
