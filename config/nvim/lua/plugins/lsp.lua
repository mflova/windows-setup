return {
  "neovim/nvim-lspconfig",
  opts = {
    inlay_hints = { enabled = false },
    servers = {
      ty = {
        mason = true,
        autostart = true,
      },
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
