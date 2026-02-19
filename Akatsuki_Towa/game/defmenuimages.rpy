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

#Scene Select##
image book_backing:
    Crop((656,391,178,174), "atlas_JournalBeta.png")

image book_corners:
    Frame(Crop((634,218,118,118), "atlas_JournalBeta.png"), 56, 56)

image bracer_emblem:
    Crop((789, 795, 175, 229), "atlas_JournalBeta.png")#Crop((779, 795, 185, 229), "atlas_JournalBeta.png")
    alpha .50

image book_scrap:
    Crop((1,484,271,96), "atlas_JournalBeta.png")

image book_paper:
    Crop((451,414,204,168), "atlas_JournalBeta.png")

layeredimage book_paper_cropped:
    always:
        Solid('#00000000')
        xysize (204,168)
    always:
        Crop((463,424,192,145), "atlas_JournalBeta.png")
        pos (12,10)

image book_paper_strip:
    Crop((165,417,91,22), "atlas_JournalBeta.png")

#Never found a good place to put it, but leaving it defined here
layeredimage nametag:
    always:
        Crop((634,339,323,52), "atlas_JournalBeta.png")
    group name:
        attribute nacht default:
            Crop((0,418,163,20), "atlas_JournalBeta.png")
            #align (0.5,0.5)
            pos (30,16)

###buttons / other###########################################
image mainmenu_button:
    Crop((68,306,150,46), "atlas_JournalBeta.png")

image booktab1:
    Crop((755,192,243,37), "atlas_JournalBeta.png")

image booktab2:
    Crop((227,314,238,37), "atlas_JournalBeta.png")

image sidearea_tab:
    Crop((0,268,235,37), "atlas_JournalBeta.png")

layeredimage red_return_button_idle:
    always:
        Crop((754,231,106,106), "atlas_JournalBeta.png")
        rotate -60

layeredimage red_return_button_hover:
    always:
        Crop((861,231,106,106), "atlas_JournalBeta.png")
        rotate -60

image scenebutton:
    "images_free/gui/scenebutton.png"

image underline:
    Crop((256,478,16,4), "atlas_JournalBeta.png")

image check_foreground:
    Crop((445,192,24,24), "atlas_JournalBeta.png")

image check_selected_foreground:
    Crop((483,62,24,24), "atlas_JournalBeta.png")

image blue_confirm_button:
    Crop((41,63,60,46), "atlas_JournalBeta.png")
image blue_confirm_button_pressed:
    Crop((196,97,60,46), "atlas_JournalBeta.png")

#For some reason, the "pressed" image is more opaque than the "idle" image,
#So in order to avoid the button looking like it grows and shrinks when hovered,
#it seems to work better to have the bigger "pressed" image as a layer underneath the smaller "idle" image
image red_cancel_button_pressed:
    Crop((163,49,58,46), "atlas_JournalBeta.png")
layeredimage red_cancel_button:
    always:
        "red_cancel_button_pressed"
    always:
        Crop((258,89,58,46), "atlas_JournalBeta.png")


###scrollbar###########################################
image horizontal_scrollbar_thumb_idle_pc:
    "images_free/gui/scrollbar/horizontal_scrollbar_thumb_idle.png" 
    zoom .5

image horizontal_scrollbar_thumb_hover_pc:
    "images_free/gui/scrollbar/horizontal_scrollbar_thumb_hover.png" 
    zoom .5

image vertical_scrollbar_thumb_idle_pc:
    "images_free/gui/scrollbar/vertical_scrollbar_thumb_idle.png" 
    zoom .5

image vertical_scrollbar_thumb_hover_pc:
    "images_free/gui/scrollbar/vertical_scrollbar_thumb_hover.png" 
    zoom .5

image horizontal_scrollbar_thumb_idle_mobile:
    "images_free/gui/scrollbar/horizontal_scrollbar_thumb_idle.png" 
    zoom 1.1

image horizontal_scrollbar_thumb_hover_mobile:
    "images_free/gui/scrollbar/horizontal_scrollbar_thumb_hover.png" 
    zoom 1.1

image vertical_scrollbar_thumb_idle_mobile:
    "images_free/gui/scrollbar/vertical_scrollbar_thumb_idle.png" 
    zoom 1.1

image vertical_scrollbar_thumb_hover_mobile:
    "images_free/gui/scrollbar/vertical_scrollbar_thumb_hover.png" 
    zoom 1.1
