import git
from git_contributions_importer import *
import os
import json
from datetime import datetime

bitbucket_folder_path = "/Users/chriskarvouniaris/workspace_local/Bitbucket/"
repo_relative_foler_paths = os.listdir(bitbucket_folder_path)
repos = [git.Repo(os.path.join(bitbucket_folder_path, repo_relative_path)) for repo_relative_path in repo_relative_foler_paths]
last_import_ts_file_path = "last_import_ts.json"
print(repos)

with open(last_import_ts_file_path, 'r') as f:
    json_data = json.load(f)

if 'last_commit_git_import_ts' in json_data:
    LAST_COMMIT_GIT_IMPORT_TS = json_data["last_commit_git_import_ts"]

print("do things")
# # Your private repo or Bitbucket repo
# repo = git.Repo("/Users/chriskarvouniaris/workspace_local/Bitbucket/ruby-backend")
# # Your mock repo
mock_repo = git.Repo(".", search_parent_directories=True)
importer = Importer(repos, mock_repo)
# # I use both my personal email and work email here,
# # Since the private repo uses work email, and Github profiles uses
# # my work email
importer.set_author(['christos.karvouniaris247@gmail.com', 'c.karvouniaris@trebbble.co'])
importer.import_repository()

with open(last_import_ts_file_path, "w") as outfile:
    body = {
        "last_commit_git_import_ts" : str(datetime.utcnow())
    }
    json.dump(body, outfile)
print("befnh")
