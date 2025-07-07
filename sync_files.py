"""Sync files from the computer to the Git repo."""

import os
import shutil
from pathlib import Path


def sync_powershell_profile() -> None:
    """Copies the user's PowerShell profile to the local 'config/powershell' directory."""
    # Resolve the default PowerShell profile path
    folders = list(Path(os.environ["USERPROFILE"]).glob("OneDrive *"))
    assert len(folders) == 1, "Expected exactly one OneDrive folder"
    folder = folders[0]
    documents = list(folder.glob("Documents"))
    assert len(documents) == 1, "Expected exactly one Documents folder"
    profile_path = documents[0] / "WindowsPowerShell" / "Microsoft.PowerShell_profile.ps1"

    if not profile_path.exists():
        print(f"PowerShell profile not found at {profile_path}")
        return

    # Destination path: <current_file_dir>/config/powershell
    destination_dir = Path(__file__).parent / "config" / "powershell"
    destination_dir.mkdir(parents=True, exist_ok=True)

    # Copy the profile file
    destination_file = destination_dir / profile_path.name
    shutil.copy2(profile_path, destination_file)

    print(f"PowerShell profile copied to: {destination_file}")

def sync_komorebi_files() -> None:
    """Finds and copies all files under the user's home directory that contain 'komorebi'."""
    user_home = Path(os.environ["USERPROFILE"])
    destination_base = Path(__file__).parent / "config" / "komorebi"
    destination_base.mkdir(parents=True, exist_ok=True)

    # Find all matching files (case-insensitive)
    matches = [f for f in user_home.glob("*") if f.is_file() and "komorebi" in f.name.lower()]

    if not matches:
        print("No matching Komorebi files found.")
        return

    for source_file in matches:
        # Compute relative path from user_home
        relative_path = source_file.relative_to(user_home)
        destination_file = destination_base / relative_path

        # Ensure destination directory exists
        destination_file.parent.mkdir(parents=True, exist_ok=True)

        # Copy the file
        shutil.copy2(source_file, destination_file)

    print(f"Copied {len(matches)} Komorebi files to {destination_base}")

def sync_yazi_files() -> None:
    """Copies the entire %APPDATA%/yazi directory to the local 'config/yazi' directory."""
    source_dir = Path(os.environ["APPDATA"]) / "yazi" / "config"
    destination_dir = Path(__file__).parent / "config" / "yazi"

    if not source_dir.exists():
        print(f"Yazi directory not found at: {source_dir}")
        return

    # Create destination directory if it doesn't exist
    destination_dir.mkdir(parents=True, exist_ok=True)

    # Copy all contents from source_dir to destination_dir
    for item in source_dir.iterdir():
        dest_item = destination_dir / item.name
        if item.is_dir():
            shutil.copytree(item, dest_item, dirs_exist_ok=True)
        else:
            shutil.copy2(item, dest_item)

    print(f"Copied Yazi configuration from {source_dir} to {destination_dir}")

if __name__ == "__main__":
    # shutil.rmtree(Path(__file__).parent / "config")
    sync_powershell_profile()
    sync_komorebi_files()
    sync_yazi_files()