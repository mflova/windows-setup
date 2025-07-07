-- DuckDB plugin configuration
require("duckdb"):setup({
    mode = "standard",  --- Choose between "standard" or "summarized" mode
})
require("git"):setup()