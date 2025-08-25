import asyncio
from vsec_tls import TlsSession


license_key = "YOUR_LICENSE_KEY"
api_key = "vsk_live_4zFJH1rM@8kq7XyPbUvdM9LrNcVtE#QeRWtZpBGY6La*JUfh2vSx"


def test_ja3_request_sync():
    """Test basic sync HTTP requests."""
    print("\n=== Testing Sync Ja3 Request ===")

    session = TlsSession(license_key=license_key, api_key=api_key)

    print("\n1. GET Request:")
    response = session.get("https://tls.browserleaks.com/json", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.66 Safari/537.36",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "accept-encoding": "text/plain",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "dnt": "1",
        "sec-ch-ua": '"Chromium";v="139", "Google Chrome";v="139", "Not=A?Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-platform-version": '"15.0.0"',
        "sec-ch-ua-arch": '"x86"',
        "sec-ch-ua-bitness": '"64"',
        "sec-ch-ua-wow64": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "x-requested-with": "XMLHttpRequest"
    })
    print(f"Status: {response.status_code}")
    print(f"OK: {response.ok}")
    print(f"Headers: {list(response.headers.keys())}")
    print(f"Text: {response.text}")
    print(f"Cookies: {response.cookies}")

    print("\n=== END Testing Sync Ja3 Request ===")


async def test_ja3_requests_async():
    """Test basic async HTTP requests with JA3."""
    print("\n=== Testing Async JA3 Request ===")

    session = TlsSession(license_key=license_key, api_key=api_key)

    print("\n1. GET Request:")
    response = await session.get_async("https://tls.browserleaks.com/json", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.66 Safari/537.36",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "accept-encoding": "text/plain",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "dnt": "1",
        "sec-ch-ua": '"Chromium";v="139", "Google Chrome";v="139", "Not=A?Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-platform-version": '"15.0.0"',
        "sec-ch-ua-arch": '"x86"',
        "sec-ch-ua-bitness": '"64"',
        "sec-ch-ua-wow64": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "x-requested-with": "XMLHttpRequest"
    })

    print(f"Status: {response.status_code}")
    print(f"OK: {response.ok}")
    print(f"Headers: {list(response.headers.keys())}")
    print(f"Text: {response.text}")
    print(f"Cookies: {response.cookies}")

    print("\n=== END Testing Async JA3 Request ===")


async def test_ja3_requests_async_with_proxy(proxy: dict):
    """Test basic async HTTP requests with JA3."""
    print("\n=== Testing Async JA3 Request with Proxy ===")

    session = TlsSession(
        license_key=license_key,
        api_key=api_key,
        proxy=proxy
    )

    print("\n1. GET Request:")
    response = await session.get_async("https://api.ipify.org?format=json", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.66 Safari/537.36",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "accept-encoding": "text/plain",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "dnt": "1",
        "sec-ch-ua": '"Chromium";v="139", "Google Chrome";v="139", "Not=A?Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-platform-version": '"15.0.0"',
        "sec-ch-ua-arch": '"x86"',
        "sec-ch-ua-bitness": '"64"',
        "sec-ch-ua-wow64": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "x-requested-with": "XMLHttpRequest"
    })

    print(f"Status: {response.status_code}")
    print(f"OK: {response.ok}")
    print(f"Headers: {list(response.headers.keys())}")
    print(f"Text: {response.text}")
    print(f"Cookies: {response.cookies}")

    print("\n=== END Testing Async JA3 Request with Proxy ===")


def main():
    """Run all tests."""
    print("=== TLS Session Test Suite ===")

    test_ja3_request_sync()
    asyncio.run(test_ja3_requests_async())
    asyncio.run(test_ja3_requests_async_with_proxy(proxy={
        "type": "http",
        "host": "",
        "port": 8000,
        "username": "",
        "password": ""
    }))


if __name__ == "__main__":
    main()
