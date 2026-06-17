import json
import urllib.request
import urllib.error

_cache = {}


def _fetch_geo(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,country,city"
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            if data.get("status") == "success":
                return data["country"], data["city"]
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError):
        pass
    return None, None


def enrich_entries(entries):
    for entry in entries:
        ip = entry.get("ip")
        if not ip or ip in _cache:
            country, city = _cache.get(ip, (None, None))
        else:
            country, city = _fetch_geo(ip)
            _cache[ip] = (country, city)

        entry["pais"] = country if country else "Desconhecido"
        entry["cidade"] = city if city else "Desconhecido"

    return entries
