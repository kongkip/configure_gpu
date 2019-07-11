def gpu_memory_allocator(tf, percentage_allocation=0.95):
    
    config = tf.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = percentage_allocation
    session = tf.Session(config=config)
    return session