# Windows-setup

## Instructions

### Terminal based

1. Install powershell
2. Install scoop (package manager)
3. Install starship via scoop
4. Install eza via scoop
5. Install Windows terminal via scoop
6. Copy configuration settings to its corresponding place
7. Install Oh-My-Posh
8. Install nerdfonts (roboto). It can be done via scoop
9. Copy the profile of the repo (`.ps1` file) into `\Documents\WindowsPowerShell`
    - Some stuff will faill unless all the other following apps are set up.

### Specific apps

#### Neovim/Lazyvim

1. Install nodejs via scoop
2. Install neovim via scoop
3. Follow installation instructions from lazyvim
4. Launch neovim
5. Install luarocks with either:
  - The official website
  - `winget install --id=DEVCOM.Lua  -e`
6. Authenticate copilot with `:Copilot auth`
7. Install some extras via `:LazyExtas`. These should be already done by the config but it is written just in case.
  - Install different extensions that might be needed with `x` In my case, from languages: json, toml, python and markdown
  - From Plugins:
    - test.core
    - ai.core
    - coding.yanky
    - editor.inc-rename
    - lang.yaml
    - overseer.nvim (task-related such as VSCode)

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
