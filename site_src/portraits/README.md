# portraits — real art goes here

Drop a painting named after the character's id and it replaces that
character's drawn icon everywhere on the site:

    site_src/portraits/bhishma.png
    site_src/portraits/krishna.jpg
    site_src/portraits/draupadi.webp

Then:

    python3 draw_icons.py     # applies whatever is here
    python3 build_site.py     # publishes it

`draw_icons.py` cover-crops to a square biased toward the upper middle (where
a face sits), resizes to 256px, applies the circular mask and draws the
side-coloured ring — so a set that is half painted and half drawn still reads
as one series. Characters with no file here keep their drawn icon.

The ids are the filenames in `../icons/`, and the full list with a ready
prompt for each is in `../../notes/portrait-art-brief.md`.

Supply square-ish images, 512px or larger. Anything smaller will look soft
at 256px on a retina screen.
