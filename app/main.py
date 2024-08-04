import logging
from flask import request, jsonify
from app import app
from whois_scraper import scrape_whois
from cache import get_from_cache, set_in_cache
from database import save_whois_data

logging.basicConfig(level=logging.DEBUG)

@app.route('/lookup_whois', methods=['GET'])
def lookup_whois():
    domain_name = request.args.get('domain_name')
    cached_data = get_from_cache(domain_name)
    if cached_data:
        logging.debug(f"Cache hit for {domain_name}: {cached_data}")
        return jsonify(cached_data)
    
    whois_data = scrape_whois(domain_name)
    logging.debug(f"Scraped data for {domain_name}: {whois_data}")
    save_whois_data(whois_data)
    set_in_cache(domain_name, whois_data)
    return jsonify(whois_data)
