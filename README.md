**This is a mock repository.** 

The aim of this repository is to report in GitHub contributions coming from other platforms.

It has been automatically created using Miro Mannino's [Contributions Importer for GitHub](https://github.com/miromannino/contributions-importer-for-github)

## Usage:

1. Clone or fork the repo
2. Modify main.py to include the paths for your git projects folders - can include any git repo from any platform, as it is just local in your station
3. Modify main.py to include the emails used for the git repositories you pointing at - can include multiple emails, so you can cover personal, work email etc
4. Initialise last_import_ts.json as empty json for the first runtime - after each run of the script, this will be populated so that the next runs won't include already counted commits
5. Run the main.py script to fetch all of your commits from the git repos in the destination folders
6. Git add, git commit and git push 
7. Done - check your github graph to see the pushed commits - the commits will be accounted on this dummy mock repo so just you can monitor your commits from all other platforms


## Notice

The content of this repository contains mock code. This prevents private source code to be leaked. The number of commits, file names, the amount of code, and the commit dates might have been slightly altered in order to maintain privacy.

Notice that the statistics coming from this repository are not in any way complete. Commits only come from other selected git repositories. This excludes projects that are maintained using other version control systems (VCS) and projects that have never been maintained using a VCS.

## Reasons

GitHub shows contributions statistics of its users. There are [several reasons](https://github.com/isaacs/github/issues/627) why this feature could be debatable.

Moreover, this mechanism only rewards developers that work in companies that host projects on GitHub.

Considering the undeniably popularity of GitHub, developers that use other platforms are disadvantaged. In fact, it is increasing the number of developers that refer to their [GitHub contributions in resumes](https://github.com/resume/resume.github.com). Similarly, recruiters [may use GitHub to find talents](https://www.socialtalent.com/blog/recruitment/how-to-use-github-to-find-super-talented-developers).

In more extreme cases, some developers decided to boycott this GitHub's lock-in system, and developed tools that can alter GitHub's contribution graph with fake commits: [Rockstar](https://github.com/avinassh/rockstar) and [Vanity text for GitHub](https://github.com/ihabunek/github-vanity) are good examples. 

Instead, the aim of [Contributions Importer for GitHub](https://github.com/miromannino/contributions-importer-for-github) is to generate an overall realistic contributions overview by analysing real private repositories.
