# Chapter 3 - Camera Projection

In the last chapter, we've seen how a Lens works. In this chapter, we are finding a mathematical model for converting
the (X,Y,Z)-Coordinates of an Object in our world to pixel coordinates (u,v) on an image. 

In this example, (u,v) are pixel coordinates measured from the top-left of an image. The center of our image is the Origin, or
principal point *O*. The focal length *f* is given as well as the Optical Center, e.g. the Center of the Lens *C*.

To convert from World to Pixel coordinates, we have to perform three steps:
- 1. Convert the world point (X,Y,Z) to a new coordinate system that has the cameras Optical Center *C* as the (0,0,0) Origin. We
do that via rigid body transformation, so Rotation R and translation t. 
- 2. Convert the resulting Camera Point to new coordinates in the same coordinate system on the Optical sensor, (x,y). The optical sensor is also 
referred to as "image plane"
- 3. Convert (x,y) to pixel coordinates (u,v). 

![World and pixel coordinates, p. 50]()

## From World to Camera

Given world coordinates (Xw, Yw, Zw), we want to find a new coordinates (Xc, Yc, Zc) which is just a new coordinate system
that has the Cameras Principal Point *O* as the origin point (0, 0, 0). 
This can be done using a rigid body transformation, so a combined rotation R and translation t. 
The matrix [R|t] is called the **Matrix of extrinsic parameters**. 

![World and Camera coordinates, p. 58]()

## From Camera to Image plane

We can map a point from the Camera Coordinate System, Pc = (Xc, Yc, Zc) to the Optical sensor p = (x, y) by using the concept of 
similarity triangles again, with thinking back to the pinhole approximation from the last chapter. 

Let's isolate the cameras x,y dimension and have a look at them seperatly. We see that Pc = (Xc, 0, Zc) projects into p = (x,0). 
We now need to find out the projections x coordinate. 
From the concept of similarity, we see that *x/f = Xc / Zc* must hold. Therefore, we can deduct that **x = fXc / Zc**. 
This also holds for the y-dimenion, of course: **y = fYc / Zc**. 

## From Camera to Pixel Coordinates
The first step is already done: with **x = fXc / Zc** and **y = fYc / Zc**, we bring the Camera coordinates to Image coordinates.
Now we only have to map them to Pixel coordinates by shifting them from the Origin *O = (u0, v0)* to the top-left (0,0) Pixel. We further introduce
a new parameter *ku* and *kv* that determines the scale of the pixels in both dimensions. We get the following u,v coordinates:

**u = u0 + ku * x**
**v = v0 + ku * y**

In combination with the previous results, we get 

**u = u0 + ku * fXc / Zc**
**v = v0 + ku * fYc / Zc**

We can now bring the point p = (u,v) into the previously seen homogeneous coordinates: p = (u,v) = l*(u,v,1). Expressed in matrix form,
we get 

![Matrix for u,v, p. 53]()

This matrix is called K, the **Matrix of intrinsic parameters**, or **calibration matrix**. It defines the internal properties
of the Camera: It's focal length and the resolution, as well as the scewing factors k, which can be assumed to be 1 for modern 
cameras with good build quality.

Given an image resolution of 640x480 Pixels and a focal length of 210 **pixels**, we get a matrix of intrisics:

```
[[ f   0  u0 ],
 [0    f  v0 ],
 [0    0  1  ]]
```
or, with numbers:
```
[[210  0  320],
 [0   210 240],
 [0    0   1 ]]
```

## From World to Pixel Coordinates

We can finally bring it all together by combining the matrix of intrinsics and extrinsics.

![Matrix KRt, p. 58]()

## Normalizing the Image Coordinates

Sometimes it can be handy to have a representation with focal length = 1. We can achieve this by an alternative 
representation: 

Since K-1 is just 

```
[[1/f  0   -u0 ],
 [ 0  1/f  -v0 ],
 [ 0   0    1  ]]
```

We can create a normalized system with multiplying (u, v, 1) with K-1. 

![Matrix uv1, p. 59]()

## Image distortion

As a final step, we take lens disrotion into account. Distortion is usually radial, meaning a pixels distortion depends
on its distance to the origin *O*. The radial distortion can either be positive (Barrel distortion) or negative (pincushion
distortion). In either case, we can describe the distortion with a quadratic model that maps the ideal, non-distorted (u,v)
coordinates from previously to the real, observed coordinates with distortion (ud, vd). 

Since the distortion is depending on the origin, we get the following equation:

![Distortion equation, p. 62]()

The amount of distortion depends on the cameras FoV and a potential misalignment between the Lens and the Optical Sensor. 

