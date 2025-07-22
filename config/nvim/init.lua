-- bootstrap lazy.nvim, LazyVim and your plugins
require("config.lazy")
vim.lsp.enable("ty")

LazyVim.config.kind_filter = {
  default = {
    "Class",
    "Constructor",
    "Enum",
    "Field",
    "Function",
    "Interface",
    "Method",
    "Module",
    "Namespace",
    "Package",
    "Property",
    "Struct",
    "Trait",
    "Variable", -- Added
    "Constant", -- Added
  },
}

vim.api.nvim_set_hl(0, "LeapBackdrop", { fg = "#777777" })
vim.api.nvim_set_hl(0, "LeapLabel", { fg = "#FF0000" })
