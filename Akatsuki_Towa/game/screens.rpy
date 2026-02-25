################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True
    color '#75CFEB'
    hover_color '#75EBDF'

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar None
    thumb Frame("horizontal_scrollbar_thumb_[prefix_]pc", 16,16)
    hover_sound "common_tag.ogg"

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar None
    thumb Frame("vertical_scrollbar_thumb_[prefix_]pc", 16,16)
    hover_sound "common_tag.ogg"

style slider:
    ysize gui.slider_size
    left_bar Frame("images_free/gui/slider/horizontal_slider_left.png", 3,3)
    left_gutter 2
    right_bar Frame("images_free/gui/slider/horizontal_slider_right.png", 3,3)
    thumb "images_free/gui/slider/horizontal_slider_thumb.png"
    thumb_align 0.5
    thumb_offset 2 #in order to even-out the Auto Advance slider

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen hotkeys():
    key "r" action ShowMenu('history')
    key "l" action ShowMenu('history')
    key "a" action Preference("auto-forward", "toggle")
    key "f" action Preference("auto-forward", "toggle")

screen say(who, what, char_id=None):
    style_prefix "say"

    use hotkeys
    
    #Updates the default renpy narrator character with the last used Character object
    #This is necessary to keep the namebox visible and consistent during fade-out transitions
    if not renpy.predicting():
        $ update_narrator(char_id) # this function can be found in deffunctions.rpy

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"



## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Frame("dialoguewindow", 25, 25)

    #Expand the frame to make it touch the edges of the screen
    #accounting for the transparent shadows
    left_margin -1
    right_margin -1
    bottom_margin -2

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    xminimum 224
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("namebox", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

    color "#FFFFFF"
    outlines [ (0, "#262525", absolute(2), absolute(1)) ]

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False
    line_spacing gui.dialogue_line_spacing

    color "#FFFFFF"
    outlines [ (0, "#262525", absolute(2), absolute(1)) ]

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        spacing 30
        for i in items:
            button:
                idle_background Frame("dialoguewindow", 25, 25)
                hover_background Frame("choicehover", 25, 25)
                xysize (750, 65)
                text i.caption:
                    xpos 11
                    yalign 0.5
                    size gui.choice_button_text_size
                    color "#FFFFFF"
                    outlines [ (0, "#262525", absolute(2), absolute(1)) ]
                hovered Play("sound", "common_tag.ogg")
                action [Play("sound", "common_tag_2.ogg"), i.action]

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos (178 if not renpy.variant('touch') else 188)
    yanchor 0.5

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if not persistent.hide_quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0
            yoffset 1

            textbutton quickhistorytext action ShowMenu('history')
            textbutton quickskiptext action Skip() alternate Skip(fast=True, confirm=True)
            textbutton quickautotext action Preference("auto-forward", "toggle")


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default persistent.hide_quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")

################################################################################
## Main and Game Menu Screens
################################################################################
## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yanchor 1.0
        if not renpy.variant("touch"):
            ypos .89
        else:
            ypos .86

        spacing gui.navigation_spacing

        if not main_menu and not _in_replay:
            textbutton _("Main Menu"):
                activate_sound None
                action MainMenu()

        else:
            textbutton _("Scene Select"):
                if main_menu:
                    activate_sound "other_7004.ogg"
                    action ShowMenu("episodelist")

                elif _in_replay:
                    activate_sound None
                    action EndReplay(confirm=True)

        if _in_replay:
            # It doesn't seem to store the history after a scene, maybe because they're "Replays"
            # So just hide the button from the main menu
            textbutton _("History") action ShowMenu("history")

        textbutton _("Preferences") action ShowMenu("preferences")

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):
            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit"):
                activate_sound None
                action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    background Frame('mainmenu_button', 0,0)
    xsize 150
    hover_sound "common_tag.ogg"
    activate_sound "common_tag_2.ogg"


style navigation_button_text:
    properties gui.text_properties("navigation_button")
    idle_color '#606060'
    hover_color '#000000'
    selected_color '#000000'


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

### Main Menu Music definitions
default persistent.mainmenu_music = "mainsong.ogg"

init python:
    def update_mainmenu_music():
        if not renpy.predicting():
            if main_menu:
                if persistent.mainmenu_music != 'none':
                    play_music(persistent.mainmenu_music, if_changed=True, fadein=config.main_menu_music_fadein)
                else:
                    #Because I'm using the "default" statement, I can't set the variable to None
                    #If the variable has been set to 'none', that means it's been set to "Mute", so this will stop the music.
                    renpy.music.stop()

screen main_menu():

    $ update_mainmenu_music()
                
    ## This ensures that any other menu screen is replaced.
    tag menu

    add "mainmenuscreen"

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    if show_popup:
        add "popup"
    if show_logo:
        add "main_akatsukilogo":
            anchor main_logo_anchor
            pos main_logo_pos
            zoom main_logo_zoom
    if show_logooverlay:
        add "logooverlay":
            anchor main_overlay_anchor
            pos main_overlay_pos
            zoom main_overlay_zoom

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 184
    yfill True

    background None

style main_menu_vbox:
    xalign 1.0
    xoffset -13
    xmaximum 525
    yalign 1.0
    yoffset -13

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

default persistent.freeze_animations = False

init python:
    #Opening the menu in the middle of a cutscene can make the "typewriter" sound effect get stuck on loop, so this makes sure it stops.
    def mute_typewriter():
        global typewriter_channels

        for ch in typewriter_channels:
            renpy.music.stop(channel=ch)

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    on "show" action Function(mute_typewriter)

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        #"Still" version
        if persistent.freeze_animations in [True, title]:
            #Bottom-right corner
            add "assembled_gear":
                anchor (232,231)
                pos (1.0,1.0)
            #Top-left corner
            add "assembled_gear":
                anchor (196,196)#(230,230)
                zoom -0.7
                pos (0.12,0.07)
        #Animated version
        #Again, not entirely sure why the coordinates for the animated version are so different.
        else:
            #Bottom-right corner
            add "assembled_gear_ani":
                anchor (0.6,0.6)
                pos (1.0,1.0) 
            #Top-left corner
            add "assembled_gear_ani":
                anchor (0.7,0.7)
                zoom -0.7
                pos (0.12,0.07) 

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"
        activate_sound "common_cancel.ogg"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 7
    top_padding 80

    background "optionsmenuscreen"

style game_menu_navigation_frame:
    xsize 184
    yfill True

style game_menu_content_frame:
    left_margin 9
    right_margin 14
    top_margin 7
    bottom_margin -5

    left_padding 18
    right_padding 10
    top_padding 1
    bottom_padding 3
    background Frame("dialoguewindow", 25, 25)

style game_menu_viewport:
    xsize (610 - gui.scrollbar_size)

style game_menu_vpgrid:
    xsize (610 - gui.scrollbar_size)

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

    ysize 378
    yalign 0.5
    xoffset 3

style game_menu_side:
    spacing 7

style game_menu_label:
    xpos 33
    ysize 79

style game_menu_label_text:
    size gui.title_text_size
    color "#FFFFFF"
    outlines [ (0, "#262525", absolute(2), absolute(1)) ]
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -2


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 33
    ypadding 2

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    python:
        if not renpy.predicting():
            #This lets the main menu music change while still in the Preference menu, instead of needing to close out of it for the new music to take effect.
            update_mainmenu_music()

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True
                spacing 10

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    xsize 250
                    style_prefix "check"
                    label _("Main Menu Music")

                    textbutton _("Akatsuki Main Theme") action SetVariable("persistent.mainmenu_music", "mainsong.ogg")
                    textbutton _("Ainsel Theme") action SetVariable("persistent.mainmenu_music", "ed9998.ogg")
                    textbutton _("Remiferia Theme") action SetVariable("persistent.mainmenu_music", "ed9999.ogg")
                    textbutton _("Miss You") action SetVariable("persistent.mainmenu_music", "ed7569.ogg")
                    textbutton _("Mute") action SetVariable("persistent.mainmenu_music", 'none')

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Advance Speed")

                    bar value Preference("auto-forward time"):
                        bar_invert True

                vbox:
                    vbox:
                        spacing 7

                        vbox:
                            label _("Music Volume")

                            hbox:
                                bar value Preference("music volume")

                        vbox:
                            xsize 500
                            style_prefix "check"
                            textbutton _("Cleanly Loop BGM {size=15}(takes effect on next track change){/size}"):
                                action ToggleVariable("persistent.loop_bgm")

                    label _("Sound Effect Volume")

                    hbox:
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)

                    vbox:
                        xfill True
                        spacing 7

                        vbox:
                            xsize 500
                            if not persistent.mute_typewriter:
                                label _("Typewriter Volume {size=18}(relative to Sound Effect Volume){/size}")
                                hbox:
                                    style_prefix "slider"
                                    bar value VariableValue("persistent.typewriter_volume", min=0, max=1.0, style='slider')
                        vbox:
                            xsize 500
                            style_prefix "check"
                            textbutton _("Mute Typewriter Sound"):
                                action ToggleVariable("persistent.mute_typewriter")


                    label _("Voice Volume")

                    hbox:
                        bar value Preference("voice volume")

                        if config.sample_voice:
                            textbutton _("Test") action Play("voice", config.sample_voice)

                    null height gui.pref_spacing

                    textbutton _("Mute All"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"

                    if not renpy.variant("touch"):
                        vbox:
                            xsize 500
                            style_prefix "check"
                            fixed:
                                xysize (0,8)
                            textbutton _("Hide Quick Menu during cutscenes"):
                                action ToggleVariable("persistent.hide_quick_menu")

                    vbox:
                        xsize 500
                        style_prefix "check"
                        label _("Freeze Preference Screen Animations")
                        hbox:
                            xsize 500
                            textbutton _("Nowhere") action SetVariable("persistent.freeze_animations", False)
                            textbutton _("Everywhere") action SetVariable("persistent.freeze_animations", True)
                            textbutton _("History Screen Only") action SetVariable("persistent.freeze_animations", "History")


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0
    color "#FFFFFF"
    outlines [ (0, "112042", absolute(2), absolute(1)) ]

style pref_vbox:
    xsize 148

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "check_[prefix_]foreground"

style radio_button_text:
    properties gui.text_properties("radio_button") xoffset 12

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "check_[prefix_]foreground"

style check_button_text:
    properties gui.text_properties("check_button") xoffset 12

style slider_slider:
    xsize 230

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 7

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 296


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        vbox:
            spacing 10
            for h in _history_list:
                vbox:
                    if h.who:
                        text [h.who + ":"]:
                            substitute False
                            xalign 0.0
                            color "#FDDC5C"
                            size gui.name_text_size

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False
                        xalign 0.0
                        if not renpy.variant('touch'):
                            xsize 595
                        else:
                            xsize 560
                        size gui.text_size

            if not _history_list:
                label _("The dialogue history is empty.")

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 10

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("R/L")
        text _("Opens the History menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("A/F")
        text _("Toggles dialogue auto-advance.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 6

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 165
    right_padding 14

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    on "show" action Play('audio', 'common_remind.ogg')

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 20

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 66

                textbutton _("Yes"):
                    idle_background Frame("blue_confirm_button", 27,18)
                    background Frame("blue_confirm_button_pressed", 27,18)

                    hovered Play("sound", "common_tag.ogg")
                    action [Play('sound', 'common_select.ogg'), yes_action]

                textbutton "No":
                    idle_background Frame("red_cancel_button", 27,18)
                    background Frame("red_cancel_button_pressed", 27,18)

                    hovered Play("sound", "common_tag.ogg")
                    action [Play('sound', 'common_cancel.ogg'), no_action]

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame("dialoguewindow", 25,25)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    xysize (100,48)
    bottom_padding 4

style confirm_button_text:
    properties gui.text_properties("confirm_button")
    color "#FFF"


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 4

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 296

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if not persistent.hide_quick_menu:

        hbox:
            yalign 0
            xalign 0.0

            button:
                background Frame("blue_confirm_button", 22, 22)
                xysize (quickmenubutton_width, quick_button_height)
                text quickmenutext:
                    xalign 0.5
                    ypos -1
                    size quick_button_text_size
                    color "#FFFFFF"
                action [Play("sound", "common_tag_2.ogg"), ShowMenu()]

        hbox:
            yalign 0
            xalign 1.0

            button:
                background Frame("blue_confirm_button", 22, 22)
                selected_background Frame("blue_confirm_button_pressed", 22,22)
                xysize (quickskipbutton_width, quick_button_height)
                text quickskiptext:
                    xalign 0.5
                    ypos -1
                    size quick_button_text_size
                    color "#FFFFFF"
                action [Play("sound", "common_tag_2.ogg"), Skip()] 
                alternate Skip(fast=True, confirm=True)

            button:
                background Frame("blue_confirm_button", 22, 22)
                selected_background Frame("blue_confirm_button_pressed", 22,22)
                xysize (quickautobutton_width, quick_button_height)
                text quickautotext:
                    xalign 0.5
                    ypos -1
                    size quick_button_text_size
                    color "#FFFFFF"
                action [Play("sound", "common_tag_2.ogg"), Preference("auto-forward", "toggle")]


style radio_button:
    variant "small"
    foreground "check_[prefix_]foreground"

style check_button:
    variant "small"
    foreground "check_[prefix_]foreground"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style pref_vbox:
    variant "small"
    xsize 263

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "touch"
    ysize gui.scrollbar_size
    thumb Frame("horizontal_scrollbar_thumb_[prefix_]mobile", 25, 25, tile=True)
    hover_sound None

style vscrollbar:
    variant "touch"
    xsize gui.scrollbar_size
    thumb Frame("vertical_scrollbar_thumb_[prefix_]mobile", 25, 25, tile=True)
    hover_sound None

style slider:
    variant "touch"
    ysize gui.slider_size
    thumb "images_free/gui/slider/horizontal_slider_thumb_mobile.png"
    left_gutter 2

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 394

style navigation_button:
    variant "touch"
    ysize 50
    xsize 180
    hover_sound None

style navigation_button_text:
    variant "touch"