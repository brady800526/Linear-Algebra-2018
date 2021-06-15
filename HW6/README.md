# Homework 6: Singular Value Decomposition

## Purpose:

Use Singular Value Decomposition to compress the image size.

## Summary:

![Singular Value Decomposition](img/LA_HW6_SVD.png)
Given any image, every image can be decomposed to U$\Sigma$V, and we can use SVD to compress image by use only part of the matrix to reconstruct the image.

### Problem 1

**A plot includes curve describing the relation of k and approxi- mation error**<br>
![K value equals to 1](img/LA_HW6_Problem1-1.png)

U and V<sup>T</sup> are orthogonal matrix, and Σ is diagonal matrix used as an index to enlarge/retract the vector. To reconstruct the image, we use matrix multiplication on U, VT and Σ. However, if we want to compress the image, we can only use part of the matrix. The Σ matrix from top left to right bottom represents the significance priority, we can take only one singular to construct matrix with U shape (2880, 1), Σ shape (1, 1) and V<sup>T</sup> shape (1, 1620), so on so forth.

This is the approximation and approximation error with only use one singular value.

![K value equals to 1](img/LA_HW6_Problem1-2.png)

This is the approximation and approximation with use 130 singular value.

<p float="left">
  <img src="img/LA_HW6_Problem1-k1.png" width=50% />
  <img src="img/LA_HW6_Problem1-k5.png" width=49% />
</p>

<p float="left">
  <img src="img/LA_HW6_Problem1-k50.png" width=49% />
  <img src="img/LA_HW6_Problem1-k150.png" width=49% /> 
</p>

<p float="left">
  <img src="img/LA_HW6_Problem1-k400.png" width=49% />
  <img src="img/LA_HW6_Problem1-k1050.png" width=49% /> 
</p>

<p float="left">
  <img src="img/LA_HW6_Problem1-k1289.png" width=49% />
</p>

Approximation Image with different k value 1, 5, 50, 150, 400, 1050, 1289

![Singular Value Decomposition](img/LA_HW6_Problem1-error.png)

Approximation Error on k

### Problem 2

**Analyze the rank of R channel of the provided image and explain how you analyze**
The non-zero number of $\Sigma$ equals the rank of the image, which is 1680.

### Problem 3

**Plots in page 6 but on G channel(A<sub>i,G</sub>, ∀1 ≤ i ≤ 5)**

<p float="left">
  <img src="img/LA_HW6_Problem3-A1.png" width=32% />
  <img src="img/LA_HW6_Problem3-A2.png" width=32% />
  <img src="img/LA_HW6_Problem3-A3.png" width=32% />
</p>
<p float="left">
  <img src="img/LA_HW6_Problem3-A4.png" width=32% />
  <img src="img/LA_HW6_Problem3-A5.png" width=32% />
  <img src="img/LA_HW6_Problem3-A.png" width=32% />
</p>

Approximation Image with first k value 1, 2, 3, 4, 5 and summation of previous image.

## Reference

- [Homework explaination powerpoint](https://drive.google.com/file/d/1nJTnZWUXystt_GLBlcdjIcqjsMGTicdz/view?fbclid=IwAR2X-o_JTXNZpV2jIuWlcPPorwUZbWmYBMjPd1sn4Zrm_qCksBCM8PssMTA)
