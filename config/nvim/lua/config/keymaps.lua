-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

-- Quickfix list navigation
vim.keymap.set("n", "<S-down>", "<cmd>cnext<return>")
vim.keymap.set("n", "<S-up>", "<cmd>cprev<return>")
