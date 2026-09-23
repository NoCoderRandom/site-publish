# SunsetScan website

Static GitHub Pages site for https://www.sunsetscan.com/. A push to `main` runs the Pages deployment workflow.

## Keep claims current

Before changing a version number, install command, or feature claim, check the tagged SunsetScan release and its README. The site currently describes v2.2.1. The hardware totals (86,276 records, 81,738 model summaries, 224 vendors) come from `data/hardware_eol/sunsetscan_hardware_eol_summary.json` in that tag; they are database totals, not device counts. The Debian package includes the full database, while source installs can use smaller downloadable profiles.

Do not equate EOL, end of sale, or discontinued with the end of security updates unless the vendor source explicitly supports that conclusion. The router guide links to the vendor pages used for its examples. Recheck those links and statements when updating the guide.

`sample-report.html` is a copy of the sanitized v2.1.1 lab report in the SunsetScan repository, with a `noindex` tag and whitespace cleanup. Keep its version label on the homepage if the sample is reused. Do not publish an unsanitized home or customer report.

When updating a release, review `index.html` metadata and links, the install commands and their copy buttons, `sitemap.xml`, and the social preview image. Test desktop and mobile layouts and confirm the deployed Pages run and live site after pushing.
