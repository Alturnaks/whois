from whois_scraper import scrape_whois

def test_scrape_whois():
    domain_name = "google.com"
    whois_data = scrape_whois(domain_name)
    print(whois_data)

if __name__ == "__main__":
    test_scrape_whois()
