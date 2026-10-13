"""Release website copy only after Apple exposes the exact build version."""

import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from release.check_live import ready_for_release, public_version


def apple(version, app_id=6796368335, bundle_id="com.freddv2.booktionary"):
    return {"resultCount": 1, "results": [
        {"trackId": app_id, "bundleId": bundle_id, "version": version}]}


class ReleaseGateTests(unittest.TestCase):
    def test_both_public_storefronts_must_show_exact_version(self):
        pending = {"version": "1.0.12"}
        ready, _ = ready_for_release(pending, lambda _: apple("1.0.12"))
        self.assertTrue(ready)
        ready, versions = ready_for_release(pending, lambda country: apple(
            "1.0.12" if country == "us" else "1.0.11"))
        self.assertFalse(ready)
        self.assertEqual(versions["ca"], "1.0.11")
        ready, _ = ready_for_release(pending, lambda _: apple("1.0.13"))
        self.assertFalse(ready)

    def test_wrong_app_or_missing_result_fails_closed(self):
        with self.assertRaises(ValueError):
            public_version(apple("1.0.12", app_id=1))
        with self.assertRaises(ValueError):
            public_version({"resultCount": 0, "results": []})
