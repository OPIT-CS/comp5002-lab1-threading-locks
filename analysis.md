# Lab 1 Analysis Questions

## Task 1 Demonstrate Race Condition

Observed incorrect Actual count values (list 1–2 examples):
- 
- 

## Task 2 Fix Race Condition with Lock

Observation after adding the lock:


## Task 4 Analysis Questions

1. **Race Condition** Briefly explain why the `unsafe_counter.py` script produced incorrect results. What specific mechanism caused the errors? Refer to atomicity and interleaving.

2. **Lock Correction** How did adding `threading.Lock` in `safe_counter.py` fix the race condition? What principle does the lock enforce?

3. **CPU-Bound Performance**
   - Sequential CPU time: [enter recorded time]
   - Threaded CPU time: [enter recorded time]
   - Comparison and explanation: Did threading provide a significant speedup? Explain why or why not, referencing the GIL.

4. **I/O-Bound Performance**
   - Sequential I/O time: [enter recorded time]
   - Threaded I/O time: [enter recorded time]
   - Comparison and explanation: Did threading provide a significant speedup? Explain why or why not, referencing the GIL and how it interacts with I/O operations.

5. **Conclusion** Based on your results, summarise when using Python `threading` is beneficial for performance in CPython and when it is not.
