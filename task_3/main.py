import timeit

from pathlib import Path
from tabulate import tabulate
from bms import boyer_moore_search
from kmp import kmp_search
from rks import rabin_karp_search


# Отримуємо абсолютні шляхи до файлів
base_path = Path(__file__).parent
article_1_path = base_path / 'article_1.txt'
article_2_path = base_path / 'article_2.txt'

# Завантаження статей
with article_1_path.open('r', encoding='windows-1251') as file:
    article_1 = file.read()

with article_2_path.open('r', encoding='windows-1251') as file:
    article_2 = file.read()


patterns = ["Література", "алгоритм"]

def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=100)

results = {}
for pattern in patterns:
    results[pattern] = {
        "Boyer-Moore": (measure_time(boyer_moore_search, article_1, pattern), measure_time(boyer_moore_search, article_2, pattern)),
        "KMP": (measure_time(kmp_search, article_1, pattern), measure_time(kmp_search, article_2, pattern)),
        "Rabin-Karp": (measure_time(rabin_karp_search, article_1, pattern), measure_time(rabin_karp_search, article_2, pattern)),
    }

table_data = []
for pattern, result in results.items():
    for algo, times in result.items():
        table_data.append([pattern, algo, f"{times[0]:.6f}", f"{times[1]:.6f}"])

headers = ["Substring", "Algorithm", "Article 1 (sec)", "Article 2 (sec)"]
table = tabulate(table_data, headers, tablefmt="github")

print(table)