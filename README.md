# PyVisualOdometry
Python implementation of Visual Odometry algorithms from http://rpg.ifi.uzh.ch/

# Chapter 1 - Overview
[Lecture 1](http://rpg.ifi.uzh.ch/docs/teaching/2019/01_introduction.pdf) Slides 54 - 78
- Definition of Visual Odometry
- Differences between VO, VSLAM and SFM
- Needed assumptions for VO
- Illustrate building blocks

# Chapter 2 - Optics
[Lecture 2](http://rpg.ifi.uzh.ch/docs/teaching/2019/02_image_formation_1.pdf) Slides 1 - 48
- What is a blur circle
- Derive thin lense equation and perform the pinhole approximation
- Define vanishing points and lines
- Prove that parallel lines intersect at vanishing points
- How to build an Ames room
- Derive a relation between field of view and focal length

# Chapter 3 - Camera Projection
[Lecture 2](http://rpg.ifi.uzh.ch/docs/teaching/2019/02_image_formation_1.pdf) Slides 48 - 66
- Perspective projection equation
- lense distortion 
- World to camera projection

# Chapter 4 - Camera Calibration
[Lecture 3](http://rpg.ifi.uzh.ch/docs/teaching/2019/03_image_formation_2.pdf) Slides 1 - 64
- Describe the general PnP problem and derive the behavior of its solutions
- Explain the working principle of the P3P algorithm
- Explain and derive the DLT & the minimum number of point correspondences it requires
- Define central and non central omnidirectional cameras
- What kind of mirrors ensure central projection

# Chapter 5 - Image Filtering
[Lecture 4](http://rpg.ifi.uzh.ch/docs/teaching/2019/04_filtering.pdf) Slides 1 - 63
- Explain the differences between convolution and correlation.
- Explain the differences between a box filter and a Gaussian filter.
- Explain why should one increase the size of the kernel of a Gaussian filter if is
large (i.e. close to the size of the filter kernel.
- Explain when would we need a median & bilateral filter.
- Explain how to handle boundary issues.
- Explain the working principle of edge detection with a 1𝐷 signal.
- Explain how noise does affect this procedure.
- Explain the differential property of convolution.
- Show how to compute the first derivative of an image intensity function along 𝑥
and 𝑦?
- Explain why the Laplacian of Gaussian operator is useful.
- List the properties of smoothing and derivative filters.
- Illustrate the Canny edge detection algorithm.
- Explain what non-maxima suppression is and how it is implemented.