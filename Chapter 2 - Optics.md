# Chapter 2 - Optics

In this article, we are goint to find out how an image is formed on an Image Plane. 

The overall principle is quite basic: An object reflects light that falls on an Image sensor, which captures the lights intensity and
therefore forms an image. To ensure that every part of the scenery only falls onto the optical sensor at one spot only, we can introduce
an optical barrier with a hole in it which ensures that - for each point in our scene - only light rays with a particular 
angle fall onto the image plane.
We can therefore create an upside down copy of the scenery on our optical sensor. The smaller the barriers hole, the more angle-selective
our camera becomes, the sharper the image appears. The hole is also known as aperture, or pinhole. 

![Pinhole Model, p. 7]()

An ideal pinhole camera has - mathematically - an infinitely small pinhole to have an infinitely sharp image. In practice, this comes in
hand with two problems: The smaller the pinhole, the less light we can capture on our sensor. Furhter, a pinhole smaller than 0.3mm will
cause lightwave interferreneces, making the image blurry again due to diffraction effects. 

To combat these issues, lenses are used. They have the property that they bundle lightrays coming from the same point in our scenery
into a (preferrably) single spot on the optical sensor. Lenses must fullfill two characteristics to be fitting camera lenses:
- 1. Light rays that travel through the optical center of the lens will not be deviated
- 2. Lightrays that fall parallel to the optical axis into the lens are focues in a so called "focal point" f behind the lens. 

With combining these two properties, we can derrie the "thin lense equation": From a single Object in our Scene at distanze Z and height A
in front of our lens, we can construct two lighrays: One passing through the optical center, the other entering the lens parallel
to the optical axis. 

To make the Object appear sharp, we have to ensure that both lighrays fall onto the same point on our optical sensor. Since the
focal point is given by the lens properties, we can not vary the focal length *f* (distance between focal point and lens). What we 
can change is the position of the optical sensor: We can either bring it closer or farther to lens. We call the distance to the
optical sensor *e*. 


With looking back at similarity triangles principles, we can see that The objects elevation *A* in respect to the position of the 
sensor crossing point *B* must be the same as the distance to the Object *z* in respect to the distance from the Lens to the 
Image Sensor *e*. We therefore conduct that *B/A = e/z*. 
As a second equation, we can conduct that *B/A* must also be equal to the ration *e-f / f*. To simplify, we can also write
*B/A = e/f - 1*.

![Thin Lens equation, p. 17]()

With combining these two equations, we get that *e/f - 1 = e/z* and finally **1/f = 1/z + 1/e**. Therefore, for a given
distance *z*, the object only appears sharp if the optical sensor is distance *e* away from the Lens.

It becomes clear that if we move an Object further away (increasing *z*), the distance e must be changed to make the object appear
sharp again. 
When the thin lens equation is not satisfied, the light rays do not intersect at the optical sensor, creating a blur circle which
is perceived as "unsharp". Only a blur circle with radius less than 1 Pixel gives a sharp image. 

The distance between the focal Plane (where the light rays at this distance actually meet) and the image plane (optical sensor)
is called *S*, the diameter of a Pinhole is referred to as *L*. For simple pinhole cameras, this gives us a blur circle 
radius of **R = LxS / 2xe**. 

![Blur circle, p. 19]()

Why is this relevant? Well, for large distances to our object *z* we can approximate our lens-based camera model with a pinhole camera,
since the distance to any world object is much much larger than the focal length or the Lens size. Typically, smartphone cameras
have focal lengths of 1.7mm and Lens sizes of < 1 cm. We can therefore focus at objects at infinity. This implies that the 
focal plane for objects that are inifinitely far away moves to the focal point. 

We can therefore safely aproximate that the focal length *f* is equal to the optical sensor distance *e*: *e ~= f*. This makes the 
relation between our objects elevation *A* and the point on the Image plane *B* even simpler: We don't have to consider two
lightrays but just one falling straight throught the pinhole. This also leaves us with a simpler equation to
find the point *B* where a object at distce *z* and elevation *A* would fall on the Image sensor: *B/A = f/z*, or *B = f/z x A*. 
Therefore, Objects twice as far away appear half as large in on the optical sensor. 

![Pinhole approximation, p. 22]()

The distance range in which an object appears sharp (R < 1 Pixel) is called the Depth of Field (DoF). The smaller the apperture, 
the larger the Depth of Field, but the less light we have left for the Image Sensor. 
Further, the lens size at a fixed focal length defines the biggest Angle the camera can perceive, the Field of View (FoV). 
We can also increase/decrease the FoV by changing the focal length: Larger focal lengths intuitively result in a more narrow
viewing angle. The ratio between the focal length and the FoW angle *p* can be simply expressed via a tangential relation:
*tan(p/2) = W/2 x f*

![Pinhole approximation, p. 22]()

An interesting consequence of perspecitve projection is that parallel lines in the 3D world are no longer perceived as parallel on the 2D image
plane. Neither are angles preserved. Further, it seems that parallel lines in an image will cross at some point, the so called
vanishing point. With tracking all these vanishing points, we can fit a vanishing line through them: A line on which all vanishing
points land. We observe two vanihshing lines: one for horizontal and one for vertical parallel lines. 

To understand why this happens, we make a quick excursion to homogeneous coordinates. We are used to having a euclidean coordinate
system with (x,y)-Coordinates. But in a perspective sense, we also have a third dimension, the distance, leaving us with
the coordinates (x, y, w). We can translate from the euclidean system to the homogenous one with interpreting the euclidean coordinate
system as a plane on w=1, m aking (x,y) = (x,y,1). 
We can also map homogenous coordinates back into euclidean ones by defining (x,y) = (x/w, y/w). 
To represent a point that is infinitely far away, we'd need a point (x,y) = (oo, oo) in the euclidean system. The same point
represented in homogenous coordinates would just be (x,y,0). 
We can therefore proof that two parallel lines will intersect at infinity. Let's define two parallel lines: *L1 = Ax + By + C = 0* and 
*L2 = Ax + By + D = 0*. Since C must be different from D (otherwise the lines would be the same), there is no solution for the
euclidean system. However, in the homogenous form, we have the corresponding line definitions *L1 = Ax/w + By/w + C = 0* and 
*L2 = Ax/w + By/w + D = 0*, so for (x, y, 0) the equation is satisfied. Therefore, two lines meet at some point (x,y,0), which is
somewhere at infinity since *w* = 0.



