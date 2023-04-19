"""Defines various scraper functions."""
from types import ModuleType

from .util.scrape import scrape_reviews, scrape_product
from .util.url import construct_reviews_URL, construct_product_URL, construct_questions_URL


def get_reviews(domain: str, asin: str) -> ModuleType:
    print(f"[INFO] Scraping Reviews of Amazon ProductID - {asin}")
    """Scraper
    Args:
        asin: Amazon Product ID.
    Returns:
        Scraped Dataframe
    """
    all_reviews_url = construct_reviews_URL(domain, asin)
    return scrape_reviews(all_reviews_url, domain)

def get_product(domain: str, asin: str) -> ModuleType:
    print(f"[INFO] Scraping Product Details of Amazon ProductID - {asin}")
    """Scraper
    Args:
        asin: Amazon Product ID.
    Returns:
        Scraped Dataframe
    """
    product_url = construct_product_URL(domain, asin)
    print(f"[INFO] Scraping Product Details of Amazon ProductID - {product_url}")
    return scrape_product(product_url)

def get_questions(domain: str, asin: str) -> ModuleType:
    print(f"[INFO] Scraping Questions of Amazon ProductID - {asin}")
    """Scraper
    Args:
        asin: Amazon Product ID.
    Returns:
        Scraped Dataframe
    """
    all_reviews_url = construct_reviews_URL(domain, asin)
    return scrape_reviews(all_reviews_url, domain)

def get_all(domain: str, asin: str) -> ModuleType:
    print(f"[INFO] Scraping All of Amazon ProductID - {asin}")
    """Scraper
    Args:
        asin: Amazon Product ID.
    Returns:
        Scraped Dataframe
    """
    all_reviews_url = construct_reviews_URL(domain, asin)
    return scrape_reviews(all_reviews_url, domain)
