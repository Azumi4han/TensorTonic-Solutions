So, basically there is a simple version which is more expensive to compute, and few more versions that are like optimizations. 

First non-optimized version is to use just "expf" to calculate tanh. 
Second version is much optimized but still is expensive is using "tanhf" function. 
Third version is to use stride so instead of launching one thread per element (which can mean millions of threads for a big array), you launch a fixed, smaller grid that fits the GPU well, and each thread walks through the array in steps.

Fourth instead of loading/storing one float (4 bytes) per instruction, load and store four floats at once (float4 = 16 bytes).