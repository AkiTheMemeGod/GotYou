import json
import random
import string
import subprocess
import argparse
import os

# Path to the JSON file storing randomized paths
PATHS_FILE = "randomized_paths.json"

# Generate random URL paths
def generate_random_path(prefix):
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{prefix}-{random_suffix}"

# Save randomized paths to a JSON file
def save_randomized_path(random_path, target):
    if os.path.exists(PATHS_FILE):
        with open(PATHS_FILE, "r") as file:
            paths = json.load(file)
    else:
        paths = {}

    paths[random_path] = target.lower()
    print(paths)
    with open(PATHS_FILE, "w") as file:
        json.dump(paths, file)

# Generate phishing link
def generate_phishing_link(target):
    # Create a random path based on the target
    prefix = "accounts.google.com.v3.signin.identifier.continue" if target.lower() == "google" else "www.facebook.com.login.php"
    random_path = generate_random_path(prefix)

    # Save the path to the JSON file
    save_randomized_path(random_path, target)

    # Generate the link
    link = f"http://127.0.0.1:5000/{random_path}"
    return link

def main():
    # Define CLI arguments
    parser = argparse.ArgumentParser(description="Phishing Link Generator (Educational Use Only)")
    parser.add_argument(
        "--target",
        required=True,
        help="The target for the phishing simulation (e.g., Google, Facebook)."
    )
    parser.add_argument(
        "--runserver",
        action="store_true",
        help="Run the Flask server to serve phishing pages."
    )
    args = parser.parse_args()

    # Generate the phishing link
    phishing_link = generate_phishing_link(args.target)
    print(f"Generated Link: {phishing_link}")
    if args.runserver:
        print("\nStarting Flask server... Access the link above in your browser.")
        subprocess.run(["python", "-m", "flask","run"])

if __name__ == "__main__":
    main()
