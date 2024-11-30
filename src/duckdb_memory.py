import time

import duckdb
from memory_profiler import memory_usage
import gc
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def benchmark_memory(func, *args, **kwargs) -> float:
    """
        Measure the peak memory usage of a function.

        Args:
            func (callable): The function to benchmark.
            *args: Positional arguments to pass to the function.
            **kwargs: Keyword arguments to pass to the function.

        Returns:
            float: The peak memory usage in MB.
    """
    gc.collect()
    mem_usage = memory_usage((func, args, kwargs), interval=0.001)
    time.sleep(0.1)
    return max(mem_usage) - min(mem_usage)


def duckdb_benchmark(csv_files: [str]) -> [(str, str, float)]:
    """
    Benchmark memory usage for reading CSV files using duckdb.

    Args:
        csv_files (List[str]): List of CSV file paths.

    Returns:
        List[Tuple[str, str, float]]: List of tuples containing file path, library name, and memory usage.
    """
    mem_usages = []
    output_dir = '../benchmark_outputs'
    os.makedirs(output_dir, exist_ok=True)

    logging.info("Starting duckdb benchmark")

    for csv_file in csv_files:
        logging.info(f"Benchmarking with file: {csv_file}")

        try:
            # Reading
            read_mem = benchmark_memory(duckdb.read_csv, csv_file)
            logging.info(f"Read memory: {read_mem}")

            mem_usages.append((csv_file, 'duckdb', read_mem))
        except duckdb.IOException as e:
            logging.error(f"IO Error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    return mem_usages
