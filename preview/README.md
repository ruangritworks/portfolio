# Local portfolio preview

The production version now lives at the repository root. Open ../index.html in VS Code with Live Server. This folder retains the earlier mockup for reference; it is not deployed.

This is a standalone HTML/CSS mockup based on Ruangrit's resume. It is separate from the Jekyll website and does not require Ruby, npm, or a build.

## Open in VS Code

1. Open this project's folder in VS Code.
2. Open `preview/index.html`.
3. Right-click the file and choose **Open with Live Server** if that extension is installed.

You can also open `preview/index.html` directly in a browser.

## Preview using Python

From the project root, run:

```powershell
python -m http.server 5500 --bind 127.0.0.1 --directory preview
```

Then visit http://127.0.0.1:5500/. Press Ctrl+C to stop.

Edit `index.html` for content and `styles.css` for design. The project cards and resume use native expandable sections. All assets are local; no external font or JavaScript dependencies are needed.

This mockup contains a separate copy of the content; updates here do not automatically update the Jekyll pages. The current visuals are illustrative, not screenshots of client work.
