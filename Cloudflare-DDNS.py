import requests
import time

# Cloudflare API Token
api_token = "input-your-own-edit-zone-dns-api-token"

# Dictionary of domain names and corresponding record names
domain_record_dict = {
    "domain1.com": "record1",
    "domain2.org": "record2"
}

# Loop forever, updating DNS records every 10 minutes
while True:
    # Loop over each domain and record name pair
    for domain_name, record_name in domain_record_dict.items():
        # Get the zone ID for the domain
        zone_url = f"https://api.cloudflare.com/client/v4/zones?name={domain_name}"
        headers = {"Authorization": f"Bearer {api_token}", "Content-Type": "application/json"}
        response = requests.get(zone_url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to get zone ID for {domain_name}.")
            continue

        zone_id = response.json()["result"][0]["id"]

        # Get current DNS record details
        dns_type = "A"
        dns_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records?type={dns_type}&name={record_name}"
        response = requests.get(dns_url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to get DNS record for {record_name} in zone {zone_id}.")
            continue

        dns_record = response.json()["result"][0]

        # Get current server IP address
        ip_url = "https://api.ipify.org"
        ip_address = requests.get(ip_url).text

        # Update DNS record with new IP address
        data = {
            "type": dns_record["type"],
            "name": record_name,
            "content": ip_address,
            "ttl": dns_record["ttl"],
            "proxied": dns_record["proxied"]
        }
        update_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_record['id']}"
        response = requests.put(update_url, headers=headers, json=data)

        # Print response message based on status code
        if response.status_code == 200:
            print(f"DNS record for {record_name}.{domain_name} updated with IP address {ip_address}.")
        elif response.status_code == 404:
            print(f"DNS record for {record_name}.{domain_name} not found.")
        elif response.status_code == 422:
            print("Validation error.")
        elif response.status_code == 429:
            print("API rate limit exceeded.")
        elif response.status_code == 500:
            print("Internal server error.")
        else:
            print("Unknown error.")

    # Wait for 10 minutes before updating again
    time.sleep(600)
