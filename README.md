# SunsetScan Website

Static homepage for `www.sunsetscan.com`, the public website for the open-source SunsetScan scanner.

## Local preview

This site has no build step:

```bash
python3 -m http.server 4173
```

Then open `http://127.0.0.1:4173/`.

## Deployment

The repository is ready for GitHub Pages in two ways:

- GitHub Pages with Actions, using `.github/workflows/pages.yml`.
- Plain static hosting from the repository root, because all page files are committed directly.

The `CNAME` file points GitHub Pages at:

```text
www.sunsetscan.com
```

After the repository is published, set the domain DNS to GitHub Pages:

```text
A     @     185.199.108.153
A     @     185.199.109.153
A     @     185.199.110.153
A     @     185.199.111.153
CNAME www   NoCoderRandom.github.io
```

GitHub Pages will also provide the normal project URL, typically:

```text
https://nocoderrandom.github.io/sunsetscan.com/
```

## Source product

The scanner source lives in the renamed SunsetScan repository:

https://github.com/NoCoderRandom/sunsetscan

## Content notes

The homepage currently uses SunsetScan data from the public repository and local documentation:

- MIT licensed scanner.
- Hardware EOL database artifacts licensed under CC BY-NC 4.0.
- Current scanner release: 2.0.0.
- Current hardware EOL snapshot: 59,969 lifecycle records and 47,341 model summaries.
- Monthly scanner and database refresh positioning.
