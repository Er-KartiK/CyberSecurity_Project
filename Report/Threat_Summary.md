# Threat Summary

## Detected Anomalies
- Multiple TCP connections from 10.0.2.15 to external IPs using high-numbered ports
- HTTP request to `malicious.com/payload.exe` — likely malware download

## Mitigation Recommendations
- Block 10.0.2.15 in firewall rules immediately
- Add signature detection for `/payload.exe` in web filters
- Monitor outbound traffic for unusual domains and filenames
- Conduct endpoint antivirus scan on hosts communicating with flagged IPs

## Notes
Due to tool limitations, Zeek logs and analysis were simulated based on real PCAP samples.
