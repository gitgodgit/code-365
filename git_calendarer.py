#!/usr/bin/env python3
"""
Git Calendarer - Automatically creates GitHub contributions for missing days
Starts from January 1, 2023 and fills in days with varying frequency and intensity
"""

import os
import subprocess
import random
import time
from datetime import datetime, timedelta
import json

START_DATE = datetime(2023, 1, 1)
COMMIT_FILE = "contributions.json"


def remove_git_lock():
    """Remove git lock file if it exists"""
    lock_file = ".git/index.lock"
    if os.path.exists(lock_file):
        try:
            os.remove(lock_file)
            print(f"[DEBUG] Removed stale git lock file")
            return True
        except Exception as e:
            print(f"[WARNING] Could not remove lock file: {e}")
            return False
    return True


def run_git_command(cmd, check=True, verbose=False):
    """Run a git command and return the output"""
    # Remove lock file before running commands that might need it
    if "commit" in cmd or "add" in cmd:
        remove_git_lock()
    
    if verbose:
        print(f"[DEBUG] Running git command: {cmd}")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=check
        )
        output = result.stdout.strip()
        if verbose and output:
            print(f"[DEBUG] Command output: {output[:200]}")
        return output
    except subprocess.CalledProcessError as e:
        if check or verbose:
            print(f"[ERROR] Error running git command: {cmd}")
            print(f"[ERROR] Error code: {e.returncode}")
            print(f"[ERROR] Stderr: {e.stderr}")
            if e.stdout:
                print(f"[ERROR] Stdout: {e.stdout}")
        return None


def init_git_repo():
    """Initialize git repository if it doesn't exist"""
    if not os.path.exists(".git"):
        print("[INFO] Initializing git repository...")
        result = run_git_command("git init", verbose=True)
        if result is None:
            print("[ERROR] Failed to initialize git repository")
        else:
            print(f"[DEBUG] Git init output: {result}")
        
        run_git_command('git config user.name "Git Calendarer"', verbose=True)
        run_git_command('git config user.email "calendarer@example.com"', verbose=True)
        print("[INFO] Git repository initialized.")
    else:
        print("[INFO] Git repository already exists.")


def get_commit_dates():
    """Get all dates that have commits"""
    output = run_git_command('git log --pretty=format:"%ad" --date=short', check=False)
    if not output:
        return set()
    
    dates = set()
    for line in output.split('\n'):
        if line.strip():
            try:
                date = datetime.strptime(line.strip(), '%Y-%m-%d').date()
                dates.add(date)
            except ValueError:
                continue
    return dates


def get_contribution_count_for_date(date):
    """Get number of contributions (commits) for a specific date"""
    date_str = date.strftime('%Y-%m-%d')
    cmd = f'git log --since="{date_str} 00:00:00" --until="{date_str} 23:59:59" --oneline'
    output = run_git_command(cmd, check=False)
    if not output:
        print(f"[DEBUG] No commits found for {date_str}")
        return 0
    count = len([line for line in output.split('\n') if line.strip()])
    print(f"[DEBUG] Found {count} commit(s) for {date_str}")
    return count


def load_contributions():
    """Load previously created contributions from file"""
    if os.path.exists(COMMIT_FILE):
        try:
            with open(COMMIT_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}


def save_contributions(contributions):
    """Save contributions to file"""
    with open(COMMIT_FILE, 'w') as f:
        json.dump(contributions, f, indent=2, default=str)


def create_commit_for_date(date, num_commits=1):
    """Create commit(s) for a specific date"""
    date_str = date.strftime('%Y-%m-%d')
    print(f"[DEBUG] Creating {num_commits} commit(s) for {date_str}")
    
    # Generate varied times throughout the day for multiple commits
    commit_times = []
    if num_commits == 1:
        # Single commit: random time during working hours (8:00 - 21:00)
        hour = random.randint(8, 21)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        commit_time = f"{hour:02d}:{minute:02d}:{second:02d}"
        commit_times.append(commit_time)
        print(f"[DEBUG] Generated time for single commit: {commit_time}")
    else:
        # Multiple commits: spread them throughout the day
        # Divide the day into segments to avoid overlapping times
        start_hour = 8  # 8:00 AM
        end_hour = 22   # 10:00 PM (22:00)
        total_minutes = (end_hour - start_hour) * 60
        
        # Create time slots and pick random times within each slot
        for i in range(num_commits):
            slot_start = (total_minutes // num_commits) * i
            slot_end = (total_minutes // num_commits) * (i + 1) if i < num_commits - 1 else total_minutes
            
            # Random time within this slot
            random_minute = random.randint(slot_start, slot_end - 1)
            hour = start_hour + (random_minute // 60)
            minute = random_minute % 60
            second = random.randint(0, 59)
            
            commit_time = f"{hour:02d}:{minute:02d}:{second:02d}"
            commit_times.append(commit_time)
            print(f"[DEBUG] Generated time for commit {i+1}/{num_commits}: {commit_time}")
        
        # Shuffle to make it look more natural (not always sequential)
        random.shuffle(commit_times)
        print(f"[DEBUG] Shuffled commit times: {commit_times}")
    
    commits_created = []
    
    for i, commit_time in enumerate(commit_times):
        print(f"[DEBUG] Processing commit {i+1}/{len(commit_times)} at {commit_time}")
        # Create or update a file with contribution data
        # Add unique content to ensure git sees it as different
        contribution_data = {
            "date": date_str,
            "commit_number": i + 1,
            "total_commits": num_commits,
            "timestamp": commit_time,
            "unique_id": f"{date_str}-{commit_time}-{i+1}"
        }
        
        print(f"[DEBUG] Writing contribution data to contributions.json")
        try:
            with open("contributions.json", 'w') as f:
                json.dump(contribution_data, f, indent=2, default=str)
            print(f"[DEBUG] File written successfully")
        except Exception as e:
            print(f"[ERROR] Failed to write contributions.json: {e}")
            continue
        
        # Stage the file and verify it was staged
        print(f"[DEBUG] Staging contributions.json")
        remove_git_lock()  # Remove lock before adding
        
        # Check if file is tracked
        ls_files = run_git_command("git ls-files contributions.json", check=False)
        is_tracked = ls_files and "contributions.json" in ls_files
        print(f"[DEBUG] File tracked: {is_tracked}")
        
        # Add the file
        add_result = run_git_command("git add contributions.json", check=False, verbose=True)
        
        # Check if file is actually staged
        # Use diff --cached to verify something is staged for commit
        diff_cached = run_git_command("git diff --cached --name-only", check=False)
        is_staged = diff_cached and "contributions.json" in diff_cached
        
        if not is_staged:
            print(f"[WARNING] File not staged. Checking git status...")
            status_result = run_git_command("git status --porcelain contributions.json", check=False)
            print(f"[DEBUG] Git status: {status_result}")
            
            # If file shows as modified but not staged, or if it's untracked
            if status_result:
                if status_result.startswith("??"):  # Untracked file
                    print(f"[DEBUG] File is untracked, trying add again...")
                    run_git_command("git add contributions.json", check=False, verbose=True)
                elif status_result.startswith(" M"):  # Modified but not staged
                    print(f"[DEBUG] File modified but not staged, trying force add...")
                    run_git_command("git add -f contributions.json", check=False, verbose=True)
            
            # Verify again
            diff_cached = run_git_command("git diff --cached --name-only", check=False)
            is_staged = diff_cached and "contributions.json" in diff_cached
            
            if not is_staged:
                print(f"[ERROR] Failed to stage contributions.json after retries. Status: {status_result}")
                # Try one more time with a small delay and explicit add
                time.sleep(0.1)  # Small delay to let file system sync
                run_git_command("git add .", check=False, verbose=True)
                diff_cached = run_git_command("git diff --cached --name-only", check=False)
                is_staged = diff_cached and "contributions.json" in diff_cached
                
                if not is_staged:
                    print(f"[ERROR] Final attempt failed. Skipping commit.")
                    continue
        
        print(f"[DEBUG] File successfully staged for commit")
        
        # Create commit with backdated timestamp
        # Use both --date flag and environment variables to ensure dates are set correctly
        commit_message = f"Contribution for {date_str}"
        if num_commits > 1:
            commit_message += f" ({i+1}/{num_commits})"
        
        # Format date for git (YYYY-MM-DD HH:MM:SS)
        date_time_str = f"{date_str} {commit_time}"
        
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = date_time_str
        env['GIT_COMMITTER_DATE'] = date_time_str
        
        print(f"[DEBUG] Creating commit with message: {commit_message}")
        print(f"[DEBUG] Author date: {date_time_str}")
        print(f"[DEBUG] Committer date: {date_time_str}")
        
        # Use --date flag along with environment variables
        commit_cmd = f'git commit --date="{date_time_str}" -m "{commit_message}"'
        print(f"[DEBUG] Running: {commit_cmd}")
        
        result = subprocess.run(
            commit_cmd,
            shell=True,
            env=env,
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            commits_created.append((date_str, commit_time))
            print(f"[DEBUG] Successfully created commit for {date_str} at {commit_time}")
            if result.stdout:
                print(f"[DEBUG] Commit output: {result.stdout[:100]}")
        else:
            print(f"[ERROR] Failed to create commit for {date_str} {commit_time}")
            print(f"[ERROR] Return code: {result.returncode}")
            print(f"[ERROR] Stderr: {result.stderr}")
            if result.stdout:
                print(f"[ERROR] Stdout: {result.stdout}")
    
    return commits_created


def should_have_contribution(date):
    """
    Determine how many commits a date should have (always creates if missing)
    Returns: (should_have, num_commits)
    Since we only call this for days WITHOUT contributions, always return True
    """
    # Always create contributions for days that don't have them
    # Use deterministic pattern based on day number for variety
    # This ensures same day always gets same number of commits if rerun
    
    day_of_year = date.timetuple().tm_yday
    weekday = date.weekday()
    
    # Deterministic pattern: use day number to determine commits
    # Weekend (Sat/Sun): 1-2 commits
    if weekday >= 5:
        # Deterministic: every 3rd weekend day gets 2 commits, others get 1
        num_commits = 2 if (day_of_year % 7) == 0 else 1
    else:
        # Weekdays: 1-5 commits based on day pattern
        # Use modulo to create variety: 1, 2, 3, 4, or 5 commits
        pattern = day_of_year % 10
        if pattern < 4:
            num_commits = 1
        elif pattern < 7:
            num_commits = 2
        elif pattern < 9:
            num_commits = 3
        elif pattern == 9:
            num_commits = 4
        else:
            num_commits = 5
    
    return (True, num_commits)


def process_dates():
    """Process all dates from START_DATE to today"""
    print("[INFO] Starting process_dates()...")
    init_git_repo()
    
    today = datetime.now().date()
    current_date = START_DATE.date()
    
    print(f"[INFO] Processing dates from {START_DATE.date()} to {today}")
    print(f"[INFO] Total days to check: {(today - START_DATE.date()).days + 1}")
    
    print("[DEBUG] Loading contributions from file...")
    contributions = load_contributions()
    print(f"[DEBUG] Loaded {len(contributions)} contributions from file")
    
    print("[DEBUG] Getting existing commit dates from git...")
    commit_dates = get_commit_dates()
    print(f"[DEBUG] Found {len(commit_dates)} dates with commits in git")
    
    total_commits_created = 0
    days_processed = 0
    days_with_contributions = 0
    
    while current_date <= today:
        days_processed += 1
        
        if days_processed % 100 == 0:
            print(f"[INFO] Progress: Processed {days_processed} days...")
        
        # Check if date already has contributions
        print(f"[DEBUG] Checking contributions for {current_date}...")
        contribution_count = get_contribution_count_for_date(current_date)
        has_contributions = contribution_count > 0
        
        if has_contributions:
            # Already has contributions, skip
            if days_processed % 50 == 0:
                print(f"[INFO] Processed {days_processed} days... (already has {contribution_count} contributions: {current_date})")
        else:
            # Day has no contributions - always create some
            should_have, num_commits = should_have_contribution(current_date)
            print(f"[INFO] No contributions found for {current_date}. Creating {num_commits} commit(s)...")
            
            print(f"[INFO] Creating {num_commits} commit(s) for {current_date}...")
            commits_created = create_commit_for_date(current_date, num_commits)
            
            if commits_created:
                contributions[str(current_date)] = {
                    "commits": num_commits,
                    "created_at": datetime.now().isoformat()
                }
                total_commits_created += len(commits_created)
                days_with_contributions += 1
                print(f"[OK] Created {len(commits_created)} commit(s) for {current_date}")
            else:
                print(f"[WARNING] No commits were created for {current_date}")
        
        current_date += timedelta(days=1)
    
    save_contributions(contributions)
    
    print("\n" + "="*50)
    print("Summary:")
    print(f"Days processed: {days_processed}")
    print(f"Days with new contributions: {days_with_contributions}")
    print(f"Total commits created: {total_commits_created}")
    print("="*50)
    
    # Check if remote is configured
    remote_url = run_git_command("git config --get remote.origin.url", check=False)
    if not remote_url:
        print("\n[WARNING] No remote repository configured.")
        print("To push to GitHub, run:")
        print("  git remote add origin <your-github-repo-url>")
        print("  git branch -M main")
        print("  git push -u origin main")
    else:
        print(f"\n[OK] Remote repository: {remote_url}")
        print("\nTo push all commits to GitHub, run:")
        print("  git push origin main")
        print("\nNote: You may need to use --force if rewriting history:")


if __name__ == "__main__":
    print("Git Calendarer - Automatic Contribution Generator")
    print("=" * 50)
    
    try:
        process_dates()
        print("\n[OK] Done! Check your GitHub contribution graph to see the results.")
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Progress saved.")
    except Exception as e:
        print(f"\n[ERROR] Error: {e}")
        import traceback
        traceback.print_exc()

