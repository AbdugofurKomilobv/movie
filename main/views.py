from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,template_name='index.html')


def toqmi_juftmi(son):
    if son % 2 == 0:
        return "Juft"
    else:
        return "Toq"

def sozlar_soni(matn):
    return len(matn.split())

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * faktorial(n - 1)
def musbat_sonlar(royxat):
    return [son for son in royxat if son > 0]


from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


from collections import Counter

def top_word(text):
    words = text.lower().split()
    counter = Counter(words)
    return counter.most_common(1)[0]
def divisible_filter(nums, n):
    return list(filter(lambda x: x % n == 0, nums))
def find_palindromes(words):
    return [w for w in words if w == w[::-1]]

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors
import re

def sum_of_digits_in_text(text):
    numbers = re.findall(r'\d+', text)
    return sum(int(n) for n in numbers)
def sort_by_length(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)


def read_in_chunks(filename, chunk_size=1000):
    with open(filename, 'rb') as f:
        while chunk := f.read(chunk_size):
            yield chunk
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
