# management/commands/fetch_problems.py
import requests
from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import Problem  # Replace 'your_app' with your actual app name

class Command(BaseCommand):
    help = 'Fetch problems from Codeforces API and store them in the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--start',
            type=int,
            default=1,
            help='Start index for problem fetching (default: 1)'
        )
        parser.add_argument(
            '--end',
            type=int,
            default=100,
            help='End index for problem fetching (default: 100)'
        )

    def handle(self, *args, **options):
        start_index = options['start']
        end_index = options['end']
        
        self.stdout.write(f"Fetching problems from index {start_index} to {end_index}")
        
        try:
            # Fetch problems from Codeforces API
            response = requests.get('https://codeforces.com/api/problemset.problems')
            response.raise_for_status()
            
            data = response.json()
            
            if data['status'] != 'OK':
                self.stderr.write(f"API Error: {data.get('comment', 'Unknown error')}")
                return
            
            problems = data['result']['problems']
            self.stdout.write(f"Retrieved {len(problems)} problems from API")
            
            # Process and save problems
            saved_count = 0
            with transaction.atomic():
                for problem_data in problems:
                    # Skip problems without contestId or index
                    if 'contestId' not in problem_data or 'index' not in problem_data:
                        continue
                    
                    # Create or update problem
                    problem, created = Problem.objects.update_or_create(
                        contest_id=problem_data['contestId'],
                        index=problem_data['index'],
                        defaults={
                            'name': problem_data.get('name', ''),
                            'rating': problem_data.get('rating'),
                            'tag': self.get_primary_tag(problem_data.get('tags', []))
                        }
                    )
                    
                    if created:
                        saved_count += 1
                    
                    # Print progress
                    if saved_count % 100 == 0:
                        self.stdout.write(f"Saved {saved_count} problems...")
            
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully fetched and saved {saved_count} problems to database"
                )
            )
            
        except requests.exceptions.RequestException as e:
            self.stderr.write(f"Network error: {e}")
        except Exception as e:
            self.stderr.write(f"Unexpected error: {e}")

    def get_primary_tag(self, tags):
        """Get the primary tag from a list of tags"""
        if not tags:
            return None
        
        # You can customize this logic based on your preference
        # Here we just return the first tag
        return tags[0]