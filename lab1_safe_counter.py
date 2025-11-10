# lab1_safe_counter.py
import threading
import time

# Shared global variable
global_counter = 0
NUM_THREADS = 10
INCREMENTS_PER_THREAD = 100_000

# --- TODO: Task 2 - Create a Lock object ---
# counter_lock = threading.Lock()
# --- End TODO ---

def safe_increment():
    """
    Increments the global counter safely using a lock.
    """
    global global_counter
    for _ in range(INCREMENTS_PER_THREAD):
        # --- TODO: Task 2 - Use the lock to protect the critical section ---
        # with counter_lock:
        current_value = global_counter
        # time.sleep(0.000001)  # Optional small sleep
        global_counter = current_value + 1
        # --- End TODO ---

def run_threads():
    """
    Creates and runs multiple threads targeting safe_increment.
    Waits for all threads to complete.
    """
    threads = []
    # --- TODO: Task 2 - Create, start, and join threads ---
    # for _ in range(NUM_THREADS):
    #     t = threading.Thread(target=safe_increment)
    #     threads.append(t)
    # for t in threads:
    #     t.start()
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
        print("Result: Error! Counter value is incorrect despite lock.")
