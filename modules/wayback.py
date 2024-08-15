import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

def wayback(domain):
    command = f"curl -sk 'http://web.archive.org/cdx/search/cdx?url=*.{domain}&output=txt&fl=original&collapse=urlkey&page=' | awk -F/ '{{gsub(/:.*/, \"\", $3); print $3}}' | sort -u"
    result = run_command(command)
    with open(f'tmp-wayback-{domain}', 'w') as f:
        f.write(result)
    print(f"[*] WayBackMachine: {len(result.splitlines())}")
