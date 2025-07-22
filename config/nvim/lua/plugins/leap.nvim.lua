return {
  "ggandor/leap.nvim",
  enabled = true,
  opts = {
    safe_labels = {},

    on_beacons = function(targets, _, _)
      for _, t in ipairs(targets) do
        -- Overwrite the `offset` value in all beacons.
        -- target.beacon looks like: { <offset>, <extmark_opts> }
        if t.label and t.beacon then
          t.beacon[1] = 0
        end
      end
      -- Returning `true` tells `light_up_beacons` to continue as usual
      -- (`false` would short-circuit).
      return true
    end,
  },
}
