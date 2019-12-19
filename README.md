# PyVisualOdometry
Python implementation of Visual Odometry algorithms from http://rpg.ifi.uzh.ch/

# Chapter 1 - Overview
@mhoegger
[Lecture 1](http://rpg.ifi.uzh.ch/docs/teaching/2019/01_introduction.pdf) Slides 54 - 78
- Definition of Visual Odometry
- Differences between VO, VSLAM and SFM
- Needed assumptions for VO
- Illustrate building blocks

# Chapter 2 - Optics
@joelbarmettlerUZH
[Lecture 2](http://rpg.ifi.uzh.ch/docs/teaching/2019/02_image_formation_1.pdf) Slides 1 - 48
- What is a blur circle
- Derive thin lense equation and perform the pinhole approximation
- Define vanishing points and lines
- Prove that parallel lines intersect at vanishing points
- How to build an Ames room
- Derive a relation between field of view and focal length

# Chapter 3 - Camera Projection
@joelbarmettlerUZH
[Lecture 2](http://rpg.ifi.uzh.ch/docs/teaching/2019/02_image_formation_1.pdf) Slides 48 - 66
- Perspective projection equation
- lense distortion 
- World to camera projection

# Chapter 4 - Camera Calibration
@mhoegger
[Lecture 3](http://rpg.ifi.uzh.ch/docs/teaching/2019/03_image_formation_2.pdf) Slides 1 - 64
- Describe the general PnP problem and derive the behavior of its solutions
- Explain the working principle of the P3P algorithm
- Explain and derive the DLT & the minimum number of point correspondences it requires
- Define central and non central omnidirectional cameras
- What kind of mirrors ensure central projection

# Chapter 5 - Image Filtering
@joelbarmettlerUZH
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

# Chapter 6 - Point Feature Detection (Harris & Shi-Tomasi)
@joelbarmettlerUZH
[Lecture 5](http://rpg.ifi.uzh.ch/docs/teaching/2019/05_feature_detection_1.pdf) Slides 1 - 65
- Explain what is template matching and how it is implemented?
- Explain what are the limitations of template matching? Can you use it to
recognize cars?
- Illustrate the similarity metrics SSD, SAD, NCC, and Census transform?
- What is the intuitive explanation behind SSD and NCC?
- Explain what are good features to track? In particular, can you explain what are
corners and blobs together with their pros and cons?
- Explain the Harris corner detector? In particular:
- - Use the Moravec definition of corner, edge and flat region.
- - Show how to get the second moment matrix from the definition of SSD and first order
approximation (show that this is a quadratic expression) and what is the intrinsic
interpretation of the second moment matrix using an ellipse?
- - What is the M matrix like for an edge, for a flat region, for an axis-aligned 90-degree
corner and for a non-axis—aligned 90-degree corner?
- - What do the eigenvalues of M reveal?
- - Can you compare Harris detection with Shi-Tomasi detection?
- - Can you explain whether the Harris detector is invariant to illumination or scale
changes? Is it invariant to view point changes?
- - What is the repeatability of the Harris detector after rescaling by a factor of 2?

# Chapter 7 - Point Feature Description & Matching (FAST, SIFT, SURF)
@joelbarmettlerUZH
[Lecture 6](http://rpg.ifi.uzh.ch/docs/teaching/2019/06_feature_detection_2.pdf) Slides 1 - 79
- How does automatic scale selection work?
- What are the good and the bad properties that a function for automatic scale
selection should have or not have?
- How can we implement scale invariant detection efficiently? (show that we can
do this by resampling the image vs rescaling the kernel).
- What is a feature descriptor? (patch of intensity value vs histogram of oriented
gradients). How do we match descriptors?
- How is the keypoint detection done in SIFT and how does this differ from Harris?
- How does SIFT achieve orientation invariance?
- How is the SIFT descriptor built?
- What is the repeatability of the SIFT detector after a rescaling of 2? And for a 50
degrees viewpoint change?
- Illustrate the 1st to 2nd closest ratio of SIFT detection: what’s the intuitive
reasoning behind it? Where does the 0.8 factor come from?

# Chapter 8 - Stereovision, Trinagulation, Feature Correspondance, Disparity Map
@mhoegger
[Lecture 7](http://rpg.ifi.uzh.ch/docs/teaching/2019/07_multiple_view_geometry_1.pdf) Slides 1 - 74
- Can you relate Structure from Motion to 3D reconstruction? In what they differ?
- Can you define disparity in both the simplified and the general case?
- Can you provide a mathematical expression of depth as a function of the baseline, the disparity and the focal
length?
- Can you apply error propagation to derive an expression for depth uncertainty? How can we improve the
uncertainty?
- Can you analyze the effects of a large/small baseline?
- What is the closest depth that a stereo camera can measure?
- Are you able to show mathematically how to compute the intersection of two lines (linearly and non-linearly)?
- What is the geometric interpretation of the linear and non-linear approaches and what error do they minimize?
- Are you able to provide a definition of epipole, epipolar line and epipolar plane?
- Are you able to draw the epipolar lines for two converging cameras, for a forward motion situation, and for a
side-moving camera?
- Are you able to define stereo rectification and to derive mathematically the rectifying homographies?
- How is the disparity map computed?
- How can one establish stereo correspondences with subpixel accuracy?
- Describe one or more simple ways to reject outliers in stereo correspondences.
- Is stereo vision the only way of estimating depth information? If not, are you able to list alternative options?

# Chapter 9 - Structure from Motion
@mhoegger
[Lecture 8](http://rpg.ifi.uzh.ch/docs/teaching/2019/08_multiple_view_geometry_2.pdf) Slides 1 - 43
- What's the minimum number of correspondences required for calibrated SFM and why?
- Are you able to derive the epipolar constraint?
- Are you able to define the essential matrix?
- Are you able to derive the 8-point algorithm?
- How many rotation-translation combinations can the essential matrix be decomposed into?
- Are you able to provide a geometrical interpretation of the epipolar constraint?
- Are you able to describe the relation between the essential and the fundamental matrix?
- Why is it important to normalize the point coordinates in the 8-point algorithm?
- Describe one or more possible ways to achieve this normalization.
- Are you able to describe the normalized 8-point algorithm?
- Are you able to provide quality metrics for the essential matrix estimation?

# Chapter 10 - RANSAC & Bundle Adjustment
@mhoegger
[Lecture 8](http://rpg.ifi.uzh.ch/docs/teaching/2019/08_multiple_view_geometry_2.pdf) Slides 44 - 88
[Lecture 9](http://rpg.ifi.uzh.ch/docs/teaching/2019/09_multiple_view_geometry_3.pdf) Slides 1 - 7
- Why do we need RANSAC?
- What is the theoretical maximum number of combinations to explore?
- After how many iterations can RANSAC be stopped to guarantee a given success probability?
- What is the trend of RANSAC vs. iterations, vs. the fraction of outliers, vs. the number of points
to estimate the model?
 How do we apply RANSAC to the 8-point algorithm, DLT, P3P?
- How can we reduce the number of RANSAC iterations for the SFM problem?

# Chapter 11 - Visual Odometry / Visual SLAM
@mhoegger
[Lecture 9](http://rpg.ifi.uzh.ch/docs/teaching/2019/09_multiple_view_geometry_3.pdf) Slides 8 - 61
[Lecture 10](http://rpg.ifi.uzh.ch/docs/teaching/2019/10_multiple_view_geometry_4.pdf) Slides 1 - 29
- Are you able to define Bundle Adjustment (via mathematical expression and
illustration)?
- Are you able to describe hierarchical and sequential SFM for monocular VO?
- What are keyframes? Why do we need them and how can we select them?
- Are you able to define loop closure detection? Why do we need loops?
- Are you able to provide a list of the most popular open source VO and VSLAM
algorithms?
- Are you able to describe the differences between feature-based methods and
direct methods?
- How do we benchmark VO/SLAM algorithms?
- Along which axes can we evaluate them?
- Benchmarking accuracy: Can we use the end pose error? What are ATE and RTE?
- How can we quantify Efficiency? And Robustness?

# Chapter 12 - Feature Trackings
@joelbarmettlerUZH
[Lecture 11](http://rpg.ifi.uzh.ch/docs/teaching/2019/11_tracking.pdf) Slides 1 - 76
- Are you able to illustrate tracking with block matching?
- Are you able to explain the underlying assumptions behind differential methods,
derive their mathematical expression and the meaning of the M matrix?
- When is this matrix invertible and when not?
 What is the aperture problem and how can we overcome it?
- What is optical flow?
- Can you list pros and cons of block-based vs. differential methods for tracking?
- Are you able to describe the working principle of KLT?
- Are you able to derive the main mathematical expression for KLT?
- What is the Hessian matrix and for which warping function does it coincide to
that used for point tracking?
- Can you list Lukas-Kanade failure cases and how to overcome them?
- How does one get the initial guess?
- Can you illustrate the coarse-to-fine Lucas-Kanade implementation?
- Can you illustrate alternative tracking procedures using point features?

# Chapter 13 - Dense 3D Reconstruction
@joelbarmettlerUZH
[Lecture 12a](http://rpg.ifi.uzh.ch/docs/teaching/2019/12a_3D_reconstruction.pdf) Slides 1 - 47
- Are you able to describe the multi-view stereo working principle?
(aggregated photometric error)
- What are the differences in the behavior of the aggregated photometric
error for corners, flat regions, and edges?
 What is the disparity space image (DSI) and how is it built in practice?
- How do we extract the depth from the DSI?
- How do we enforce smoothness (regularization) and how do we
incorporate depth discontinuities (mathematical expressions)?
- What happens if we increase lambda (the regularization term)? What if
lambda is 0? And if lambda is too big?
- What is the optimal baseline for multi-view stereo?
- What are the advantages of GPUs?

# Chapter 14 - Place Recognition
@mhoegger
[Lecture 12b](http://rpg.ifi.uzh.ch/docs/teaching/2019/12b_recognition.pdf) Slides 1 - 51
- What is an inverted file index?
- What is a visual word?
- How does K-means clustering work?
- Why do we need hierarchical clustering?
- Explain and illustrate image retrieval using Bag of Words.
- Discussion on place recognition: what are the open challenges and what
solutions have been proposed?

# Chapter 15 - Deep Learning
@None
[Lecture 12c](http://rpg.ifi.uzh.ch/docs/teaching/2019/12c_Deep_Learning_Tutorial.pdf) Slides 1 - 71

# Chapter 16 - Visual inertial fusion
@mhoegger
[Lecture 13](http://rpg.ifi.uzh.ch/docs/teaching/2019/13_visual_inertial_fusion.pdf) Slides 1 - 50
- Why is it recommended to use an IMU for Visual Odometry?
- Why not just an IMU?
- How does a MEMS IMU work?
- What is the drift of an industrial IMU?
- What is the IMU measurement model?
- What causes the bias in an IMU?
- How do we model the bias?
- How do we integrate the acceleration to get the position formula?
- What is the definition of loosely coupled and tightly coupled visual inertial
fusions?
- How can we use non-linear optimization-based approaches to solve for visual
inertial fusion?

# Chapter 17 - Visual inertial fusion
@joelbarmettlerUZH
[Lecture 14](http://rpg.ifi.uzh.ch/docs/teaching/2019/14_event_based_vision.pdf) Slides 1 - 72
- What is a DVS and how does it work?
- What are its pros and cons vs. standard cameras?
- Can we apply standard camera calibration techniques?
- How can we compute optical flow with a DVS?
- Could you intuitively explain why we can reconstruct the intensity?
- What is the generative model of a DVS and how to derive it?
- What is a DAVIS sensor?
- What is the focus maximization framework and how does it work? What is its
advantage compared with the generative model?
- How can we get color events?
