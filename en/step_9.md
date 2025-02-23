## Improving your program


To refine your code and perhaps calculate a more accurate estimation of the speed of the ISS, you could try and investigate any of the following:

- Use a different feature detection [algorithm in OpenCV](https://docs.opencv.org/3.4/db/d27/tutorial_py_table_of_contents_feature2d.html){:target='_blank'}
- Choose a different number of feature matches to use
- Use more than two photos
- Check how long a photo takes to be written to disk to get a more accurate value for the time between photos 
- Does the curvature of the Earth have an effect on the actual distance values travelled?
- Does the height of the identified feature also have an effect?
- Does the angle of motion (diagonally across the frame) have a impact that needs to be corrected for?
-- If your matched features are clouds, can you compensate for the fact that they may be moving too?

