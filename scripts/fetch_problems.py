# scripts/fetch_problems.py
import requests
from core.models import Problem

def run():
    url = "https://codeforces.com/api/problemset.problems"
    response = requests.get(url).json()
    
    if response["status"] != "OK":
        print("Failed to fetch problems")
        return

    problems = response["result"]["problems"]
    for p in problems:
        Problem.objects.get_or_create(
            contest_id=p.get("contestId"),
            index=p["index"],
            defaults={
                "name": p.get("name"),
                "rating": p.get("rating"),
                "tag": p.get("tag", []),
            }
        )
    print(f"Inserted {len(problems)} problems into DB")
