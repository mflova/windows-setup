return {
  "folke/snacks.nvim",
  opts = {
    picker = {
      enabled = true,
      exclude = {
        ".ruff_cache",
        ".pytest_cache",
        ".mypy_cache",
        "__pycache__",
        "*egg-info*",
      },
      sources = {
        explorer = {
          hidden = true,
          ignored = true,
        },
        picker = {
          hidden = true,
          ignored = true,
        },
      },
    },
  },
}
