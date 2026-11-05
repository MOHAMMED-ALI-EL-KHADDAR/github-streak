import subprocess
import datetime
import random
import os

# Absolute path to your local git repository
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(REPO_DIR, "activity_log.txt")

def run_git_command(args):
    result = subprocess.run(["git"] + args, cwd=REPO_DIR, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Git error: {result.stderr}")
    return result.returncode == 0

def make_commit():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write timestamp to trigger a file modification
    with open(LOG_FILE, "a") as f:
        f.write(f"Activity update: {now}\n")
    
    # Stage, commit, and push
    if run_git_command(["add", "activity_log.txt"]):
        commit_msg = f"chore: automated update {now}"
        if run_git_command(["commit", "-m", commit_msg]):
            run_git_command(["push", "origin", "main"])

if __name__ == "__main__":
    make_commit()