"""Regenerate the two v2.2.1 hardware examples with SunsetScan itself.

Usage: python3 scripts/generate-example-reports.py /path/to/sunsetscan
The scanner checkout must be at v2.2.1 and include its bundled EOL index.
"""

import argparse
import hashlib
import sys
from datetime import datetime, timedelta
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scanner", type=Path)
    args = parser.parse_args()
    scanner = args.scanner.resolve()
    site = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(scanner))

    from core.device_identifier import DeviceIdentity
    from core.findings import FindingRegistry, Severity
    from core.hardware_eol import HardwareEOLDatabase
    from core.scanner import HostInfo, ScanResult
    from sunsetscan import SunsetScan
    from ui.export import ReportExporter

    db_path = scanner / "data/hardware_eol/sunsetscan_hardware_eol_index.json.gz"
    expected_sha256 = "743885f22e72d6c997394837104642bb4f92961e81e4d0122606a0eac0e75beb"
    assert hashlib.sha256(db_path.read_bytes()).hexdigest() == expected_sha256, "Database differs from v2.2.1"
    db = HardwareEOLDatabase(db_path)
    converter = SunsetScan.__new__(SunsetScan)
    exporter = ReportExporter()
    assert exporter.settings.version == "2.2.1", "Exporter differs from v2.2.1"

    # The published v2.1.1 lab example shows an Archer C7 with revision v2.0.
    # Keep its lifecycle finding aligned with the v2.2.1 database as well.
    tp_link = db.lookup("TP-Link", "Archer C7", "Archer C7", hardware_version="v2.0")
    assert tp_link is not None and tp_link.status == "unsupported"
    assert tp_link.security_eol_date == "2017-12-31"
    assert tp_link.finding_title == "TP-Link Archer C7 no longer receives security updates"

    scenarios = (
        ("example-asus-router.html", "ASUS", "RT-AC68U", "192.0.2.10", "LOW", "lifecycle_review"),
        ("example-linksys-router.html", "Linksys", "WRT1900AC", "192.0.2.20", "HIGH", "unsupported"),
    )
    for filename, vendor, model, ip, severity, status in scenarios:
        match = db.lookup(vendor=vendor, model=model, part_number=model)
        assert match is not None and match.status == status, (vendor, model, match)
        assert match.match_type == "vendor_model", (vendor, model, match.match_type)
        started = datetime(2026, 9, 23, 10, 0)
        result = ScanResult(target=ip, profile="QUICK", start_time=started,
                            end_time=started + timedelta(seconds=12))
        result.hosts[ip] = HostInfo(ip=ip, state="up", vendor=vendor)
        # The UPnP extractor assigns 0.75 when a device exposes its model.
        identity = DeviceIdentity(vendor=vendor, model=model, device_type="Router",
                                  confidence=0.75, sources=["upnp"])
        converter.hardware_eol = db
        converter.last_device_identities = {ip: identity}
        emitted = converter._run_hardware_eol_pipeline(result)
        assert len(emitted) == 1, (vendor, model, emitted)
        finding = emitted[0]
        assert finding.severity == Severity[severity], (vendor, model, finding.severity)
        assert finding.title == match.finding_title
        assert finding.evidence.endswith("source: " + match.source_url)
        findings = FindingRegistry()
        findings.add(finding)
        path = site / filename
        assert exporter.export_html(result, str(path), findings=findings,
                                    device_identities={ip: identity})
        html = path.read_text(encoding="utf-8")
        assert "<style>" in html and finding.title in html and match.source_url in html
        # This small site navigation sits outside the scanner-generated report body.
        banner = (
            '<div class="example-site-banner"><strong>Example report · SunsetScan v2.2.1</strong>'
            '<a href="/#sample">← All example reports</a></div>\n'
        )
        css = (
            '<style>.example-site-banner{max-width:1300px;margin:16px auto 0;'
            'padding:10px 20px;display:flex;justify-content:space-between;gap:16px;'
            'flex-wrap:wrap;background:#fff;border:1px solid #e2e8f0;'
            'color:#334155;font:600 13px -apple-system,BlinkMacSystemFont,'
            '"Segoe UI",sans-serif}.example-site-banner a{color:#2563eb}</style>\n'
        )
        metadata = (
            f'<meta name="description" content="SunsetScan v2.2.1 example report: '
            f'{vendor} {model} hardware lifecycle finding.">\n'
            f'<link rel="canonical" href="https://www.sunsetscan.com/{filename}">\n'
        )
        html = html.replace("</head>", css + metadata + "</head>", 1)
        html = html.replace("<body>", "<body>\n" + banner, 1)
        html = "\n".join(line.rstrip() for line in html.splitlines()) + "\n"
        path.write_text(html, encoding="utf-8")
        print(f"{filename}: {vendor} {model}, {match.status}, {finding.severity.value}, {match.security_eol_date}")


if __name__ == "__main__":
    main()
