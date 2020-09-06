# Voxelize

Voxelize is a tool which convert pixel in images in voxel. It takes 6 images as input and produce a 3D model as a combination of this images.

## How to use

The images must be a rapresentation of the 6 sides of a 3D model (front, back, top, bottom, right and left).

```
python voxelize.py <img front> <img right> <img left> <img top> <img bottom> <img back>
```

The following example explain how to define the 6 images

![Image example](https://github.com/MarcoCiaramella/Voxelize/blob/master/tutorial/usage_images.png)

The images orientation must follow the x,y,z system as shown in the example.

And this is the output

![Image output](https://github.com/MarcoCiaramella/Voxelize/blob/master/tutorial/result.png)
