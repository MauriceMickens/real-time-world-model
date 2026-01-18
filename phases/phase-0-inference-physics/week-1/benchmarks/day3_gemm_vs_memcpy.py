import torch
import nvtx

torch.backends.cuda.matmul.allow_tf32 = True
torch.set_float32_matmul_precision("high")

DEVICE = "cuda"
DTYPE  = torch.float16

# Choose sizes that fit on A10G and show scaling clearly
SIZES = [1024, 2048, 4096, 8192]
WARMUP = 5
ITERS  = 10

def time_cuda(fn, stream=None):
    if stream is None:
        stream = torch.cuda.current_stream()
    start = torch.cuda.Event(enable_timing=True)
    end   = torch.cuda.Event(enable_timing=True)

    # warmup
    for _ in range(WARMUP):
        fn()
    stream.synchronize()

    # timed
    start.record(stream)
    for _ in range(ITERS):
        fn()
    end.record(stream)
    end.synchronize()

    ms = start.elapsed_time(end) / ITERS
    return ms

def main():
    assert torch.cuda.is_available()

    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"DTYPE: {DTYPE}")
    print(f"WARMUP={WARMUP} ITERS={ITERS}")
    print("")

    print("=== GEMM (A@B) avg ms ===")
    for N in SIZES:
        with nvtx.annotate(f"gemm_alloc_{N}"):
            A = torch.randn((N, N), device=DEVICE, dtype=DTYPE)
            B = torch.randn((N, N), device=DEVICE, dtype=DTYPE)

        def gemm():
            with nvtx.annotate(f"gemm_{N}"):
                _ = A @ B

        ms = time_cuda(gemm)
        print(f"N={N:5d}  gemm_ms={ms:8.3f}")

    print("")
    print("=== H2D memcpy avg ms (size scales with N^2) ===")
    for N in SIZES:
        # pinned host tensor
        with nvtx.annotate(f"h2d_alloc_{N}"):
            x_cpu = torch.empty((N, N), dtype=DTYPE, pin_memory=True).normal_()
            x_gpu = torch.empty((N, N), dtype=DTYPE, device=DEVICE)

        def h2d():
            with nvtx.annotate(f"h2d_{N}"):
                x_gpu.copy_(x_cpu, non_blocking=True)

        ms = time_cuda(h2d)
        mb = x_cpu.numel() * x_cpu.element_size() / 1e6
        gbps = (mb/1000.0) / (ms/1000.0)  # decimal GB/s
        print(f"N={N:5d}  h2d_ms={ms:8.3f}  size_MB={mb:8.3f}  GBps={gbps:6.2f}")

if __name__ == "__main__":
    main()
