return {
  "neovim/nvim-lspconfig",
  opts = {
    servers = {
      pyright = {
        mason = true,
        autostart = true,
        settings = {
          python = {
            analysis = {
              autoSearchPaths = true,
              diagnosticMode = "openFilesOnly",
              useLibraryCodeForTypes = true,
              typeCheckingMode = "off",
            },
          },
        },
      },
    },
  },
}
