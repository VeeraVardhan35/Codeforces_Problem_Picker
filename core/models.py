from django.db import models
from django.contrib.auth.models import User

class Problem(models.Model):
    TAG_CHOICES = [
        ("dp", "Dynamic Programming"),
        ("greedy", "Greedy"),
        ("math", "Math"),
        ("graphs", "Graphs"),
        ("trees", "Trees"),
        ("implementation", "Implementation"),
        ("strings", "Strings"),
        ("brute_force", "Brute Force"),
        ("sortings", "Sortings"),
        ("binary_search", "Binary Search"),
        ("number_theory", "Number Theory"),
        ("combinatorics", "Combinatorics"),
        ("geometry", "Geometry"),
        ("bitmasks", "Bitmasks"),
        ("probabilities", "Probabilities"),
        ("dsu", "DSU"),
        ("constructive", "Constructive"),
        ("two_pointers", "Two Pointers"),
        # add more if needed
    ]

    contest_id = models.IntegerField()
    index = models.CharField(max_length=5)
    name = models.CharField(max_length=255, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES, null=True, blank=True)

    class Meta:
        unique_together = ['contest_id', 'index']

    @property
    def url(self):
        return f"https://codeforces.com/problemset/problem/{self.contest_id}/{self.index}"
    
    def __str__(self):
        return f'{self.contest_id}{self.index} - {self.name}'



class SeenProblems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'problem']
