#!/usr/bin/env python3

import os
from pathlib import Path
import subprocess
import sys

import requests

REPOS_ENDPOINT = 'https://api.github.com/users/{}/repos'

user = sys.argv[1]

user_directory = Path(f'users/{user}')

repos = [repo
         for repo in requests.get(REPOS_ENDPOINT.format(user)).json()
         if not repo['fork']]

print('Found these repos:')
for repo in repos:
    print(f"- {repo['name']} [{repo['clone_url']}]")
print()

try:
    os.mkdir(user_directory)
except FileExistsError:
    print(user_directory, 'directory already exists.')
    print()

for repo in repos:
    subprocess.run(('git', 'clone',
                    repo['clone_url'], str(user_directory/repo['name'])))
    print()

for jupyter_notebook in user_directory.glob("**/*.ipynb"):
    subprocess.run(('jupyter-nbconvert', '--to', 'script',
                    str(jupyter_notebook)))
    print()

subprocess.run(('cloc', str(user_directory)))
