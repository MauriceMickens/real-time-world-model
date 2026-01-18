Below is a complete, portfolio-grade README you can drop directly into your new repo.
It is written to give Cursor (and future you) crystal-clear context about:

- what this project is
- why it exists
- how it is structured
- where you are right now (Week 1)
- how progress is evaluated

This is intentionally systems-first, not hype-driven.

---

# Real-Time World Model Inference Engine

A first-principles GPU inference systems project.
Not a demo. Not a benchmark. A rigorously measured, explainable, real-time inference engine.

---

## 🎯 North Star

Build deep, first-principles mastery of GPU inference systems by delivering a real-time world model inference engine that is:

- Low latency (≥ 24 FPS)
- Deterministic (identical inputs → identical outputs)
- Interactive (responds to user actions)
- Explainable (every millisecond accounted for)
- Defensible (behavior can be justified with profiler evidence)

This repository is the single source of truth for all experiments, measurements, write-ups, and artifacts that lead to that engine.

---

## 🚩 The Flagship Vision

**Real-Time World Model Inference Engine**

An interactive AI-generated world that:

- Streams video frames in real time (≥ 24 FPS)
- Responds to user actions (keyboard / programmatic input)
- Maintains deterministic replay given identical inputs
- Runs efficiently on modern cloud GPUs (A10 / A100 / H100)

This is not about model novelty.

It is about systems quality.

---

## 🔒 Why This Project Exists (Anchor)

Modern AI performance is no longer dominated by model architecture alone.

In production:

- Latency dominates UX
- GPU time dominates cost
- Poor measurement dominates bad decisions

World models amplify these constraints:

- Stateful inference
- Temporal dependencies
- Memory growth
- Synchronization complexity
- Determinism requirements

Very few engineers can:

**measure → reason → optimize inference without guessing**

This project is designed to build exactly that capability.

---

## 🧠 How This Project Is Structured (Mental Model)

This work is intentionally layered.
Each phase builds on locked understanding from the previous one.

**Measurement → Control → Predictability → Interactivity → Optimization → Scaling**

No phase is skipped.
No intuition is trusted without evidence.

---

## 🧪 Phase 0 — Inference Physics & Measurement Literacy

**Weeks 1–2**

### Purpose

Build the ability to look at a profiler trace and explain it without guessing.

### Success Means

- GPU timelines stop looking like noise
- Kernel names start meaning something
- Measurements are trusted over intuition
- Latency changes can be predicted before running code

---

### ✅ Week 1 — GPU Time Fundamentals (CURRENT WEEK)

**Focus:** What "latency" actually means on a GPU

#### Objectives

- Understand CPU orchestration vs GPU execution
- Internalize asynchronous execution
- Learn where time is actually spent

#### Work

- Profile isolated operations:
  - GEMM (matmul)
  - Host → Device memcpy
  - Synchronization (cudaDeviceSynchronize)
- Use:
  - `torch.cuda.Event`
  - Nsight Systems (basic usage)
  - Introduce NVTX ranges

#### Deliverables

- Microbenchmark scripts
- `.nsys-rep` profiler traces
- Written answers to:
  - What dominates time?
  - What surprised me?
  - Where CPU vs GPU timing diverges

**Status:** In progress  
This repo currently lives here.

---

### Week 2 — Bandwidth vs Compute vs Overhead

**Focus:** Building intuition, not speedups

- Compute-bound vs memory-bound
- Kernel execution vs launch overhead
- Synchronization costs

**Deliverable:** a Phase 0 write-up that explains why results look the way they do.

---

## ⚙️ Phase 1 — Minimal Inference Runtime

**Weeks 3–4**

### Purpose

Own inference behavior before adding model complexity.

### Success Means

- No hidden synchronization
- No accidental allocations
- Deterministic execution
- Precise end-to-end latency accounting

---

### Week 3 — Explicit Runtime Construction

- Manual control of allocation, streams, sync
- Structured NVTX ranges
- Minimal inference loop

### Week 4 — Determinism & Precision Measurement

- RNG control
- Deterministic CUDA ops
- Replay verification
- Variance measurement (not just averages)

---

## 🌍 Phase 2 — World Model Integration

**Weeks 5–6**

### Purpose

Treat a large model as a workload, not a black box.

### Success Means

- Predictable per-frame latency
- Stable long-run behavior
- Clear understanding of memory growth

---

### Week 5 — Model as a Workload

- Integrate HY-World / Open-Sora
- Profile frame generation loop
- Identify hidden sync points

### Week 6 — Predictability & Control

- Long-sequence profiling
- Cache/state analysis
- Drift detection

---

## 🎮 Phase 3 — Interactivity & Deterministic Replay

**Week 7**

### Purpose

Combine systems correctness with real-time interaction.

### Success Means

- User actions injected without latency spikes
- Deterministic replay of identical action sequences

---

## 🚀 Phase 4 — Performance Optimization

**Week 8**

### Purpose

Engineer tradeoffs explicitly.

### Success Means

- Sustained real-time performance
- Measured improvements
- No "mystery speedups"

### Techniques

- Mixed precision
- Compilation
- Memory reuse

---

## 🧠 Phase 5 — Scaling & Advanced Systems (Optional)

**Weeks 9–10**

- Multi-GPU inference
- Quantization (INT8 / FP8)
- Higher resolutions / longer horizons

**Success = understanding why scaling helps or hurts.**

---

## ✅ What This Project Explicitly Says "Yes" To

- Measurement-first work
- Small, controlled experiments
- Profilers and timelines over intuition
- Writing explanations in my own words
- Repeating weeks if understanding is incomplete

## ❌ What This Project Explicitly Says "No" To

- Blind optimization
- Framework magic without understanding
- "It seems faster" reasoning
- Copy-paste benchmarks
- Skipping fundamentals

---

## 📌 Current State

- **Week:** 1
- **Phase:** 0 — Inference Physics & Measurement Literacy
- **Focus:** Where GPU time actually goes

All new work should respect this structure.

---

## 🧭 How Cursor Should Treat This Repo

- This project is week-structured
- Do not jump ahead conceptually
- Explanations matter as much as code
- Measurement artifacts are first-class outputs
- Assume the goal is systems mastery, not feature velocity

---

If you want, next we can:

- Generate the Week 1 markdown file to match this README
- Define a repo directory structure that enforces this discipline
- Create a Cursor project instruction block you can pin

Just say the word.
