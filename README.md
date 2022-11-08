# Bitbucket To Github Migration

Warning: use at your own risk, comes with no warranty or liability of any kind.

Although the scripts in this repository are mainly targeted at migrating a Bitbucket Mercurial repo to GitHub (using git), [this section](#git-on-Bitbucket-to-git-on-GitHub-Migration) describes migrating a git repository from Bitbucket to GitHub.

The GitHub access token has to have at least the following privileges: gist, repo, write:discussion.


## Mercurial on Bitbucket to git on GitHub Migration

* Create a GitHub repository with the same name (URL) of the original repository in BitBucket.
* Copy the description of the repository.
* Set the `USER_MAPPING`, `KNOWN_REPO_MAPPING`, `KNOWN_ISSUES_COUNT_MAPPING`, and `KNOWN_CMAP_PATHS` variables in `config.py`.
* Inspect Mercurial authors with `hg log --template "{author}\n"` and add entries to `migration_data/authors.map`.
* Run the main migration script and observe for errors:

```
./main.py \
    --github-access-token=<github's personal access token> \
    --hg-fast-export-path=<path to hg-fast-export.sh> \
    --hg-authors-map=migration_data/authors.map \
    --hg-branches-map=migration_data/branches.map \
    [space separated list of bitbucket repositories to migrate]
```

* Copy Wiki by hand from the original repository.
* Change the description of the original repository (BitBucket) to the following:
  * IMPORTANT: the official repository is now at https://github.com/viperproject/...
* Prevent commits in the original repository by changing its settings (BitBucket):
  * All users except for 'admin' should have 'read' permission only.
* Adapt the corresponding Jenkins jobs accordingly.

Alternative manual steps:
* Clone your mercurial repos
* `python3 import-forks.py --repo <path to hg repo> --bitbucket-repository <e.g. viperproject/silver> --bitbucket-username <Bitbucket username> --bitbucket-password <Bitbucket app password>`
* Create folder, `git init`, and `git config core.ignoreCase false`
* Run `<path to hg-fast-export.sh> -r <path to hg repo> --hg-hash` in the git folder
* Adapt `config.py` to have an entry for the bitbucket-repository in `KNOWN_CMAP_PATHS`
* Run `python3 hg-git-commit-map.py --repo <path to git folder> --bitbucket-repository <e.g. viperproject/silver>`
* Push the local git repository to github
* Adapt `config.py` to correctly capture the Bitbucket repos, their GitHub correspondance, and the number of issues
* Run `python3 migrate-discussions.py --github-access-token <GitHub access token> --bitbucket-repository <e.g. viperproject/silver> --github-repository <e.g. viperproject/silver>` to migrate the issues and pull requests (again for all repositories)


This project reuses some code from https://github.com/jeffwidman/bitbucket-issue-migration and https://github.com/fkirc/bitbucket-issues-to-github

## Features

This script migrates:

* Bitbucket's attachments to Github's gists
* Bitbucket's issues `#1..#n` to Github's issues `#1..#n`
  * Bitbucket's issue changes and comments to Github's comments
  * Bitbucket's issue state, kind, priority and component to Github's labels
* Bitbucket's pull requests `#1..#m` to Github's issues and pull requests `#(n+1)..#(n+m)`
  * Closed Bitbucket's pull request to closed Github's issues
  * Open Bitbucket's pull request to Github's pull requests
  * Bitbucket's pull request activity and comments to Github's comments
  * Bitbucket's pull request state to Github's labels

Within a comment:

* Bitbucket's user mentions to Github's user mentions
* Bitbucket's issue and pull request links to Github's issue links
* ...


## Install dependencies

`pip3 install -r requirements.pip`


## git on Bitbucket to git on GitHub Migration
* Clone Bitbucket repo: `git clone --mirror URL_TO_BITBUCKET_REPO`
* cd into cloned repo
* Push to GitHub: `git push --mirror URL_TO_GITHUB_REPO`
* Create a mapping of git commits to themselves: `git log --all --format='%H,%H' > cmap.txt`
* Adapt `config.py` to correctly capture the Bitbucket repos, their GitHub correspondance, and the number of issues
* Run `python3 migrate-discussions.py --github-access-token <GitHub access token> --bitbucket-repository <e.g. viperproject/silver> --github-repository <e.g. viperproject/silver>` to migrate the issues and pull requests (again for all repositories)


##

git clone --mirror git@bitbucket.org:edunext/scytale.git
cd scytale
git push --mirror git@github.com:eduNEXT/scytale.git
git log --all --format='%H,%H' > cmap.txt
python3 migrate-discussions.py --github-access-token ghp_1234 --bitbucket-repository edunext/scytale --github-repository edunext/scytale --bitbucket-username felipem_ntoya --bitbucket-password 6798




git clone --mirror git@bitbucket.org:edunext/scripted_recipes.git
cd scripted_recipes
git push --mirror git@github.com:eduNEXT/scripted_recipes.git
git log --all --format='%H,%H' > cmap.txt

python3 migrate-discussions.py --github-access-token ghp_1234 --bitbucket-repository edunext/scytale --github-repository edunext/scytale --bitbucket-username felipem_ntoya --bitbucket-password 6798

