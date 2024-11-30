import csv
from pandas_memory import pandas_benchmark
from polars_memory import polars_benchmark
from duckdb_memory import duckdb_benchmark
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

if __name__ == '__main__':
    csv_files = ['data/data_100.csv', 'data/data_10000.csv', 'data/data_1000000.csv', 'data/data_2000000.csv']

    duckdb_memory = duckdb_benchmark(csv_files)
    pandas_memory = pandas_benchmark(csv_files)
    polars_memory = polars_benchmark(csv_files)

    all_memory = pandas_memory + polars_memory + duckdb_memory

    with open('benchmark_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['csv_file', 'library', 'read_mem']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in all_memory:
            writer.writerow({
                'csv_file': row[0],
                'library': row[1],
                'read_mem': row[2],
            })

    print("Benchmark results written to benchmark_results.csv")