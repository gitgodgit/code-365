# Git Calendarer 📅

Automatically creates GitHub contributions for missing days starting from January 1, 2023. The program checks each day and creates commits with varying frequency and intensity to make your contribution calendar green!

## Features

- ✅ Automatically detects missing contribution days
- ✅ Creates commits with backdated timestamps
- ✅ Varies commit frequency (weekdays vs weekends)
- ✅ Different "greenness" levels (1-5 commits per day)
- ✅ Smart weekend/weekday contribution patterns
- ✅ Preserves existing contributions

## How It Works

The program:
1. Starts from **January 1, 2023**
2. Checks each day up to today
3. If a day has no contributions, it may create some (based on probability)
4. Creates 1-5 commits per day (more commits = darker green on GitHub)
5. Uses backdated timestamps so commits appear on the correct dates

### Contribution Patterns

- **Weekdays**: 85% chance of having contributions
  - 1-5 commits (weighted towards 1-3)
- **Weekends**: 60% chance of having contributions
  - 1-2 commits

## Setup

1. **Install Python 3.6+** (if not already installed)

2. **Run the script:**
   ```bash
   python git_calendarer.py
   ```

## Usage

1. **Navigate to your project directory** (or create a new one):
   ```bash
   cd git-calendarer
   ```

2. **Run the script:**
   ```bash
   python git_calendarer.py
   ```

3. **Connect to GitHub** (if not already connected):
   ```bash
   git remote add origin https://github.com/yourusername/your-repo.git
   git branch -M main
   ```

4. **Push to GitHub:**
   ```bash
   git push -u origin main
   ```
   
   Note: Since we're creating backdated commits, you might need to force push:
   ```bash
   git push -u origin main --force
   ```
   ⚠️ **Warning**: Only force push if this is your own repository and you're okay with rewriting history!

## How GitHub Contributions Work

GitHub's contribution graph shows:
- **No commits** = Gray
- **1-2 commits** = Light green
- **3-4 commits** = Medium green
- **5-9 commits** = Darker green
- **10+ commits** = Darkest green

This script varies the number of commits per day to create a natural-looking pattern.

## Files Created

- `contributions.json` - Tracks which dates have contributions created
- Git commits with backdated timestamps

## Notes

- The script preserves any existing commits/contributions
- Commits are created with realistic timestamps throughout each day
- The script can be run multiple times - it won't duplicate contributions for days that already have them
- Make sure you have a GitHub repository ready to push to!

## License

Free to use and modify for personal projects.

