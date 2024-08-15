import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

def subfinder(domain):
    command = f"subfinder -all -silent -d {domain} 1> tmp-subfinder-{domain}"
    run_command(command)
    print(f"[*] SubFinder: {len(open(f'tmp-subfinder-{domain}').readlines())}")
