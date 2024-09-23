label defavgimg:

###these are the insert images that appear in the middle of the screen during some cutscenes
### avg_img_005.png is not used as far as I am aware

### avg_img_007.png does not exist as far as I am aware 
### (the cutscene where it is called never showed an image in the actual game)

image Image1:
    Crop((0,0,384,512), "image_001.png")
    xcenter 0.5
    yanchor 1.0
    ypos 482

image Image8:
    Crop((0,168,384,344), "avg_img_001.png")
    xcenter 0.5
    yanchor 1.0
    ypos 399

image Image8001:
    Crop((0,219,512,293), "avg_img_002.png")
    xcenter 0.5
    yanchor 1.0
    ypos 374

image Image8002:
    Crop((0,219,512,293), "avg_img_003.png")
    xcenter 0.5
    yanchor 1.0
    ypos 374

image Image8003:
    Crop((0,219,512,293), "avg_img_004.png")
    xcenter 0.5
    yanchor 1.0
    ypos 374

###it wasn't ever called by a cutscene, guessing name just in case
image Image8004:
    Crop((0,219,512,293), "avg_img_005.png")
    xcenter 0.5
    yanchor 1.0
    ypos 374

image Image8005:
    Crop((0,219,512,293), "avg_img_006.png")
    xcenter 0.5
    yanchor 1.0
    ypos 374

### nothing was ever shown during this cutscene, and a file doesn't exist
### this would be avg_img_007.png if it existed
### using placeholder
image Image8006 = "images_free/8006.png"

image Image8007: 
    Crop((0,219,512,293), "avg_img_008.png")
    xcenter 0.5
    yanchor 1.0
    ypos 374

return