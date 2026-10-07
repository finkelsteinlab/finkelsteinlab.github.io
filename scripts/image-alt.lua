--[[
Give every image in a blog post alt text.

Pandoc moves a #+CAPTION into <figcaption> and leaves the <img> with no alt
at all, so screen readers announce the file name and accessibility checkers
flag every figure. This filter:

  - keeps an explicit `#+ATTR_HTML: :alt ...` untouched;
  - otherwise copies the figure's caption, as plain text, into alt;
  - for an image with neither, warns on stderr so the author can add one.

Used by org-to-post.sh.
--]]

local function has_alt(img)
  return (img.attributes.alt and img.attributes.alt ~= "")
    or #img.caption > 0
end

local function warn(img)
  io.stderr:write("  Warning: image has no alt text or caption: " .. img.src ..
    "\n    Add #+ATTR_HTML: :alt <description> above it.\n")
end

function Figure(fig)
  local text = pandoc.utils.stringify(fig.caption.long)
  -- The org reader hangs #+ATTR_HTML on the figure, not the image, so an
  -- explicit alt would land on <figure>. Move it to the <img>.
  local explicit = fig.attributes.alt
  fig.attributes.alt = nil
  return fig:walk {
    Image = function(img)
      if explicit and explicit ~= "" then
        img.attributes.alt = explicit
      elseif not has_alt(img) and text ~= "" then
        img.attributes.alt = text
      end
      return img
    end,
  }
end

-- Two passes: the first fills alt from captions; the second warns about any
-- image, in a figure or not, that is still left without one.
return {
  { Figure = Figure },
  {
    Image = function(img)
      if not has_alt(img) then
        warn(img)
      end
      return img
    end,
  },
}
