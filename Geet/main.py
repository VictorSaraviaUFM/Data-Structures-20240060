from utils.data_structures.linked_list import Node
import utils.status as status_utils
import utils.commit as commit_utils
import utils.init as init_utils
from pyfiglet import Figlet
import pickle
import click
import time
import sys
import os


@click.group()
def cli():
    pass


@cli.command()
def banner():

    figlet = Figlet(font='slant')
    print(figlet.renderText('geet'))


@cli.command()
def status():

    path = status_utils.get_current_path()
    new_files = status_utils.scan_for_new_files(path)
    deleted_files = status_utils.scan_for_deleted_files(path)
    modified_files = status_utils.scan_for_modified_files(path)

    status_message = '''
    On branch 'master'
    Your branch is up to date with 'origin/master'.

    Uncommited changes:
        (use "geet commit <comment>..." to commit these changes)
        (use "geet restore <commit>..." to discard changes in working directory)
    ''' 
    print(status_message)

    files_changed = False

    for file in deleted_files:
        files_changed = True
        print('             deleted:', file, end='\n')
    
    for file in modified_files:
        files_changed = True
        print('             modified:', file, end='\n')

    for file in new_files:
        files_changed = True
        print('             added:', file, end='\n')

    if not files_changed:
        print('        < There are no changes in the repository... >')


@cli.command()
def init():

    path = status_utils.get_current_path()
    initial_files = init_utils.get_init_files()
    repo_exists = init_utils.file_exists(path, '.geet')

    if repo_exists:
        print('Invalid operation: a geet repository already exists in this directory.')
        return None

    user_input = input('Creating geet repository in {} [press enter to continue]: '.format(path))
    
    if user_input != "":
        print('Canceling...')
        sys.exit(0)
 
    print('Initializing...')
    time.sleep(1)
    os.mkdir('.geet')
    os.mkdir('.geet/objects')

    for file in initial_files:
        init_utils.write_file(file, initial_files[file])

    # Creates master branch (linked list)
    branch_master = init_utils.create_branch(path)

    # Creates initial commit
    commit_tree = commit_utils.create_tree_object(path, 'Initial commit') 
    commit_utils.save_tree_object(path, commit_tree)
    branch_master.insert_last(Node(commit_tree.name, commit_tree.message))

    # Saves branch as pickle
    file_name = path + '.geet/branch'
    with open(file_name, 'wb') as outp:
        pickle.dump(branch_master, outp, pickle.HIGHEST_PROTOCOL)

    print('Geet repository successfully created.')


@cli.command()
@click.option('-m', help='Commit message')
def commit(m):

    path = status_utils.get_current_path()
    previous_hash_dict = status_utils.read_current_hash_dict(path)
    current_hash_dict = status_utils.get_hash_dict(path)

    if current_hash_dict == previous_hash_dict:
        print('\n     < No changes have been done, cannot commit. >')
        sys.exit(0)
    
    status_utils.save_hash_dict(path) # New current hash dict is saved
    commit_tree = commit_utils.create_tree_object(path, m) # Creates commit tree object
    commit_utils.save_tree_object(path, commit_tree) # Saves commit in disk
    print('Creating commit with hash {}.'.format(commit_tree.name))
    print('Commit message: {}'.format(commit_tree.message))
    # Reads pickle and retrieves branch as linked list object
    branch_path = path + '.geet/branch'

    with open(branch_path, 'rb') as file:
        branch = pickle.load(file)

    branch.insert_last(Node(commit_tree.name, commit_tree.message)) # Adds new commit to branch
    # Saves branch as pickle
    with open(branch_path, 'wb') as outp:
        pickle.dump(branch, outp, pickle.HIGHEST_PROTOCOL)


@cli.command()
def log():

    path = status_utils.get_current_path()
    # Reads pickle and retrieves branch as linked list object
    branch_path = path + '.geet/branch'

    with open(branch_path, 'rb') as file:
        branch = pickle.load(file)
    
    # Print branch from latest to oldest
    branch.reverse()
    print('[HEAD]\n')

    for commit in branch:
        print('Commit hash:', commit.data)
        print('Commit message:', commit.message, '\n')

    print('[Beginning of time]')


if __name__ == '__main__':
    cli()
