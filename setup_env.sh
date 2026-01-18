#!/bin/bash
# Setup script for Python environment with PyTorch and CUDA support

set -e

echo "=== Setting up Python environment ==="

# Check if venv exists, create if not
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate venv
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Check for NVIDIA GPU and CUDA
if command -v nvidia-smi &> /dev/null; then
    echo ""
    echo "Detected NVIDIA GPU. Checking CUDA version..."
    nvidia-smi --query-gpu=driver_version --format=csv,noheader
    echo ""
    echo "Installing PyTorch with CUDA support..."
    echo "If you need a specific CUDA version, see: https://pytorch.org/get-started/locally/"
    echo ""
    echo "Installing PyTorch for CUDA 12.1 (default)..."
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    
    echo ""
    echo "To verify CUDA is available, run: python -c 'import torch; print(torch.cuda.is_available())'"
else
    echo ""
    echo "Warning: nvidia-smi not found. GPU may not be available."
    echo "Installing CPU-only PyTorch..."
    pip install torch torchvision torchaudio
fi

echo ""
echo "=== Environment setup complete ==="
echo "To activate the environment in the future, run: source .venv/bin/activate"
