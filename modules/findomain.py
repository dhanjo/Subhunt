import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

def findomain(domain):
    command = f"findomain -t {domain} -u tmp-findomain-{domain}"
    run_command(command)
    print(f"[*] Findomain: {len(open(f'tmp-findomain-{domain}').readlines())}")
