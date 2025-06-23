# Instagram Auto-Follow and Profile Extraction

This is a simple Selenium-based automation that logs into Instagram, navigates to a specified profile, follows the account (if not already followed), and extracts basic profile data. It saves this information to a text file in the same directory.

## Features

* Logs in to Instagram using provided credentials
* Navigates to a specific user profile
* Follows the profile (if not already followed)
* Extracts profile information:
  * Number of posts
  * Number of followers
  * Number of following
* Saves the extracted data to a text file named `{profile_name}_profile.txt`

## Requirements

* Python 3.7+
* Google Chrome installed
* ChromeDriver compatible with your Chrome version

## Python Dependencies

Install the required libraries using pip:

```bash
pip install selenium
```
## Setup Instructions

1. **Edit credentials**:
   In the script, replace the placeholders with your Instagram username and password:

   ```python
   USERNAME = "your-user-name"
   PASSWORD = "your-password"
   ```

2. **Target profile**:
   Replace the `TARGET_ACCOUNT` variable with the username of the account you want to follow and extract data from:

   ```python
   TARGET_ACCOUNT = "cbitosc"
   ```

## How to Run

Run the script from your terminal:

```bash
python script.py
```

After successful execution, you will find a file named like `cbitosc_profile.txt` in the same directory with the profile's extracted data.
