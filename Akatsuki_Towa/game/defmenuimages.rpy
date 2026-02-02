###dialogue boxes############################################
image dialoguewindow:
    Crop((162,212,45,45), "avg_a1screen.png")
    alpha .75

layeredimage namebox:
    always "images_free/namebox_under.png"
    always Crop((200,5,64,37), "avg_a1screen.png")

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

image optionsmenuscreen:
    "images_free/options_background.png"

###buttons / other###########################################
image mainmenu_button:
    Crop((68,306,150,46), "atlas_JournalBeta.png")

image booktab1:
    Crop((757,192,243,37), "atlas_JournalBeta.png")

image booktab2:
    Crop((227,314,238,37), "atlas_JournalBeta.png")

image backbutton:
    Crop((0,268,245,37), "atlas_JournalBeta.png")

image bookpage:
    Crop((463,423,190,152), "atlas_JournalBeta.png")

image underline:
    Crop((256,478,16,4), "atlas_JournalBeta.png")

image check_foreground:
    Crop((445,192,24,24), "atlas_JournalBeta.png")

image check_selected_foreground:
    Crop((483,62,24,24), "atlas_JournalBeta.png")


###scrollbar###########################################
image horizontal_scrollbar_thumb_idle_pc:
    "gui/scrollbar/horizontal_scrollbar_thumb_idle.png" 
    zoom .5

image horizontal_scrollbar_thumb_hover_pc:
    "gui/scrollbar/horizontal_scrollbar_thumb_hover.png" 
    zoom .5

image vertical_scrollbar_thumb_idle_pc:
    "gui/scrollbar/vertical_scrollbar_thumb_idle.png" 
    zoom .5

image vertical_scrollbar_thumb_hover_pc:
    "gui/scrollbar/vertical_scrollbar_thumb_hover.png" 
    zoom .5

image horizontal_scrollbar_thumb_idle_mobile:
    "gui/scrollbar/horizontal_scrollbar_thumb_idle.png" 
    zoom 1.1

image horizontal_scrollbar_thumb_hover_mobile:
    "gui/scrollbar/horizontal_scrollbar_thumb_hover.png" 
    zoom 1.1

image vertical_scrollbar_thumb_idle_mobile:
    "gui/scrollbar/vertical_scrollbar_thumb_idle.png" 
    zoom 1.1

image vertical_scrollbar_thumb_hover_mobile:
    "gui/scrollbar/vertical_scrollbar_thumb_hover.png" 
    zoom 1.1
     
###Quick Menu (Mobile Ver) ###################################
image quickbutton:
    Crop((41,62,60,48), "atlas_JournalBeta.png")

image quickbutton_pressed:
    Crop((196,96,60,48), "atlas_JournalBeta.png")
