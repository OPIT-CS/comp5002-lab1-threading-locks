# lab1_performance.py
import sys
import threading
import time

NUM_THREADS = 4
CPU_COUNT = 20_000_000  # Adjust if too slow/fast on your machine
IO_SLEEP_DURATION = 0.5  # Seconds

# ==================================
# Task Functions
# ==================================


def cpu_bound_task(n):
    """Performs a CPU-intensive calculation."""
    # --- TODO: Task 3 - Implement CPU-bound task ---
    # Example:
    # total = 0
    # for i in range(n):
    #     total += i
    # return total
    # --- End TODO ---
    pass  # Remove pass when implemented


def io_bound_task(duration):
    """Simulates an I/O-bound task waiting for 'duration' seconds."""
    # --- TODO: Task 3 - Implement I/O-bound task ---
    # time.sleep(duration)
    # --- End TODO ---
    pass  # Remove pass when implemented


# ==================================
# Timing Functions
# ==================================


def measure_time(func, *args):
    """Measures execution time of a function."""
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    return end_time - start_time


def run_sequential(target_func, num_tasks, *args):
    """Runs the same workload num_tasks times sequentially."""
    for _ in range(num_tasks):
        target_func(*args)


# ==================================
# Thread Execution Function
# ==================================


def run_threaded(target_func, num_threads, *args):
    """Runs target_func once in each of num_threads threads."""
    threads = []
    # --- TODO: Task 3 - Implement threaded execution ---
    # for _ in range(num_threads):
    #     t = threading.Thread(target=target_func, args=args)
    #     threads.append(t)
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()
    # --- End TODO ---
    return None


def gil_status():
    """Returns the CPython GIL state when the interpreter exposes it."""
    checker = getattr(sys, "_is_gil_enabled", None)
    if checker is None:
        return "unknown"
    return "enabled" if checker() else "disabled"


# ==================================
# Main Execution Logic
# ==================================

if __name__ == "__main__":
    print("Starting performance comparison...")
    print(f"Python: {sys.version.split()[0]} ({sys.implementation.name})")
    print(f"GIL: {gil_status()}")
    print(f"Number of tasks/threads: {NUM_THREADS}")
    print("-" * 30)

    # --- CPU-Bound Task ---
    print("CPU-Bound Task:")
    # Sequential and threaded cases perform the same number of tasks.
    seq_cpu_time = measure_time(
        run_sequential, cpu_bound_task, NUM_THREADS, CPU_COUNT
    )
    print(f"  Sequential: {seq_cpu_time:.4f} seconds")
    threaded_cpu_time = measure_time(
        run_threaded, cpu_bound_task, NUM_THREADS, CPU_COUNT
    )
    print(f"  Threaded:   {threaded_cpu_time:.4f} seconds")
    if seq_cpu_time > 0 and threaded_cpu_time > 0:
        print(f"  Speedup:    {seq_cpu_time / threaded_cpu_time:.2f}x")
    print("-" * 30)

    # --- I/O-Bound Task ---
    print("I/O-Bound Task:")
    # Sequential and threaded cases perform the same number of tasks.
    seq_io_time = measure_time(
        run_sequential, io_bound_task, NUM_THREADS, IO_SLEEP_DURATION
    )
    print(
        f"  Sequential: {seq_io_time:.4f} seconds "
        f"(Expected ~{IO_SLEEP_DURATION * NUM_THREADS:.2f}s)"
    )
    threaded_io_time = measure_time(
        run_threaded, io_bound_task, NUM_THREADS, IO_SLEEP_DURATION
    )
    print(
        f"  Threaded:   {threaded_io_time:.4f} seconds "
        f"(Expected ~{IO_SLEEP_DURATION:.2f}s)"
    )
    if seq_io_time > 0 and threaded_io_time > 0:
        print(f"  Speedup:    {seq_io_time / threaded_io_time:.2f}x")
    print("-" * 30)

    print("Performance comparison finished.")
