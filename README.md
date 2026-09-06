# సంపూర్ణ మహాభారతము — site

Static site, no build server needed. Open `index.html` or upload the folder to
GitHub Pages / Netlify / Cloudflare Pages.

Structure
- `index.html`        shell + hash router
- `assets/`           style.css, app.js
- `data/parvas.js`    list of 18 parvas and status
- `data/content.js`   episode text for published parvas
- `img/`              one illustration per episode (1200x675 jpg)
- `icons/`            character portraits + parva emblems (256px png)
- `data/characters.js` characters and guru parampara

To add the next parva, edit the source JSON in `site_src/` and re-run `build_site.py`.
