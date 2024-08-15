import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

def assetfinder(domain):
    command = f"assetfinder --subs-only {domain}"
    result = run_command(command)
    with open(f'tmp-assetfinder-{domain}', 'w') as f:
        f.write(result)
    print(f"[*] AssetFinder: {len(result.splitlines())}")
