# lab1_unsafe_counter.py
import threading
import time

# Shared global variable
global_counter = 0
NUM_THREADS = 10
INCREMENTS_PER_THREAD = 100_000  # Each thread will attempt this many increments

def unsafe_increment():
    """
    Reads the global counter, increments it, and writes it back,
    repeatedly, without synchronization to induce a race condition.
    """
    global global_counter
    for _ in range(INCREMENTS_PER_THREAD):
        current_value = global_counter
        # Optional tiny sleep increases the chance of thread interleaving
        # time.sleep(0.000001)
        global_counter = current_value + 1

def run_threads():
    """
    Creates and runs multiple threads targeting unsafe_increment.
    Waits for all threads to complete.
    """
    threads = []
    # --- TODO: Task 1 - Create and start threads ---
    # 1) Create NUM_THREADS thread objects targeting unsafe_increment and append to 'threads'.
    # for _ in range(NUM_THREADS):
    #     t = threading.Thread(target=unsafe_increment)
    #     threads.append(t)
    #
    # 2) Start all threads.
    # for t in threads:
    #     t.start()
    #
    # 3) Join all threads.
    # for t in threads:
    #     t.join()
    # --- End TODO ---
    print("All threads finished.")

if __name__ == "__main__":
    print(f"Starting counter at: {global_counter}")
    start_time = time.perf_counter()

    run_threads()

    end_time = time.perf_counter()
    expected_count = NUM_THREADS * INCREMENTS_PER_THREAD
    actual_count = global_counter

    print(f"Expected count: {expected_count}")
    print(f"Actual count:   {actual_count}")
    print(f"Difference:     {expected_count - actual_count}")
    print(f"Execution time: {end_time - start_time:.4f} seconds")

    if expected_count == actual_count:
        print("Result: Counter value is correct.")
    else:
        print("Result: Race condition detected! Counter value is incorrect.")
