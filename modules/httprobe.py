from datetime import datetime
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    return result.stdout

def run_httprobe(combined_file, domain):
    current_date = datetime.now().strftime("%Y-%m-%d")
    httprobe_file = f'httprobe-{domain}-{current_date}.txt'
    
    # Use a set to store unique domains
    unique_domains = set()

    # Run httprobe and process the output line by line
    command = f"sort {combined_file} | httprobe"
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, text=True)
    
    with open(httprobe_file, 'w') as outfile:
        for line in result.stdout:
            domain = line.strip()
            if domain not in unique_domains:
                unique_domains.add(domain)
                outfile.write(domain + "\n")

    print(f"[*] HTTPROBE scanned file is {httprobe_file}")
