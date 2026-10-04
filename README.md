# Ruangrit Srimuang — Data Engineering Portfolio

Production website: static HTML/CSS, based on real resume information. No Ruby, Jekyll, npm, external fonts, analytics, or JavaScript is required.

## Preview locally

Open the repository folder in VS Code. Right-click **index.html** at the repository root and select **Open with Live Server**.

Alternatively:

```powershell
python -m http.server 5501 --bind 127.0.0.1
```

Visit http://127.0.0.1:5501/. Stop with Ctrl+C.

The root index.html is the production website. The preview/ directory and Jekyll template files are retained for reference and are not deployed by the workflow.

## Publish on GitHub Pages

1. Commit and push the changes to the main branch of ruangritworks/portfolio.
2. In the repository, open **Settings → Pages → Build and deployment → Source** and select **GitHub Actions**.
3. Open **Actions → Publish portfolio**. If needed, select **Run workflow**.
4. After the workflow succeeds, visit https://ruangritworks.github.io/portfolio/.

The workflow validates the website and publishes only an explicit list of production files. It does not publish the original academic template, example PDFs, scripts, or preview folder. Follow the [official GitHub Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) for repository settings.

Do not choose a branch-based Jekyll publishing source for this production site.

## Update content

- index.html: portfolio text, professional experience, skills, and contact links.
- styles.css: layout, colors, responsive styles, and focus states.
- resume.html: printable, selectable-text resume.
- files/Ruangrit-Srimuang-Resume.pdf: downloadable resume generated from resume.html.
- favicon.svg: website icon.
- robots.txt and sitemap.xml: public site discovery.

When editing resume content, keep index.html and resume.html consistent and regenerate the PDF. Browser printing with A4 and headers/footers disabled can generate it. The current PDF is a typeset version of the supplied resume information, not the original image.

If the hosting URL changes, update the canonical and Open Graph URLs in index.html, the home link in 404.html, robots.txt, and sitemap.xml.

## Verify

```powershell
python scripts/check_site.py
```

Project illustrations are decorative, not screenshots or measured client results. Professional job titles and dates match the supplied resume; no additional engineering projects or metrics are claimed.
