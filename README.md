# Gpu allocator

## install
```bash
$ pip install configure_gpu
```

This is a package for allocating gpu memory to prevent clogging the gpu memory.

## Usage
```python
# tensorflow import
import tensorflow as tf

# gpu allocator package
from configure_gpu import gpu_allocator

# configuring gpu
gpu_memory_allocator(tf, percentage_allocation=0.95)

```
