# Day 3: GEMM vs Host→Device Memcpy Scaling

## Experiment

Compare scaling behavior of:
1. GEMM (matrix multiplication) - compute-bound
2. Host→Device memcpy - memory-bound

## Measurements

- CUDA events (ground-truth GPU timing)
- NVTX ranges for profiler annotation
- Nsight Systems capture (optional)

## Prediction vs Result

### Questions to Answer After Running

1. **Which grew faster with N: GEMM or H2D?**

   _Your answer here after running the benchmark_

2. **At what N (if any) does GEMM become larger than H2D?**

   _Your answer here after running the benchmark_

3. **Where were you wrong, and why?**

   _Your answer here after running the benchmark_

## Running the Benchmark

```bash
# Basic run
python phases/phase-0-inference-physics/week-1/benchmarks/day3_gemm_vs_memcpy.py

# With Nsight Systems profiling
cd phases/phase-0-inference-physics/week-1/profiles
nsys profile --trace=cuda,nvtx,osrt -o day3_$(date +%Y%m%d_%H%M%S) python ../../benchmarks/day3_gemm_vs_memcpy.py
```

## Results

### Output Summary

_Record your actual output here_

### Key Observations

_Add observations after analysis_
