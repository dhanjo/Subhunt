import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

def crt(domain):
    command = f"curl -sk 'https://crt.sh/?q=%25.{domain}&output=json' | tr ',' '\n' | awk -F'\"' '/name_value/ {{gsub(/\\*\\./, \"\", $4); gsub(/\\\\n/,\"\\n\",$4);print $4}}' | sort -u"
    result = run_command(command)
    with open(f'tmp-crt-{domain}', 'w') as f:
        f.write(result)
    print(f"[*] crt.sh: {len(result.splitlines())}")
