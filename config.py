# Mercurial user to be used for the commits of the migration
MIGRATION_COMMITS_USER = "Tech admin <technical@edunext.co>"

# Github only accepts assignees from valid users. We map those users from bitbucket.
USER_MAPPING = {
    "felipem_ntoya": "felipemontoya",
    "andrey-canon": "andrey-canon",
    "{5ff8bfd18332a1010e04e061}": "neoneSoft",
    "{557058:3864890d-8f9f-458a-a577-d53029d72723}": "jfavellar90",
    "{5ea743350590bb0b7bdd3cf6}": "mariajgrimaldi",
    "{616ed28325f3130070470e28}": "ian2012",
    "{5aa0657979c4ca427026a4bf}": "Albeiro514",
    "{5b3b8f82e06ca62dc8ad92a5}": "Alec4r",
    "{61a76f5cb0b630006a262194}": "dcoa",
    "{6284357e46f77e006f21b4a2}": "DeimerM",
    "{5ff76fbff7ea2a0107c30a92}": "DonatoB-eduNEXT",
    "{5ff77ddd9edf2800759d8f66}": "jignaciopm",
    "{6180b51826a5400071013ead}": "JuanDavidBuitrago",
    "{557058:9c0d9c50-c6b1-4f12-969b-ee65120acefa}": "juancamilom",
    "{60e0ed910717c6006910889d}": "MaferMazu",
    "{617702f13e3753006ff44204}": "johanv26",
    "{5f5fb70804897f006af9cb10}": "magajh",
    "{5f36d32c6db35e00392b63d8}": "MoisesGSalas",
    "{601d9d3347a95400695c5269}": "Nicolas-alt",
    "{5b22ec8c53650a265f99b3ad}": "Squirrel18",
    "{62843567222d36006fb6a52d}": "Yoiber071",
    "{628435968133bb006f6d0616}": "wlvasquez",
    "{60e4dbb728780700682985af}": "santiagosuarezedunext",
    "maria.grimaldi": "mariajgrimaldi",
    "Diego Rafael Millan Martinez": "diegomillan",
    "Donato Bracuto": "DonatoB-eduNEXT",
    "Albeiro514": "Albeiro514",
    "Moisés González": "MoisesGSalas",
    "ignacio.palma": "jignaciopm",
    "Jhony Avella": "jfavellar90",
    "juancamilom": "juancamilom",
    "Daniel Quiroga": "Squirrel18",
    "Constanza Abarca": "cocococosti",
    "Maria Fernanda Magallanes Z": "MaferMazu",
    "laqEdunext": "laq",
    "Alejandro Cárdenas": "Alec4r",
    "{557058:6c7cd027-bfcc-41a3-bb4d-497f71631bef}": "bound3r",
    # "Bound3R": "bound3r",
}





# We map bitbucket's issue "kind" to github "labels".
KIND_MAPPING = {
    "bug": "bug",
    "enhancement": "enhancement",
    "proposal": "proposal",
    "task": "task",
}

# We map bitbucket's issue "priority" to github "labels".
PRIORITY_MAPPING = {
    "trivial": "trivial",
    "minor": "minor",
    "major": "major",
    "critical": "critical",
    "blocker": "blocker",
}

# We map bitbucket's issue "component" to github "labels".
COMPONENT_MAPPING = {
    "Consistency": "consistency",
    "Parser": "parser",
    "silver-obligations": "silver-obligations",
    "Triggers": "triggers",
    "Examples": "examples",
    "Functions": "functions",
    "Logging, Reporting, IDE": "logging-reporting-ide",
    "Magic Wands": "magic-wands",
    "Permissions": "permissions",
    "Quantified Permissions": "quantified-permissions",
    "Silver": "silver",
    "Z3": "z3"
}

# The only github states are "open" and "closed".
# Therefore, we map some bitbucket states to github "labels".
STATE_MAPPING = {
    "on hold": "on hold",
    "invalid": "invalid",
    "duplicate": "duplicate",
    "wontfix": "wontfix",
    "resolved": None,
    "new": None,
    "open": None,
    "closed": None,
    "DECLINED": "declined",
    "MERGED": "merged",
    "SUPERSEDED": "superseeded",
    "OPEN": None,
}

# Bitbucket has several issue and pull request states.
# All states that are not listed in this set will be closed.
OPEN_ISSUE_OR_PULL_REQUEST_STATES = {
    "open",
    "new",
    "on hold",
    "OPEN",
}

# Mapping of known Bitbucket to their corresponding GitHub repo
# This information is used to convert links
KNOWN_REPO_MAPPING = {
    "edunext/cruise-control": "edunext/cruise-control",
    "edunext/usernamefinder": "edunext/usernamefinder",
    "edunext/manage": "edunext/manage",
    "edunext/scytale": "edunext/scytale",
    "edunext/scripted_recipes": "edunext/scripted_recipes",
}

# Mapping of known Bitbucket repos to their number of issues.
# This information is used to correctly account for the offset
# of PRs' IDs
KNOWN_ISSUES_COUNT_MAPPING = {
    "edunext/cruise-control": 63,
    "edunext/usernamefinder": 3,  # inicialmente fue 0 y perfect, luego le puse 3 para ver si el offset es en github
    "edunext/manage": 12,
    "edunext/scytale": 0,
    "edunext/scripted_recipes": 0,
}

KNOWN_CMAP_PATHS = {
    "edunext/cruise-control": "../repos/cruise-control.git/cmap.txt",
    "edunext/usernamefinder": "../repos/usernamefinder.git/cmap.txt",
    "edunext/manage": "../repos/manage.git/cmap.txt",
    # "edunext/scytale": "../repos/scytale/cmap.txt",
    "edunext/scripted_recipes": "../repos/scripted_recipes.git/cmap.txt",
}






# python3 migrate-discussions.py --github-access-token ghp_1234 --bitbucket-repository edunext/cruise-control --github-repository edunext/cruise-control --bitbucket-username felipem_ntoya --bitbucket-password 6798
# python3 migrate-discussions.py --github-access-token ghp_1234 --bitbucket-repository edunext/usernamefinder --github-repository edunext/usernamefinder --bitbucket-username felipem_ntoya --bitbucket-password 6798
# python3 migrate-discussions.py --github-access-token ghp_1234 --bitbucket-repository edunext/manage --github-repository edunext/manage --bitbucket-username felipem_ntoya --bitbucket-password 6798

# mejor borrar todos los issues en bitbucket
# python3 migrate-discussions.py --github-access-token ghp_1234 --bitbucket-repository edunext/cruise-control --github-repository edunext/cruise-control --bitbucket-username felipem_ntoya --bitbucket-password 6798


