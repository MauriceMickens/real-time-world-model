# Environment Setup

## Python Virtual Environment

The project uses a Python virtual environment (`.venv`) to isolate dependencies.

### Initial Setup

Run the setup script to create and configure the environment:

```bash
./setup_env.sh
```

This will:
- Create a virtual environment (if it doesn't exist)
- Install/upgrade pip
- Detect NVIDIA GPU and install PyTorch with appropriate CUDA support
- Fall back to CPU-only PyTorch if no GPU is detected

### Activating the Environment

```bash
source .venv/bin/activate
```

### Deactivating the Environment

```bash
deactivate
```

## CUDA Requirements

**Note:** This project requires CUDA-capable GPU hardware for experiments.

- Experiments use `torch.cuda` and require GPU support
- NVTX annotations require CUDA-capable PyTorch
- Nsight Systems profiling requires NVIDIA GPU

If you're on a machine without CUDA (e.g., macOS):
- The environment will install CPU-only PyTorch
- You'll need to run experiments on a machine with CUDA support (e.g., cloud GPU instance)
- Or reinstall PyTorch with CUDA when on a CUDA-capable machine

### Installing PyTorch with CUDA (on CUDA-capable machine)

Check your CUDA version:
```bash
nvidia-smi
```

Install PyTorch for your CUDA version:
```bash
# For CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# For CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

Verify CUDA availability:
```bash
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}'); print(f'Device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')"
```

## Running Experiments

Once the environment is set up and activated:

```bash
# Example: Week 1 Day 3 benchmark
python phases/phase-0-inference-physics/week-1/benchmarks/day3_gemm_vs_memcpy.py
```

## Nsight Systems Profiling

To capture profiler traces with Nsight Systems:

```bash
# Install Nsight Systems (if not already installed)
# Download from: https://developer.nvidia.com/nsight-systems

# Run with profiling
cd phases/phase-0-inference-physics/week-1/profiles
nsys profile --trace=cuda,nvtx,osrt -o day3_$(date +%Y%m%d_%H%M%S) python ../../benchmarks/day3_gemm_vs_memcpy.py
```
