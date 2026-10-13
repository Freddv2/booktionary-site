#!/usr/bin/env python3
"""Gate a prepared website PR on the exact public App Store version."""

import json
import os
from pathlib import Path
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen

APP_ID = 6796368335
BUNDLE_ID = "com.freddv2.booktionary"
COUNTRIES = ("us", "ca")


def lookup(country):
    query = urlencode({"id": APP_ID, "country": country, "entity": "software"})
    request = Request(f"https://itunes.apple.com/lookup?{query}",
                      headers={"User-Agent": "BooktionaryReleaseCheck/1.0"})
    with urlopen(request, timeout=20) as response:
        return json.load(response)


def public_version(payload):
    results = payload.get("results", [])
    if payload.get("resultCount") != 1 or len(results) != 1:
        raise ValueError("Apple lookup did not return exactly one app")
    app = results[0]
    if app.get("trackId") != APP_ID or app.get("bundleId") != BUNDLE_ID:
        raise ValueError("Apple lookup returned the wrong app")
    version = app.get("version")
    if not isinstance(version, str) or not version:
        raise ValueError("Apple lookup omitted the public version")
    return version


def ready_for_release(pending, fetch=lookup):
    if not isinstance(pending.get("version"), str) or not pending["version"]:
        raise ValueError("pending website update has no version")
    versions = {country: public_version(fetch(country)) for country in COUNTRIES}
    return all(version == pending["version"] for version in versions.values()), versions


def main():
    pending = json.loads(Path(sys.argv[1]).read_text())
    ready, versions = ready_for_release(pending)
    print(f"Expected {pending['version']}; public US={versions['us']}, CA={versions['ca']}; ready={ready}")
    if output := os.environ.get("GITHUB_OUTPUT"):
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"ready={str(ready).lower()}\n")


if __name__ == "__main__":
    main()
