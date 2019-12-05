# Chapter 4 - Camera Calibration

This article discusses how one can derive the perspective of a camera by the given landmarks. Also, it explains how 
many of such landmarks are needed to be able to get the correct perspective and also explains the different methods 
for calibrated and uncalibrated cameras. Uncalibrated cameras are ones for which we don't know the accurate intrinsic 
parameters. We explain how camera calibration works, so how we can find the intrinsics and what aspects are important 
for this.


## Perspective from *n* Points (PnP Problem)

The goal of Perspective from n Points algorithms is to find the pose of the camera in respect to the world reference 
frame. This means we want to find the six degrees of freedom describing the position and orientation of the camera. 
As input we have the landmarks in the world reference frame as well as their images on the the camera plane. 
In the case of a uncalibrated camera we additionally want to find out the camera's intrinsic parameters which we have 
discussed already in chapter >>>XY<<<.

Let's now find out how many point we need to get a unique solution. First we look into the case of a calibrated camera.

First for only one point for which we know the position in the world and the position on the image plane of the camera 
we have infinite possible solution. This is because the camera can be placed all around that point in the world 
with any distance from it.

![image for only one point and inf solutions]

For two points we know the actual distance between the points in the world as well as for the ones on the image plane. 
Because of the fixed focal length of the camera we know the angle between the two points in the image plan and the 
camera. Therefore the camera can only be at places where the world points lie on the two lines connecting the camera point 
with the two image points. As a result we know the geometric figure describing all possible position for the 
camerapoints has to be rotationally symmetrical around the axis described by the line that intersects both world points. 
To find the exact geometrical figure we now inspect the figure that is rotated. The only figure that fulfills 
the condition that the angle of the lines connetcing the world points with the camera points through the image point on 
a plane is the circle. Therefore we have now found the correct geometrical figure in 3D that describes the possible 
location the camera can have when we have given 2 points. It is called "spindel torus".
For a chitinous reference frame this results still in a infinite number of possible positions but at least we 
know that it is bounded.

Let us now try it with three points. Again we draw lines from the points in the world reference frame through tier 
image on the camera plane. Dependent on where we place the camera these lines can intersect each other. In the case 
where all three lines intersect in one single point we have found a valid place for the camera point to be. To derive 
how many soultions there are and how to find them we take advantage of the law of cosine. In the previously described 
sotiution situation we hav three different triangles with their cornes at two of the worl-points and one at the camera 
center. Also for these triangles two edges intersect the cameraplane at the image-points.The law of cosine states 
that for each trinagle the distance between the two image points is equal to the sum of the squared distance both edges conneting the image 
points with the camera center substracing the twice the product of the times the cosine of the angle at the cameracenter.






