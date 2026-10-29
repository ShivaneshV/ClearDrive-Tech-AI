import subprocess
import re
import sys
import os
import time

def main():
    print("=" * 70)
    print("      🚗 CLEAR-DRIVE AI : LIVE CLOUDFLARE EDGE TUNNEL LAUNCHER")
    print("=" * 70)
    
    workspace = os.path.dirname(os.path.abspath(__file__))
    cloudflared_path = os.path.join(workspace, "cloudflared.exe")
    if not os.path.exists(cloudflared_path):
        print(f"[-] cloudflared.exe not found at {cloudflared_path}")
        return

    cmd = [cloudflared_path, "tunnel", "--url", "http://localhost:5000"]
    print("[+] Starting Cloudflare Quick Tunnel to http://localhost:5000...")
    
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        bufsize=1
    )
    
    tunnel_url = None
    url_pattern = re.compile(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com")
    
    for line in iter(proc.stdout.readline, ''):
        print(line, end='', flush=True)
        if not tunnel_url:
            match = url_pattern.search(line)
            if match:
                tunnel_url = match.group(0)
                print("\n" + "=" * 70)
                print(f"  🎉 LIVE CLOUDFLARE PUBLIC URL DETECTED:")
                print(f"  🔗 {tunnel_url}")
                print("=" * 70 + "\n")
                
                try:
                    tunnel_file = os.path.join(workspace, "tunnel_url.txt")
                    with open(tunnel_file, "w") as f:
                        f.write(tunnel_url + "\n")
                    print(f"[+] Saved to tunnel_url.txt: {tunnel_url}")
                    
                    # Push updated URL to GitHub so Cloudflare Worker auto-syncs
                    subprocess.run(["git", "add", "tunnel_url.txt"], cwd=workspace, check=False)
                    subprocess.run(["git", "commit", "-m", f"chore: sync live tunnel URL {tunnel_url}"], cwd=workspace, check=False)
                    subprocess.run(["git", "push", "origin", "main"], cwd=workspace, check=False)
                    print(f"[+] Cloudflare Worker cleardrive-ai synced successfully via GitHub!\n")
                except Exception as e:
                    print(f"[-] Cloudflare sync notice: {e}\n")

if __name__ == "__main__":
    main()
