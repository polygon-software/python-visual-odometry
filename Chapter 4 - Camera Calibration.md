# Chapter 4 - Camera Calibration

This article discusses how one can derive the perspective of a camera by the given landmarks. Also, it explains how 
many of such landmarks are needed to be able to get the correct perspective and also explains the different methods 
for calibrated and uncalibrated cameras. Uncalibrated cameras are ones for which we don't know the accurate intrinsic 
parameters. We explain how camera calibration works, so how we can find the intrinsics and what aspects are important 
for this.


## Perspective from *n* Points (PnP Problem)

The goal of Perspective from n Points algorithms is to find the pose of the camera in respective to the world reference 
frame. This means we want to find the six degrees of freedom describing the position and orientation of the camera. 
As input we have the landmarks in the world reference frame as well as their images on the the camera plane. 
In the case of a uncalibrated camera we additionally want to find out the camera's intrinsic parameters which we have 
discussed already in chapter >>>XY<<<.

Let's now find out how many point we need to get a unique solution. First we look into the case of a calibrated camera.

First for only one point for which we know the position in the world and the position on the image plane of the camera 
we have infinite possible solution since the camera can be placed all around the point in the world with an distance to it.

![image for only one point and inf solutions]

For two points we know the actual distance between the points in the world as well as for the ones on the image plane. 
Because of the for each camera fixed focal length we know the angle between the two point in the image plan and the 
camera. Therefore the camera can only places so that the world points lie in the two lines connecting the camera point 
with the two image points. As a result we know the geometric figure describing all possible position for the 
camerapoints has to be rotationally symetrical around the axis described by the line that intersects both world points. 
To find the exact geometrical figure we now inspect the figure that is rotated. On the plane that is rotated we the 
same condition has to be match that the word points are in the line through camrea and image point. 
The only figure that fulfills this condition the the circle. Therefore we have now found the correct geometrical 
figure in 3d that describes the possible location the camera can have when we have given 2 points. 
For a continoues reference frame this results still in a infinite number of possible positions but at least we 
knwo that it is bounded.

Let us now try it with three points.




