import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from modules.wayback import wayback
from modules.crt import crt
from modules.findomain import findomain
from modules.subfinder import subfinder
from modules.assetfinder import assetfinder
from modules.combine import combine_results
from modules.httprobe import run_httprobe

def main(domain):
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_func = {
            executor.submit(wayback, domain): "Wayback",
            executor.submit(crt, domain): "CRT",
            executor.submit(findomain, domain): "Findomain",
            executor.submit(subfinder, domain): "Subfinder",
            executor.submit(assetfinder, domain): "Assetfinder",
        }

        for future in as_completed(future_to_func):
            func_name = future_to_func[future]
            try:
                future.result()
                print(f"{func_name} completed successfully.")
            except Exception as e:
                print(f"{func_name} generated an exception: {e}")

    combined_file = combine_results(domain)
    run_httprobe(combined_file, domain)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Enumeration Script")
    parser.add_argument("-d", "--domain", required=True, help="Target domain for enumeration")
    args = parser.parse_args()

    main(args.domain)
