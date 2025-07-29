with open("zeek_logs/conn.log") as f:
    for line in f:
        parts = line.strip().split("\t")
        src_ip = parts[2]
        dst_ip = parts[4]
        dst_port = parts[5]
        if int(dst_port) > 1024:
            print(f"Suspicious high port connection: {src_ip} → {dst_ip}:{dst_port}")
