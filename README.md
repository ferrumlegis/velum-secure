# Velum Secure Python Library

## Deutsch

### Beschreibung

Velum Secure ist eine professionelle Python-Bibliothek für präzise TLS-Fingerprinting und HTTP-Client-Simulation. Die Bibliothek ermöglicht es, authentische Browser-Fingerprints zu replizieren und dabei JA3-Signaturen exakt nachzubilden.

### Hauptfeatures

- **JA3-Fingerprint-Spoofing**: Exakte Nachbildung von Browser-TLS-Signaturen
- **HTTP/2 und HTTP/1.1 Support**: Vollständige Unterstützung beider Protokolle
- **Synchrone und asynchrone Requests**: Flexible API für verschiedene Anwendungsfälle
- **Proxy-Unterstützung**: HTTP- und SOCKS5-Proxy-Integration
- **Cookie-Management**: Automatische Session-Verwaltung
- **Platform-spezifische Header**: Authentische Browser-Header-Simulation

### Installation

```bash
pip install vsec_tls
```

### Lizenzierung

Diese Software ist proprietär und erfordert eine gültige Lizenz. Sie können eine Lizenz über unsere Website erwerben:

**[https://velum-secure.com](https://velum-secure.com)**

Nach dem Kauf erhalten Sie Ihren persönlichen `license_key`, welcher für die Nutzung der Bibliothek erforderlich ist.

### Profile-Struktur

Velum Secure verwendet vordefinierte Browser-Profile für maximale Authentizität. Hier ist ein Beispiel des `chrome_139_windows` Profils:

```python
PROFILES = {
    "chrome_139_windows": {
        # Chrome 139.0.7258.66 - Latest stable version
        "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513-21,29-23-24,0",
        "alpn": ["h2", "http/1.1"],
        "http_headers": {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.66 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            "accept-encoding": "gzip, deflate, br, zstd",
            "cache-control": "max-age=0",
            "sec-ch-ua": '"Chromium";v="139", "Google Chrome";v="139", "Not=A?Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-ch-ua-arch": '"x86"',
            "sec-ch-ua-bitness": '"64"',
            "sec-ch-ua-wow64": "?0",
            "sec-ch-ua-platform-version": '"15.0.0"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "dnt": "1"
        },
        "http2_settings": {
            "header_table_size": 65536,
            "enable_push": False,
            "max_concurrent_streams": 1000,
            "initial_window_size": 6291456,
            "max_frame_size": 16384,
            "max_header_list_size": 262144
        },
        "pseudo_header_order": [":method", ":authority", ":scheme", ":path"],
        "connection_flow": 15663105,
        "tls_padding": 512,
        "force_http1": False,
        "enable_grease": True,
        "randomize_extension_order": False,
        "tcp_stealth": False,
        "http_version": "2",
        "platform": {
            "name": "Windows",
            "version": "15.0.0",
            "mobile": False
        }
    }
}
```

### TlsSession Parameter

Die `TlsSession` Klasse unterstützt folgende Initialisierungsparameter:

```python
session = TlsSession(
    license_key: str,                    # Ihr Lizenzschlüssel (erforderlich)
    api_key: str,                        # Ihr API-Schlüssel (erforderlich)
    ja3: Optional[str] = None,           # Custom JA3 String
    alpn: Optional[List[str]] = None,    # ALPN Protokolle
    proxy: Optional[Dict[str, Any]] = None,  # Proxy-Konfiguration
    http2_settings: Optional[Dict[str, Any]] = None,  # HTTP/2 Einstellungen
    tls_padding: Optional[int] = None,   # TLS Padding Größe
    headers: Optional[Dict[str, str]] = None,  # Standard-Header
    cookies: Optional[Dict[str, str]] = None,  # Standard-Cookies
    timeout: Optional[float] = 30.0,     # Request-Timeout
    verify: bool = True,                 # SSL-Zertifikat-Verifikation
    default_profile: str = "chrome_139_windows"  # Standard-Browser-Profil
)
```

### Schnellstart

**Wichtiger Hinweis**: Ersetzen Sie `YOUR_LICENSE_KEY` durch Ihren eigenen Lizenzschlüssel von [https://velum-secure.com](https://velum-secure.com).

#### Synchrone Requests

```python
from vsec_tls import TlsSession

# Initialisierung der Session
session = TlsSession(
    license_key="YOUR_LICENSE_KEY",  # Ersetzen Sie dies durch Ihren Lizenzschlüssel
    api_key="vsk_live_4zFJH1rM@8kq7XyPbUvdM9LrNcVtE#QeRWtZpBGY6La*JUfh2vSx"
)

# GET Request
response = session.get("https://tls.browserleaks.com/json", headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.66 Safari/537.36",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": '"Chromium";v="139", "Google Chrome";v="139", "Not=A?Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
})

print(f"Status: {response.status_code}")
print(f"Headers: {list(response.headers.keys())}")
print(f"Body: {response.text}")
```

#### Asynchrone Requests

```python
import asyncio
from vsec_tls import TlsSession

async def async_example():
    session = TlsSession(
        license_key="YOUR_LICENSE_KEY",  # Ersetzen Sie dies durch Ihren Lizenzschlüssel
        api_key="vsk_live_4zFJH1rM@8kq7XyPbUvdM9LrNcVtE#QeRWtZpBGY6La*JUfh2vSx"
    )

    response = await session.get_async("https://tls.browserleaks.com/json", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.66 Safari/537.36",
        "accept": "*/*"
    })

    print(f"Status: {response.status_code}")
    print(f"Body: {response.text}")

# Ausführung
asyncio.run(async_example())
```

#### Proxy-Unterstützung

```python
# HTTP Proxy
session = TlsSession(
    license_key="YOUR_LICENSE_KEY",
    api_key="vsk_live_4zFJH1rM@8kq7XyPbUvdM9LrNcVtE#QeRWtZpBGY6La*JUfh2vSx",
    proxy={
        "type": "http",
        "host": "",
        "port": 8000,
        "username": "",
        "password": ""
    }
)

# SOCKS5 Proxy
session = TlsSession(
    license_key="YOUR_LICENSE_KEY",
    api_key="vsk_live_4zFJH1rM@8kq7XyPbUvdM9LrNcVtE#QeRWtZpBGY6La*JUfh2vSx",
    proxy={
        "type": "socks5",
        "host": "",
        "port": 8000,
        "username": "",
        "password": ""
    }
)
```

#### Custom TLS-Konfiguration

```python
# Benutzerdefinierte HTTP/2 Einstellungen
session = TlsSession(
    license_key="YOUR_LICENSE_KEY",
    api_key="vsk_live_4zFJH1rM@8kq7XyPbUvdM9LrNcVtE#QeRWtZpBGY6La*JUfh2vSx",
    http2_settings={
        "header_table_size": 32768,
        "enable_push": False,
        "max_concurrent_streams": 500,
        "initial_window_size": 3145728,
        "max_frame_size": 8192,
        "max_header_list_size": 131072
    },
    tls_padding=256
)
```

---

## English

### Description

Velum Secure is a professional Python library for precise TLS fingerprinting and HTTP client simulation. The library enables replication of authentic browser fingerprints while accurately mimicking JA3 signatures.

### Key Features

- **JA3 Fingerprint Spoofing**: Exact replication of browser TLS signatures
- **HTTP/2 and HTTP/1.1 Support**: Full support for both protocols
- **Synchronous and Asynchronous Requests**: Flexible API for various use cases
- **Proxy Support**: HTTP and SOCKS5 proxy integration
- **Cookie Management**: Automatic session management
- **Platform-specific Headers**: Authentic browser header simulation

### Installation

```bash
pip install vsec_tls
```

### Licensing

This software is proprietary and requires a valid license. You can purchase a license through our website:

**[https://velum-secure.com](https://velum-secure.com)**

After purchase, you will receive your personal `license_key`, which is required to use the library.

### Profile Structure

Velum Secure uses predefined browser profiles for maximum authenticity. Here's an example of the `chrome_139_windows` profile:

```python
PROFILES = {
    "chrome_139_windows": {
        # Chrome 139.0.7258.66 - Latest stable version
        "ja3": "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513-21,29-23-24,0",
        "alpn": ["h2", "http/1.1"],
        "http_headers": {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.66 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            "accept-encoding": "gzip, deflate, br, zstd",
            "cache-control": "max-age=0",
            "sec-ch-ua": '"Chromium";v="139", "Google Chrome";v="139", "Not=A?Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-ch-ua-arch": '"x86"',
            "sec-ch-ua-bitness": '"64"',
            "sec-ch-ua-wow64": "?0",
            "sec-ch-ua-platform-version": '"15.0.0"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "dnt": "1"
        },
        "http2_settings": {
            "header_table_size": 65536,
            "enable_push": False,
            "max_concurrent_streams": 1000,
            "initial_window_size": 6291456,
            "max_frame_size": 16384,
            "max_header_list_size": 262144
        },
        "pseudo_header_order": [":method", ":authority", ":scheme", ":path"],
        "connection_flow": 15663105,
        "tls_padding": 512,
        "force_http1": False,
        "enable_grease": True,
        "randomize_extension_order": False,
        "tcp_stealth": False,
        "http_version": "2",
        "platform": {
            "name": "Windows",
            "version": "15.0.0",
            "mobile": False
        }
    }
}
```

### TlsSession Parameters

The `TlsSession` class supports the following initialization parameters:

```python
session = TlsSession(
    license_key: str,                    # Your license key (required)
    api_key: str,                        # Your API key (required)
    ja3: Optional[str] = None,           # Custom JA3 string
    alpn: Optional[List[str]] = None,    # ALPN protocols
    proxy: Optional[Dict[str, Any]] = None,  # Proxy configuration
    http2_settings: Optional[Dict[str, Any]] = None,  # HTTP/2 settings
    tls_padding: Optional[int] = None,   # TLS padding size
    headers: Optional[Dict[str, str]] = None,  # Default headers
    cookies: Optional[Dict[str, str]] = None,  # Default cookies
    timeout: Optional[float] = 30.0,     # Request timeout
    verify: bool = True,                 # SSL certificate verification
    default_profile: str = "chrome_139_windows"  # Default browser profile
)
```

### Quick Start

**Important Note**: Replace `YOUR_LICENSE_KEY` with your own license key from [https://velum-secure.com](https://velum-secure.com).

#### Synchronous Requests

```python
from vsec_tls import TlsSession

# Initialize session
session = TlsSession(
    license_key="YOUR_LICENSE_KEY",  # Replace this with your license key
    api_key="vsk_live_4zFJH1rM@8kq7XyPbUvdM9LrNcVtE#QeRWtZpBGY6La*JUfh2vSx"
)

# GET Request
response = session.get("https://tls.browserleaks.com/json", headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.66 Safari/537.36",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": '"Chromium";v="139", "Google Chrome";v="139", "Not=A?Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
})

print(f"Status: {response.status_code}")
print(f"Headers: {list(response.headers.keys())}")
print(f"Body: {response.text}")
```

#### Asynchronous Requests

```python
import asyncio
from vsec_tls import TlsSession

async def async_example():
    session = TlsSession(
        license_key="YOUR_LICENSE_KEY",  # Replace this with your license key
        api_key="vsk_live_4zFJH1rM@8kq7XyPbUvdM9LrNcVtE#QeRWtZpBGY6La*JUfh2vSx"
    )

    response = await session.get_async("https://tls.browserleaks.com/json", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.66 Safari/537.36",
        "accept": "*/*"
    })

    print(f"Status: {response.status_code}")
    print(f"Body: {response.text}")

# Execute
asyncio.run(async_example())
```

#### Proxy Support

```python
# HTTP Proxy
session = TlsSession(
    license_key="YOUR_LICENSE_KEY",
    api_key="YOUR_API_KEY",
    proxy={
        "type": "http",
        "host": "",
        "port": 8000,
        "username": "",
        "password": ""
    }
)

# SOCKS5 Proxy
session = TlsSession(
    license_key="YOUR_LICENSE_KEY",
    api_key="YOUR_API_KEY",
    proxy={
        "type": "socks5",
        "host": "",
        "port": 8000,
        "username": "",
        "password": ""
    }
)
```

#### Custom TLS Configuration

```python
# Custom HTTP/2 settings
session = TlsSession(
    license_key="YOUR_LICENSE_KEY",
    api_key="vsk_live_4zFJH1rM@8kq7XyPbUvdM9LrNcVtE#QeRWtZpBGY6La*JUfh2vSx",
    http2_settings={
        "header_table_size": 32768,
        "enable_push": False,
        "max_concurrent_streams": 500,
        "initial_window_size": 3145728,
        "max_frame_size": 8192,
        "max_header_list_size": 131072
    },
    tls_padding=256
)
```
