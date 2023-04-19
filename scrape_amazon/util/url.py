import requests
from my_fake_useragent import UserAgent

url_prefix = "https://www.amazon"

# random user-agent
ua = UserAgent(family="chrome", os_family="windows")
# ua = UserAgent(cache=False, use_cache_server=False, safe_attrs=("__injections__",))


def construct_product_URL(domain: str, asin: str) -> str:
    """Constructs product URL.
    Args:
        ASIN (product ID)
    Returns:
        Constructed URL.
    """
    return f"{url_prefix}.{domain}/dp/{asin}"

def construct_questions_URL(domain: str, asin: str) -> str:
    """Constructs questions URL.
    Args:
        ASIN (product ID)
    Returns:
        Constructed URL.
    """
    return f"{url_prefix}.{domain}/ask/questions/asin/{asin}/1?isAnswered=true"

def construct_reviews_URL(domain: str, asin: str) -> str:
    """Constructs review URL.
    Args:
        ASIN (product ID)
    Returns:
        Constructed URL.
    """
    return f"{url_prefix}.{domain}/dp/product-reviews/{asin}"


def get_content(url: str) -> str:
    """Gets the contents of a remote url.
    Args:
        url
    Returns:
        The content fetched from remote url.
    """
    user_agent = ua.random()
    while True:
        content: str = requests.get(url, headers={"User-Agent": user_agent})
        if "api-services-support@amazon.com" in content.text:
            user_agent = ua.random()
            continue
        break

    return content
