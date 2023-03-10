import git
from git_contributions_importer import *
# Your private repo or Bitbucket repo
repo = git.Repo("/Users/chriskarvouniaris/workspace_local/Bitbucket/ruby-backend")
# Your mock repo
mock_repo = git.Repo(".", search_parent_directories=True)
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['christos.karvouniaris247@gmail.com', 'c.karvouniaris@trebbble.co'])
importer.import_repository()
print("erdch")
