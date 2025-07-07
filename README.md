# Windows-setup

## Instructions

### Terminal based

1. Install powershell
2. Install Oh-My-Posh
3. Install nerdfonts
4. Install scoop (package manager)
5. Copy the profile of the repo (`.ps1` file) into `\Documents\WindowsPowerShell`
    - Some stuff will faill unless all the other following apps are set up.

### Specific apps

#### Git

1. Install lazygit via scoop

#### VSCode

1. Install VSCode and sync it with mail
    1.1. In case I cannot sync it, the main extensions I use are:
        - Error lenses
        - Lazygit (wrapper)
        - Python
        - Ruff

#### Windows manager

1. Install autohotkey via scoop
2. Install komorebi via scoop (https://lgug2z.github.io/komorebi/installation.html#scoop)
3. Copy-paste config files inside the git repo
    3.1. Directory where file should lie is `$Env:USERPROFILE`
    3.2. This includes: komorebic.json, komorebic.bar.json and komorebic.ahk
4. Enable autostart with `komorebic enable-autostart --ahk --bar`

#### File manager

1. Install Yazi via scoop
2. Install programs used by Yazi.
    - `scoop install 7zip jq fd ripgrep fzf zoxide resvg`
    - `zoxide init` to initialize it
3. Install vim via scoop (quick editor)
4. Copy config files (in Windows, this is at %APPDATA%/yazi/)
5. Install theme with `ya pkg add 956MB/vscode-dark-modern`
6. Install tabular data visualizer:
    - `scoop install duckdb`
    - ya pkg add wylie102/duckdb
7. Install git visualizer:
    - ya pkg add yazi-rs/plugins:git