###dialogue boxes############################################
image dialoguewindow:
    Crop((162,212,45,45), "avg_a1screen.png")
    alpha .75

image namebox:
    Crop((200,5,64,37), "avg_a1screen.png")

###Choice Menu###############################################
layeredimage choicehover:
    always "dialoguewindow"
    always "images_free/choiceoverlay.png"

###Main Menu#################################################
###background######
image mainmenuscreen:
    "loading00.png"
    xysize (840, 480)
    matrixcolor TintMatrix("#FFFFFF")
image sceneselect = "mainmenuscreen"

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
     
###Quick Menu (Mobile Ver) ###################################
image quickbutton:
    Crop((41,62,60,48), "atlas_JournalBeta.png")

image quickbutton_pressed:
    Crop((196,96,60,48), "atlas_JournalBeta.png")
    
return
