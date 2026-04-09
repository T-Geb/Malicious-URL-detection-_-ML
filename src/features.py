import re
import tldextract
import ipaddress

#add more functions for lexicalfeature extraction
extractor = tldextract.TLDExtract(cache_dir=False)

def get_url_length(url):
    return len(url)

def count_digits(url):
    return sum(c.isdigit() for c in url)

def equals_count(url):
    return url.count('=')

def question_count(url):
    return url.count('?')

def hyphen_count(url):
    return url.count('-')

def count_other_special_chars(url):
    pattern = r'[^a-zA-Z0-9=?-]'  #since equals, question mark and hyphen are counted separately, I'm excluding them in the count for special chars
    special_char = re.findall(pattern,url)
    count = len(special_char)
    return count

def https_check(url):
    return 1 if url.startswith("https") else 0

# A method to get the full domain e.g www.123.com. This method will be used in the domain_number_check method
def get_full_domain(url):
    return extractor(url).fqdn

def get_suffix(url):
    return extractor(url).suffix.lower()


# A method to check if the entire domain is made of numbers and dots
# This will check if the domain is IP-like numbers, which can be an indicator of malicious intent in a URL.

def count_nums_in_domain(url):
    domain = get_full_domain(url)
    digit_count = 0
    for char in domain:
        if char.isdigit():
            digit_count += 1
    return digit_count


#check if the domain is an IP address
def domain_is_ip(url):

    domain = get_full_domain(url)
    try:
        ipaddress.ip_address(domain)
        return 1
    except ValueError:
        return 0

def suspicious_suffix(url):
    suffix = get_suffix(url)
    if suffix in ('',"info","cn","cc","asia","tk","biz","fm","tv","xyz","ml"):
        return 1 # if the domain suffix matches one of the suffixes in this list, indicating suspcious domain
    else:
        return 0  # if the domain suffix doesn't match..return 0


def count_suspicious(url):
    keywords = ["ebayisapi","webscr","rfc","webmail","login","re2","servlet","urgent","confirm","signin","login","login2",
                "account","validate","activate","secure","blogs","crypto","pay","fish"]
    url = url.lower()
    count = 0
    for word in keywords:
        if word in url:
            count += 1
    return count
