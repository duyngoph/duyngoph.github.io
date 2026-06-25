# Tom Ngo — Personal Website

A clean, minimal personal/academic website inspired by [andrewng.org](https://www.andrewng.org/research).
Built as a static site (plain HTML + CSS + a little JS) — no build step, no dependencies.

## Pages

| File | Page |
|------|------|
| `index.html` | About — hero, bio, research focus, news |
| `research.html` | Research statement, interests, publications |
| `projects.html` | Selected projects |
| `cv.html` | Full CV (education, experience, skills, awards, certifications) |

## Run locally

Just open `index.html` in a browser, or serve the folder:

```bash
# Python 3
python -m http.server 8000
# then visit http://localhost:8000
```

## Customize

- **Photo** — replace `assets/profile.svg` with your own image. If you use a `.jpg`/`.png`,
  update the `src` in `index.html` (the `.hero-photo` `<img>`).
- **CV PDF** — replace `assets/Tom_Ngo_CV.pdf` with your latest compiled CV (the
  "Download PDF" button and the "CV" link point here).
- **Colors / fonts** — edit the CSS variables at the top of `style.css` (`--accent`, fonts, spacing).
- **Content** — text lives directly in the HTML files. Email, LinkedIn, and GitHub links appear
  in each page's header social row and footer.

## Deploy

**GitHub Pages**
1. Push this folder to a GitHub repo.
2. Settings → Pages → Source: `main` branch, `/ (root)`.
3. Your site goes live at `https://<username>.github.io/<repo>/`.

**Netlify / Vercel / Cloudflare Pages** — drag-and-drop the folder, or connect the repo.
No build command needed; the publish directory is the repo root.
