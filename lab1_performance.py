# lab1_performance.py
import threading
import time

NUM_THREADS = 4
CPU_COUNT = 100_000_000  # Adjust if too slow/fast on your machine
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
# Timing Function
# ==================================

def measure_time(func, *args):
    """Measures execution time of a function."""
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    return end_time - start_time

# ==================================
# Thread Execution Function
# ==================================

def run_threaded(target_func, num_threads, *args):
    """Runs the target_func in 'num_threads' threads."""
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

# ==================================
# Main Execution Logic
# ==================================

if __name__ == "__main__":
    print("Starting performance comparison...")
    print(f"Number of threads: {NUM_THREADS}")
    print("-" * 30)

    # --- CPU-Bound Task ---
    print("CPU-Bound Task:")
    # Sequential
    seq_cpu_time = measure_time(cpu_bound_task, CPU_COUNT)
    print(f"  Sequential: {seq_cpu_time:.4f} seconds")
    # Threaded
    threaded_cpu_time = measure_time(run_threaded, cpu_bound_task, NUM_THREADS, CPU_COUNT)
    print(f"  Threaded:   {threaded_cpu_time:.4f} seconds")
    if seq_cpu_time > 0 and threaded_cpu_time > 0:
        print(f"  Speedup:    {seq_cpu_time / threaded_cpu_time:.2f}x")
    print("-" * 30)

    # --- I/O-Bound Task ---
    print("I/O-Bound Task:")
    # Sequential
    seq_io_time = measure_time(io_bound_task, IO_SLEEP_DURATION * NUM_THREADS)  # Total sleep time
    print(f"  Sequential: {seq_io_time:.4f} seconds (Expected ~{IO_SLEEP_DURATION * NUM_THREADS:.2f}s)")
    # Threaded
    threaded_io_time = measure_time(run_threaded, io_bound_task, NUM_THREADS, IO_SLEEP_DURATION)
    print(f"  Threaded:   {threaded_io_time:.4f} seconds (Expected ~{IO_SLEEP_DURATION:.2f}s)")
    if seq_io_time > 0 and threaded_io_time > 0:
        print(f"  Speedup:    {seq_io_time / threaded_io_time:.2f}x")
    print("-" * 30)

    print("Performance comparison finished.")
