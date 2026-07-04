#!/usr/bin/env python3
"""Regenerate app/data.js from data/regions.json (the single source of truth).
Run this after editing regions.json:  python3 build.py"""
import json, os

here = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(here, "data", "regions.json")))
out = ("// AUTO-GENERATED from ../data/regions.json — do not edit by hand.\n"
       "window.CALENDER_DATA = " + json.dumps(data, indent=2) + ";\n")
open(os.path.join(here, "app", "data.js"), "w").write(out)

pop = sum(1 for r in data["regions"] if r["status"] == "populated")
dist = sum(len(r["districts"]) for r in data["regions"])
print(f"Built app/data.js — {len(data['regions'])} regions ({pop} populated), {dist} districts.")
