--[[
Find the quoted passage in a quote post (#+KIND: quote).

A quote post's body is either the bare passage, or ordinary org prose with
one top-level #+BEGIN_QUOTE block holding the passage:

    A sentence of my own.

    #+BEGIN_QUOTE
    The words being quoted.
    #+END_QUOTE

    Optionally, a sentence after it.

In the second form this filter unwraps the block and brackets its contents
with HTML comment markers, so _includes/blog/quote.html can put the intro
before the <blockquote>, the passage inside it, the attribution after it and
any closing prose last. With no quote block, the body passes through
untouched and the whole of it is the quote.

Two things are refused, since neither has a sensible rendering: more than one
top-level quote block, and a "--- Name" attribution line inside the block
(the layout writes the attribution from #+AUTHOR: and #+SOURCE:).

Used by org-to-post.sh for quote posts only.
--]]

local START = pandoc.RawBlock("html", "<!-- quote:start -->")
local STOP = pandoc.RawBlock("html", "<!-- quote:end -->")

local function attribution_line(block)
  if block.t ~= "Para" or #block.content == 0 then
    return false
  end
  local first = block.content[1]
  return first.t == "Str" and first.text:match("^—") ~= nil
end

function Pandoc(doc)
  local found = 0
  for _, block in ipairs(doc.blocks) do
    if block.t == "BlockQuote" then
      found = found + 1
    end
  end
  if found == 0 then
    return doc
  end
  if found > 1 then
    error("a quote post may hold only one top-level #+BEGIN_QUOTE block; found " .. found .. ".")
  end

  local out = pandoc.Blocks({})
  for _, block in ipairs(doc.blocks) do
    if block.t == "BlockQuote" then
      local inner = block.content
      if #inner > 0 and attribution_line(inner[#inner]) then
        error("drop the \"--- Name\" line from the #+BEGIN_QUOTE block; "
          .. "the attribution comes from #+AUTHOR: and #+SOURCE:.")
      end
      out:insert(START)
      out:extend(inner)
      out:insert(STOP)
    else
      out:insert(block)
    end
  end
  doc.blocks = out
  return doc
end
