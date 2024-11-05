import os
import subprocess

def update_repository():
    # Path to your cloned repository
    repo_path = ''

    # Change the current working directory to the repository path
    os.chdir(repo_path)

    # Pull the latest changes from the remote repository
    try:
        subprocess.run(['git', 'pull'], check=True)
        print("Repository updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while updating the repository: {e}")

if __name__ == "__main__":
    update_repository()