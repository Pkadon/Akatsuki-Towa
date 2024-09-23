label defmenuimages:

###dialogue boxes############################################
image dialoguewindow:
    Crop((162,212,45,45), "avg_a1screen.png")
    alpha .75

image namebox:
    Crop((200,5,64,37), "avg_a1screen.png")


###Main Menu#################################################
###background######
image mainmenuscreen:
    "loading00.png"
    xysize (840, 480)
    matrixcolor TintMatrix("#FFFFFF")
image sceneselect = "mainmenuscreen"

###logo animation######
image akatsukilogo2:
    Crop((0,331,502,178), "atlas_loading.png")
    zoom .85
image towani:
    "images_free/towani2.png"
    pause 1.0
    "images_free/towani.png" with Dissolve(1.0, alpha=True)
image towa:
    "sc085_01_i256.png"
    anchor (.5,.5)
    xpos 0.68
    ypos 1.5
    zoom 1.5
    rotate -20
    pause 1.0
    ease 1.0 ypos .925 


###buttons / other###########################################
image booktab1:
    Crop((757,192,243,37), "atlas_JournalBeta.png")

image booktab2:
    Crop((227,314,238,37), "atlas_JournalBeta.png")

image backbutton:
    Crop((0,268,245,37), "atlas_JournalBeta.png")

image bookpage:
    Crop((463,423,190,152), "atlas_JournalBeta.png")

image altbutton:
    Crop((635,340,322,51), "atlas_JournalBeta.png")
     
    
    
return
