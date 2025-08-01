﻿################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(840, 480)

## Enable checks for invalid or unstable properties in screens or transforms
define config.check_conflicting_properties = True

################################################################################
## GUI Configuration Variables
################################################################################

## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#000000'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#707070'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = '#606060'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#000000'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = '#555555'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#7070707f'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = '#666666'
define gui.hover_muted_color = '#999999'

## The colors used for dialogue and menu choice text.
define gui.text_color = '#404040'
define gui.interface_text_color = '#404040'


## Fonts and Font Sizes ########################################################

## The size of text in the game's user interface.
define gui.interface_text_size = 20

## The size of labels in the game's user interface.
define gui.label_text_size = 23

## The size of text on the notify screen.
define gui.notify_text_size = 17

## The size of the game's title.
define gui.title_text_size = 33


## Main and Game Menus #########################################################


## The images used for the main and game menus.
define gui.main_menu_background = "mainmenuscreen"

define gui.game_menu_background = "gui/game_menu.png"


## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The placement of the textbox vertically on the screen. 0.0 is the top, 0.5 is
## center, and 1.0 is the bottom.
define gui.textbox_yalign = 1.0

## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.
define gui.name_xpos = 0.5
define gui.name_ypos = -20

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.name_xalign = 0.5

## The width, height, and borders of the box containing the character's name, or
## None to automatically size it.
define gui.namebox_width = None
define gui.namebox_height = 37

## The borders of the box containing the character's name, in left, top, right,
## bottom order.
define gui.namebox_borders = Borders(25, -1, 25, 5)

## If True, the background of the namebox will be tiled, if False, the
## background of the namebox will be scaled.
define gui.namebox_tile = False

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = 0.95

## The horizontal alignment of the dialogue text. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.dialogue_text_xalign = 0.0


## Buttons #####################################################################
##
## These variables, along with the image files in gui/button, control aspects of
## how buttons are displayed.

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.button_borders = Borders(3, 3, 3, 3)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

## The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.0

## These variables override settings for different kinds of buttons. Please see
## the gui documentation for the kinds of buttons available, and what each is
## used for.
##
## These customizations are used by the default interface:

define gui.radio_button_borders = Borders(12, 3, 3, 15)
define gui.radio_button_height = 32

define gui.check_button_borders = Borders(12, 3, 3, 15)
define gui.check_button_height = 32

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(7, 3, 7, 3)

define gui.quick_button_borders = Borders(7, 3, 7, 0)
define gui.quick_button_text_size = 10
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.
define gui.slot_button_width = 182
define gui.slot_button_height = 136
define gui.slot_button_borders = Borders(7, 7, 7, 7)
define gui.slot_button_text_size = 10
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 168
define config.thumbnail_height = 95

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 27

## The vertical position of the skip indicator.
define gui.skip_ypos = 7

## The vertical position of the notify screen.
define gui.notify_ypos = 30

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 3

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 7

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = 7

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames.
define gui.frame_borders = Borders(3, 3, 3, 3)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(27, 27, 27, 27)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(11, 4, 33, 4)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(11, 4, 27, 4)

## Should frame backgrounds be tiled?
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define gui.bar_size = 17
define gui.scrollbar_size = 20
define gui.slider_size = 17

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(3, 3, 3, 3)
define gui.scrollbar_borders = Borders(3, 3, 3, 3)
define gui.slider_borders = Borders(3, 3, 3, 3)

## Vertical borders.
define gui.vbar_borders = Borders(3, 3, 3, 3)
define gui.vscrollbar_borders = Borders(3, 3, 3, 3)
define gui.vslider_borders = Borders(3, 3, 3, 3)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.
define gui.unscrollable = "hide"


## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = 100

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 102
define gui.history_name_ypos = 0
define gui.history_name_width = 570
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 112
define gui.history_text_ypos = 2
define gui.history_text_width = 570
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 7, 0, 14)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define gui.nvl_height = 76

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 7

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 283
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 99
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 296
define gui.nvl_text_ypos = 6
define gui.nvl_text_width = 388
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define gui.nvl_thought_xpos = 158
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 512
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 296
define gui.nvl_button_xalign = 0.0


################################################################################
## Mobile devices
################################################################################

init python:

    @gui.variant
    def touch():

        ## Font sizes.
        gui.skip_ypos = quick_button_height
        gui.scrollbar_size = 50

        ## Change the size and spacing of various things.
        gui.slider_size = 24
        gui.navigation_spacing = 14
        gui.pref_button_spacing = 10

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    @gui.variant
    def small():

        ## Font sizes.
        gui.text_size = small_text_size
        gui.name_text_size = small_name_text_size

        ## Adjust the location of the textbox.
        gui.textbox_height = small_textbox_height
        gui.dialogue_line_spacing = small_dialogue_line_spacing
        gui.dialogue_xpos = small_dialogue_xpos
        gui.dialogue_ypos = small_dialogue_ypos

        gui.choice_button_text_size = small_choice_button_text_size

        gui.history_height = 125
        gui.history_text_width = 453
