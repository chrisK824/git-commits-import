## Usage

* Create a file at root folder of repository named `settings.json`
* This file name is under gitignore and will not be pushed to the repository
* The `settings.json` file is to include your settings for your import use case, example:
```json
{
  "git_folder_path": "/git/folders/directory/here/",
  "last_imported_commit_ts": 0,
  "emails": [
    "mypersonal@email.com",
    "mycompany@email.com"
  ],
  "new_author": "github-username-here <github-email-here>"
}
```
* Fields explanation:
  * `git_folder_path`: the directory path where your local git repositories (the ones you want to import commits from) are located at
  * `last_imported_commit_ts`: this is the last epoch timestamp that the script has run and is used so that no commits are duplicated during next imports. It should be initialised as 0 and is updated by the script every time it runs.
  * `emails`: the emails that are going to be used by the script to locate the commits to import from local repos. The script will only import commits with author one of those emails in the list
  * `new_author`: the author to be used for the mock imported commits
  * Set the commiter user email through git cli like that: `git config user.email "github-email-here"` . You can skip that part if you already have this set. Use `global` flag if you want this to be global setting for all repositories in your system.

* Run `main.py`: this will analyse all repos in the target directory and import all the commits found with author one of the requested emails.If you see messages printing then you are doing it right.This might take a while if your git folders have many commits history.
* When the script finishes,as you normally would do add, commit and push to remote repository


## Example of my use case:

* `settings.json`:
```json
{
  "git_folder_path": "/Users/chriskarvouniaris/workspace_local/Bitbucket/",
  "last_imported_commit_ts": 0,
  "emails": [
    "christos.karvouniaris247@gmail.com",
    "c.karvouniaris@trebbble.co",
    "christos.karvouniaris@lightsourcelabs.com"
  ],
  "new_author": "chrisK824 <christos.karvouniaris247@gmail.com>"
}

```
* git user.email config:
`git config user.email "christos.karvouniaris247@gmail.com"
`