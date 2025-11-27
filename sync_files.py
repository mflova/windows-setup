"""Sync files from the computer to the Git repo."""

import os
import shutil
from pathlib import Path


def sync_windows_terminal_settings() -> None:
    settings_json = (
        Path(os.environ["USERPROFILE"])
        / "scoop"
        / "apps"
        / "windows-terminal"
        / "current"
        / "settings"
        / "settings.json"
    )
    destination_folder = Path(__file__).parent / "config" / "windows-terminal"
    destination_folder.mkdir(parents=True, exist_ok=True)
    destination_file = destination_folder / "settings.json"
    if not settings_json.exists():
        print(f"Windows Terminal settings file not found at: {settings_json}")
        return

    # Copy the settings file to the destination folder
    shutil.copy2(settings_json, destination_file)
    print(f"Windows Terminal settings copied to: {destination_file}")


def sync_powershell_profile() -> None:
    """Copies the user's PowerShell profile to the local 'config/powershell' directory."""
    # Resolve the default PowerShell profile path
    folders = list(Path(os.environ["USERPROFILE"]).glob("OneDrive *"))
    assert len(folders) == 1, "Expected exactly one OneDrive folder"
    folder = folders[0]
    documents = list(folder.glob("Documents"))
    assert len(documents) == 1, "Expected exactly one Documents folder"
    profile_path = (
        documents[0] / "WindowsPowerShell" / "Microsoft.PowerShell_profile.ps1"
    )

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
    matches = [
        f for f in user_home.glob("*") if f.is_file() and "komorebi" in f.name.lower()
    ]

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


def sync_nvim_files() -> None:
    source_dir = Path(os.environ["APPDATA"]).parent / "Local" / "nvim"
    destination_dir = Path(__file__).parent / "config" / "nvim"

    if not source_dir.exists():
        print(f"NVIM directory not found at: {source_dir}")

    # Create destination directory if it doesn't exist
    destination_dir.mkdir(parents=True, exist_ok=True)

    # Copy all contents from source_dir to destination_dir
    for item in source_dir.iterdir():
        dest_item = destination_dir / item.name
        if item.is_dir():
            shutil.copytree(item, dest_item, dirs_exist_ok=True)
        else:
            shutil.copy2(item, dest_item)

    print(f"Copied Nvim configuration from {source_dir} to {destination_dir}")

def sync_git_config() -> None:
    """Copies the .gitconfig file from the user's home directory to the local 'config/git' directory, excluding the [user] section."""
    source_file = Path(os.environ["USERPROFILE"]) / ".gitconfig"
    destination_dir = Path(__file__).parent / "config" / "git"
    
    if not source_file.exists():
        print(f"Git config file not found at: {source_file}")
        return
    
    # Create destination directory if it doesn't exist
    destination_dir.mkdir(parents=True, exist_ok=True)
    
    # Read the source file and filter out the [user] section
    destination_file = destination_dir / ".gitconfig"
    with open(source_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Filter out [user] section
    filtered_lines = []
    skip_section = False
    for line in lines:
        # Check if we're starting a new section
        if line.strip().startswith('['):
            skip_section = line.strip().lower().startswith('[user')
        
        # Add line if we're not in the [user] section
        if not skip_section:
            filtered_lines.append(line)
    
    # Write the filtered content to the destination file
    with open(destination_file, 'w', encoding='utf-8') as f:
        f.writelines(filtered_lines)
    
    print(f"Git config copied to: {destination_file} (excluded [user] section)")

if __name__ == "__main__":
    # shutil.rmtree(Path(__file__).parent / "config")
    sync_windows_terminal_settings()
    sync_powershell_profile()
    sync_git_config()
    sync_komorebi_files()
    sync_nvim_files()
    # sync_yazi_files()
