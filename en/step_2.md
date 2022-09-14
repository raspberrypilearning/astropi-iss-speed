## Use Exif data to find a time difference

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
An <span style="color: #0faeb0">**exchangeable image file format (Exif)**</span> is a standard that sets formats for image and sound files, and various tags that can be stored within the file. These tags can include the time the photo was taken, the location it was taken at, and the type of camera that was used.
</p>

To collect Exif data from a photograph, you need a Python library called `exif`.

--- task ---

Open the Thonny Python IDE, and click on **Tools** > **Manage packages**, then search for and install the `exif` library. 

--- /task ---

[[[thonny-install-package]]]

--- task ---

In the main code editor, add the following two lines of code.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 
line_highlights: 1-2
---
from exif import Image
from datetime import datetime
--- /code ---

--- /task ---

--- task ---

Save your file as `iss_speed.py`.

--- /task ---

--- task ---

You will need some images taken from the Astro Pi unit on the ISS. You can download a zip file of the photos by clicking on [this link](https://rpf.io/p/en/astropi-iss-speed-go){:target='_blank'}. Once the photos have been downloaded, you can right-click on the folder in your **Downloads** and unzip the folder. **Then move the photos to the same place that you have saved your python script.**

--- /task ---

--- task ---

Beneath your `import` lines, create a function to find the time that a photo was taken. It will take one argument, which will be the photo's file name.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 
line_highlights: 5
---
from exif import Image
from datetime import datetime


def get_time(image):
--- /code ---

--- /task ---

--- task ---

The image needs to be opened and then converted to an `Image` object, which is part of the `exif` package.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 
line_highlights: 6-7
---
from exif import Image
from datetime import datetime


def get_time(image):
    with open(image, 'rb') as image_file:
        img = Image(image_file)
--- /code ---

--- /task ---

--- task ---

You can have a look at all the Exif data that is saved in the image file.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 
line_highlights: 8-9
---
from exif import Image
from datetime import datetime


def get_time(image):
    with open(image, 'rb') as image_file:
        img = Image(image_file)
        for data in img.list_all():
            print(data)
--- /code ---

--- /task ---

--- task ---

You can test out your function using one of the image names that you have downloaded. This needs to be a string.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 
line_highlights: 12
---
from exif import Image
from datetime import datetime


def get_time(image):
    with open(image, 'rb') as image_file:
        img = Image(image_file)
        for data in img.list_all():
            print(data)


get_time('photo_00154.jpg')
--- /code ---

--- /task ---

--- task ---

Run your code, and you should see some output that looks like this:

```
image_width
image_height
make
model
x_resolution
y_resolution
resolution_unit
datetime
y_and_c_positioning
_exif_ifd_pointer
_gps_ifd_pointer
compression
jpeg_interchange_format
jpeg_interchange_format_length
exposure_time
exposure_program
photographic_sensitivity
exif_version
datetime_original
datetime_digitized
components_configuration
shutter_speed_value
brightness_value
metering_mode
flash
maker_note
flashpix_version
color_space
pixel_x_dimension
pixel_y_dimension
_interoperability_ifd_Pointer
exposure_mode
white_balance
gps_latitude_ref
gps_latitude
gps_longitude_ref
gps_longitude
```

--- /task ---

--- task ---

The data that is needed for this project is `datetime_original`. This can be saved as a string, and then it needs to be converted to a `datetime` object so that calculations can be performed on it.

--- code ---
---
language: python
filename: iss_speed.py
line_numbers: true
line_number_start: 
line_highlights: 8-10, 12
---
from exif import Image
from datetime import datetime


def get_time(image):
    with open(image, 'rb') as image_file:
        img = Image(image_file)
        time_str = img.get("datetime_original")
        time = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
    return time


print(get_time('photo_00154.jpg'))
--- /code ---

When you run this code, you should see output that looks like this:

```
2022-01-14 15:25:07
```
--- /task ---

--- save ---
