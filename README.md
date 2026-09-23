# SunsetScan website

Static GitHub Pages site for https://www.sunsetscan.com/. A push to `main` runs the Pages deployment workflow.

## Keep claims current

Before changing a version number, install command, or feature claim, check the tagged SunsetScan release and its README. The site currently describes v2.2.1. The hardware totals (86,276 records, 81,738 model summaries, 224 vendors) come from `data/hardware_eol/sunsetscan_hardware_eol_summary.json` in that tag; they are database totals, not device counts. The total includes related software, services, modules, and accessories. Code is MIT licensed; the database is CC BY-NC 4.0, so do not call the database open source or promise commercial use. The Debian package includes the full database, while source installs can use smaller downloadable profiles.

Do not equate EOL, end of sale, or discontinued with the end of security updates unless the vendor source explicitly supports that conclusion. The router guide and illustrated ASUS/Cisco report previews link to the vendor pages used for their examples. The Cisco 2960-S preview is not a generated scan and does not claim an automatic match in the v2.2.1 database. Keep fictional report details clearly labeled. The comparison page uses a dated snapshot of eol.network, EOSL.ai, Flexera and Device42; refresh counts and scope before repeating its claims. Recheck those links and statements when updating the guide.

`sample-report.html` is a copy of the sanitized v2.1.1 lab report in the SunsetScan repository, with a `noindex` tag, whitespace cleanup, and an example-report label. Keep its version label on the homepage if the sample is reused. Do not publish an unsanitized home or customer report.

The site links to GitHub Discussions in the program repository (`NoCoderRandom/sunsetscan`), confirmed enabled on 23 September 2026. Check that it remains enabled before keeping the Community links.

When updating a release, review `index.html` metadata and links, the install commands and their copy buttons, `sitemap.xml`, and the social preview image. Test desktop and mobile layouts and confirm the deployed Pages run and live site after pushing.
