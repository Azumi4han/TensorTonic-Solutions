What is np.linalg.norm ? Why not just use default np.sqrt and np.absolute? 

Linalg norm computes exact norm that assignment requires us to compute.
Another reason why we shouldn't use np.sqrt and np.absolute here, is because it computes element-wise operations for a = [3, 4] it produces [3, 4] again (the absolute values). It does not sum the squares first, so it is not a vector norm at all!

And it also does more calls that it supposed to do, therefore it's much slower. 

Link: [https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)



**Key differences between Cosine similarity and Euclidean:**

Euclidean distance is affected by magnitude. Vectors [1,0][1,0] and [100,0][100,0] have large Euclidean distance but cosine similarity of 1.

Cosine similarity is affected only by direction. It treats [1,2,3][1,2,3] and [2,4,6][2,4,6] as identical.



**When to use which:**

- Cosine similarity: text similarity, recommendation systems, comparing embeddings
- Euclidean distance: spatial data, clustering when magnitude matters