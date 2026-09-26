# Lab 1 Analysis Questions

## Environment

Record the environment used for your measurements:

- Python version:
- Python implementation:
- Reported GIL status from `lab1_performance.py`:

If the GIL is reported as disabled, note that you are using free-threaded CPython and that the CPU-bound result may differ from the standard GIL-enabled behavior discussed in the module.

## Task 1 Demonstrate Race Condition

Observed incorrect Actual count values (list 1–2 examples):
- 
- 

## Task 2 Fix Race Condition with Lock

Observation after adding the lock:


## Task 4 Analysis Questions

1. **Race Condition** Briefly explain why `lab1_unsafe_counter.py` produced incorrect results. What specific mechanism caused the errors? Refer to atomicity and interleaving.

2. **Lock Correction** How did adding `threading.Lock` in `lab1_safe_counter.py` fix the race condition? What principle does the lock enforce?

3. **CPU-Bound Performance**
   - Sequential CPU time: [enter recorded time]
   - Threaded CPU time: [enter recorded time]
   - Comparison and explanation: Did threading provide a significant speedup? Explain why or why not, referencing the GIL state reported by your interpreter. The sequential and threaded cases perform the same number of CPU tasks.

4. **I/O-Bound Performance**
   - Sequential I/O time: [enter recorded time]
   - Threaded I/O time: [enter recorded time]
   - Comparison and explanation: Did threading provide a significant speedup? Explain why or why not, referencing the GIL and how it interacts with blocking I/O operations. The sequential and threaded cases perform the same number of I/O tasks.

5. **Conclusion** Based on your results, summarise when using Python `threading` is beneficial for performance in standard GIL-enabled CPython and when it is not. If you used free-threaded CPython, explain how that changes the CPU-bound result.
