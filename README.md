# COMP-5002 – Lab 1 • Basic Threading, Race Conditions, and Locks

**Module** Module 2. Concurrency: Threads & The Global Interpreter Lock  
**Objective** Implement basic threading, demonstrate race conditions, apply locks for synchronization, and compare threaded performance on I/O versus CPU-bound tasks.

## Prerequisites

- Python 3 installed.
- Git installed and basic familiarity with `clone`, `add`, `commit`, `push`.
- Understanding from Module 2:
  - Process vs Thread.
  - Thread creation and management (`threading.Thread`, `start()`, `join()`).
  - Race conditions and critical sections.
  - The Global Interpreter Lock (GIL) and its implications.
  - Basic locks (`threading.Lock`, `with` statement).

### Python environment note

The expected CPU-bound result assumes a standard GIL-enabled CPython interpreter. CPython 3.13+ also supports optional free-threaded builds where the GIL can be disabled. `lab1_performance.py` reports the Python version and, where the interpreter exposes it, the current GIL state. If the GIL is disabled, record that in `analysis.md` and explain why your CPU-bound result may differ from the standard expectation.

## Files Provided

- `README.md` this file
- `lab1_unsafe_counter.py` starter for demonstrating a race condition
- `lab1_safe_counter.py` starter for fixing the race with a lock
- `lab1_performance.py` starter for comparing CPU-bound and I/O-bound threading
- `analysis.md` where you answer the analysis questions

## Tasks

**General instructions**

- Clone the repository created for you by GitHub Classroom.
- Modify the `.py` files to complete the tasks.
- Answer the analysis questions in `analysis.md`.
- Commit frequently with meaningful messages.
- Push your final changes before the deadline.

---

### Task 1 — Demonstrate a race condition (`lab1_unsafe_counter.py`)

1. Open `lab1_unsafe_counter.py`.
2. Complete `run_threads`:
   - Create a list to hold `threading.Thread` objects.
   - Loop `NUM_THREADS` times, creating threads targeting `unsafe_increment`; append each to the list.
   - Start all threads.
   - Join all threads.
3. Run several times: `python lab1_unsafe_counter.py`.
4. Observe the output. Compare “Expected count” vs “Actual count”. Record one or two typical incorrect results in `analysis.md`.

The starter deliberately yields occasionally between the read and write inside `unsafe_increment`. This widens the race window so the unsafe interleaving is observable reliably across current CPython versions. Do not remove that yield while completing Task 1.

---

### Task 2 — Fix the race with a lock (`lab1_safe_counter.py`)

1. Open `lab1_safe_counter.py`.
2. Create a lock globally, for example `counter_lock = threading.Lock()`.
3. In `safe_increment`, use `with counter_lock:` to protect the complete read-modify-write sequence of `global_counter`.
4. Complete `run_threads` as in Task 1, but target `safe_increment`.
5. Run: `python lab1_safe_counter.py`.
6. Record whether the actual count now matches the expected count every run.

The safe starter uses the same periodic yield as the unsafe version so you are testing the lock under comparable interleaving pressure.

---

### Task 3 — Performance comparison (`lab1_performance.py`)

1. Open `lab1_performance.py`.
2. Implement `cpu_bound_task(n)`; a simple Python arithmetic loop is sufficient.
3. Implement `io_bound_task(duration)` using `time.sleep(duration)`.
4. Complete `run_threaded`:
   - Create one thread per task, each targeting `target_func`.
   - Start all threads.
   - Join all threads.
5. Run: `python lab1_performance.py`.
6. Record times for all four cases (Sequential CPU, Threaded CPU, Sequential I/O, Threaded I/O) in `analysis.md`.

The sequential and threaded measurements execute the same number of identical tasks. This makes the timing comparison fair: only the execution model changes.

---

### Task 4 — Analysis (`analysis.md`)

Answer based on your observations:

1. **Race condition** Explain why `lab1_unsafe_counter.py` produced incorrect results, referencing atomicity and interleaving.
2. **Lock correction** Explain how `threading.Lock` fixes the race and what principle it enforces.
3. **CPU-bound performance** Compare sequential vs threaded CPU times. State whether threading helped and why, referencing the GIL and the GIL state reported by your interpreter.
4. **I/O-bound performance** Compare sequential vs threaded I/O times. Explain any speedup and how the GIL interacts with blocking I/O.
5. **Conclusion** Summarise when Python `threading` helps performance in CPython and when it does not. If you used a free-threaded build, distinguish that result from standard GIL-enabled CPython.

---

## Submission

1. Save all `.py` changes.
2. Ensure `analysis.md` is complete.
3. Stage: `git add lab1_unsafe_counter.py lab1_safe_counter.py lab1_performance.py analysis.md` (or `git add .`)
4. Commit: `git commit -m "Complete Lab 1"`
5. Push: `git push origin main` (or your default branch)
6. Verify on GitHub that your files and `analysis.md` are updated.
