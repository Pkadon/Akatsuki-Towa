# Akatsuki-Towa
## This is a Ren'Py project to recreate Akatsuki no Kiseki cutscenes

 - [Setup](#setup)
 - [Build](#build)
 - [Add Typewriter Sound Effect](#adding-typewriter-sound-effect-back-in)
 - [Accuracy](#accuracy)
 - [Translation](#translation)
   - [Translation File Generator](#translation-file-generation)
 - [Mobile](#mobile-version)
 - [Troubleshooting](#troubleshooting)
 - [Thanks](#extra-special-thanks)
---
# Setup
**DOES NOT INCLUDE ANY GAME FILES**

Please export required assets from the original game's unity3D files

I recommend using AssetStudioMod (by aelurum)  <https://github.com/aelurum/AssetStudio>

**If using AssetStudioMod to export assets, you can:**
 1. **Drag-and-drop the folder containing all of your .unity3D asset files into the AssetStudio window.**
 2. **Select the "Asset List" tab at the top**
 3. **Change the search type in the dropdown to "Regex (Name)"**
 4. **Paste the following regex pattern into the search field to easily filter required files:**

		avg_(vocal|role|img)|bat_(arts_wt02_2|craft_wind_01|utility_(jump|landing))|bcv_(oc00(1|2|3|4_hurt_02|6_(com_01|hurt_01)|8_c0(1_01|3_02))|sc020_sc01_0(4|5))|common_|dun_obj005_01_01|ed7v|^[eE][dD]\d\d\d\d$|elc_5|fight_|mainsong|other_7|sys_utility_typewriter|^text$|(atlas_(journal|login$|loading))|(avg_(a1screen|bg))|image_001|loading00|\d\d_\d\d_avg|sc085_01_i256|startbackground
 5. **Export by selecting "Export"->"Filtered assets"**
 6. **Then the folders are named so that you should be able to take the folders created by AssetStudio\* after exporting, ("AudioClip", "MonoBehaviour", "Texture2D") and drag them into Akatsuki-Towa's `game` folder. (Replace files in the destination when prompted)**

\* This is assuming you are exporting with AssetStudio's default settings. If any files are not able to be found by the game, or if you are using a different program to export the assets, please ensure that:
 - `Texture2D` are converted to `.png`, and that they end up in the `game/Texture2D` folder
 - `AudioClip` are converted to `.ogg`, and that they end up in the `game/AudioClip` folder
 - `MonoBehaviour` are converted to `.json`, and that they end up in the `game/MonoBehaviour` folder

---

REQUIRES the official `text.json` and `avg_role.json` to be placed in the `game/MonoBehaviour` folder in order to display text properly.

All Audio files in the `game/AudioClip` folder are placeholder files to keep the program from crashing.
Please replace them with the actual files.
(Cutscenes can be read without replacing any audio filess.)

All Image files in the `game/Texture2D` folder are placeholder files to keep the program from crashing.
Pleace replace them with the actual files.
(Cutscenes can be read without replacing any image files.)

---
# Build

To build into an .exe:
 1. Get the Ren'Py SDK here: https://www.renpy.org/latest.html
 2. Download the Akatsuki Towa source code, and move the [Akatsuki_Towa](Akatsuki_Towa) folder to your Ren'Py projects folder.
 3. Add the original game asset files, as described in the [Setup](#Setup) section
     - then build it from the "Build Distributions" menu within Ren'Py.
     - or, you can just "Launch Project" from inside Ren'Py, and play the game that way.

NOTE: if you get an error when launching that says Ren'Py can't find a file, it may be because the `game` folder is inside of too many other folders.  Try moving it up one level, outside of the parent folder.

---

### Scripts are also provided to generate text files from cutscene files, or re-generate renpy scripts in the `generate_scripts` folder:

 - **`generate_scripts/extra_json` folder**: 
   - contains pre-sorted lists of cutscenes
 - **`generate_scripts/MonoBehaviour` folder**:  
   - please export the following files from the original game files, then place them in this folder:
     - `avg_replay.json`
     - `avg_role.json`
     - `bgm.json`
     - `booktabs.json`
     - `quest.json`
     - `sfx.json`
     - `text.json`
     - `training_event.json`
     - `trigger.json`
     - `voice.json` (not required to make .txt files)
     - all "avg" json files (example: `10001.json`) found in the `data_avg_data_[##].unity3d` files
   - (see [Generate Scripts Requirements](generate_scripts/MonoBehaviour/REQUIREMENTS.md) for a little more information, and a regex pattern to use)
---
**__It is no longer recommended to use these next three scripts, unless for some reason you need to make a brand new menu from scratch.__**
These scripts are only able to use the information that was accessible from the original game's files at the time of shutdown (with a few exceptions).  I have made a TON of modifications to the copies of the `.json` files stored in this repository, that can't easily be replicated with these scripts alone.  I feel it's important to keep them around, just to be able to "show my work", but just know that they are not necessary, or even used here anymore.

 1. **`1_make_new_quest_json.py`:** 
   - uses `booktabs.json` in combination with `quest.json` to create a simpler questlog json file in the `generate_scripts/extra_json` folder called `new_quest.json` 

 2. **`2_make_new_story_json.py`:**
   - uses `avg_replay.json` to organize and label all cutscenes accessible from the `物語回想` section of the in-game Bracer Notebook
   - then uses the newly-made `generate_scripts/extra_json/new_quest.json` to match up quests with their questlog by matching the ID of the quest's string with the ID of the questlog's string.
   - outputs `new_story.json` in the `generate_scripts/extra_json` folder

 3. **`3_make_new_training_json.py`:**
   - uses `quest.json`, `trigger.json`, and `training_event.json` to find `戦闘訓練` stages that trigger cutscenes, and creates `new_training.json` in the `generate_scripts/extra_json` folder

   - **NOTE for sorting Training Events:** 
     - This script by default will only sort the `訓練` section of Training, skipping over the `イベント` section, because not all `イベント` cutscenes are accessible from all `quest.json`+`training_event.json` combinations. (that's why there's `generate_scripts/extra_json/EX12_event.json`)

---

**Then all of the json files in `generate_scripts/extra_json` can be checked over and edited before continuing**

The order that quests will be listed in the game's menu will match the order that they are listed inside these json files.  At this point, you can rearrange anything you want to, or remove quests that you don't want to be visible on the scene select screen. (maybe you're working on a translation and don't want to translate all of the weird extra stuff).   Deleting the .json file itself will also allow you to create a menu file that has that entire category removed.  (deleting the `new_quest.json`file will also let you easily hide all of the questlog buttons if needed.)

Currently, the order that quests will be sorted in is as follows:
 1. `new_story.json`
 2. `new_training.json`
 3. `EX12_event.json`
 4. `EX13_exploration.json`
 5. `EX14_daily.json`
 6. `EX15_unused.json`

but you could change the order that they are added together from within `4_make_menus.py`

---
 
 - **`4_make_menus.py`:** 
   - combines all of the json files in `generate_scripts/extra_json` into a single `episodelist.json` menu file for Akatsuki Towa.

 - **`5_generate_script.py`:**
   - uses `avg_role.json`, `bgm.json`, `sfx.json`, `voice.json`
   - reads the avg json files in the `generate_scripts/MonoBehaviour` folder to create .rpy scripts for Akatsuki Towa.

##### **PLEASE NOTE:** 
Not all generated scripts will be accessible from Akatsuki Towa by default.
Scenes not accessible from the Scene Select menu have been removed from the default build folder to reduce load time.  The complete set of cutscene script files can be found in [this folder](complete_scripts_archive).  Move any or all of the `.rpy` files you are interested in into your `game/scripts` folder. 
Then they can be manually played from within Akatsuki Towa by clicking the "Jump" button on the left side of the "Scene Select" menu, and entering the cutscene file's number in the box.

---
## Adding typewriter sound effect back in
**enabletypewritersound.rpy**

I originally had gotten the "typewriter" sound (that plays while dialogue is being typed out) working here by using an audio recording from the real game.  The audio recording won't be included in this repository, however, so the entire thing has been disabled by default.

But the hooks are all still intact, and if you have a usable audio recording, you can re-enable the typewriter effect:
 1. Uncomment the second half of `game/enabletypewritersound.rpy`, and if necessary, change the name of the file that will be played to match your recording.
 2. Place your audio file in the `AudioClip` folder.

---

## Accuracy

Everything was done with the goal of being as accurate as possible, but nothing is 100% certain to be 100% accurate

 - **Scene labeling, order**:
   - Story:
     - Scenes were originally sorted using original files, so should be correctly labeled
     - They HAVE been reordered from the original `物語回想` menu's ordering (namely, the quests from Prologue up through Chapter 3) but it was mostly to get them closer to the original play order.  (the original menu had grouped them by Main and Sub quests, instead of the order they were played in)
   - Training:
     - `訓練` cutscenes were originally sorted using original files, so should be correctly labeled and ordered
     - `イベント` cutscenes were sorted by hand, and their current placement can be found inside [generate_scripts/extra_json/EX12_event.json](generate_scripts/extra_json/EX12_event.json)
       - Most `イベント` scenes are not labeled with their original title, but instead defaulting to the overall event's title if it wasn't 100% sure where the correct string was.
   - Pretty much everything else was sorted by hand, and its current placement can be found inside one of the other json files in [generate_scripts/extra_json](generate_scripts/extra_json/)
     - Especially for unused scenes in [generate_scripts/extra_json/EX15_unused.json](generate_scripts/extra_json/EX15_unused.json), there is no documentation or video reference to use, and some scenes were originally numbered out of order, so take placement and scene titles with a grain of salt 

 - **Character Sprites**:
   - bodies:
     -  cropped from their original texture atlases, using the coordinates found in the original game files
     -  default placement on the screen was "eyeballed", so may be a few pixels off, but takes into account each individual sprite's "x-offset" value found in "avg_role.json"
   - faces:
     -  cropped from their original texture atlases, using the coordinates found in the original game files
     -  placement on the "body" sprite was done by hand. this can be verified by clicking the "Sprite" button on the left side of Akatsuki-Towa's Scene Select menu to go to "Sprite Test" mode
        - the first line of dialogue for when a sprite shows up ("oc000_01") is the default "body" sprite.
        - the second line of dialogue ("oc000_01 1") shows the default "face" sprite overlayed on top of the body sprite

 - **Cutscene Accuracy**:
   - music, sound effects should all play when they are supposed to
   - backgrounds should change when they are supposed to
   - animations don't use any values from game files and are "made up"
   - "memory" overlay was recreated with GIMP, and is not 100% accurate to the original game.
   - "typewriter" sound effect is disabled by default. (see [enabletypewritersound.rpy](#enabletypewritersound.rpy)

 - **Observed Differences from the original game**:
   - **+** **Obvious** errors and inconsistencies have been carefully corrected. 
      - Most of these can be undone if needed by deleting the block in the [script generator](generate_scripts/5_generate_script.py), then regenerating the scripts.
      - There is also a duplicate line that is skipped in avg 12038.  The line to remove that can be found a little further down in the same script.
      - And a typo fix at the bottom of [loadinfo.rpy](Akatsuki_Towa/game/loadinfo.rpy)
   - **+** Portrait animations will now wait for the fade transition to finish before playing.  In the original game it was possible to miss animations, or see them be applied to the wrong character's portrait while the fade played out.
   - **+** If a character without a portrait speaks from the left or right side of the screen while a portrait is being shown in the middle position, the middle portrait will be darkened to indicate that it is not the one speaking.  This was not accounted for in the original game!
   - **+** Similarly, if portraits are being displayed on the left/right sides, and a charPos 0 speaker with no portrait speaks, the left/right portraits will be darkened.
   - **-** Selecting a choice is not supposed to "clear the board" and remove all portraits.  I'm not sure whether this will be able to be fixed here or not.

---

# Translation
If someone were to attempt to translate Akatsuki's script and have it play from within Akatsui-Towa, for the most part, you would only need to create edited/translated copies of `text.json` and `avg_role.json`, and replace the files in `game/MonoBehaviour` with your newly created files, but there are some special circumstances to note:
 - Text may not fit inside some of the buttons, and either the frame size or the text itself may need to be resized
   - These values can now be changed by editing them in `game/CONFIG.rpy`
 - Some text used in the menus could not be sourced directly from the original script file
   - These strings can now be changed by editing them in `game/CONFIG.rpy`

## Translation file notes
The text loader was made more flexible, and it is now possible to load .csv files, and (partially) customized .json files as script files.
Please test your file early and often, to make sure that it is loaded properly.
 - Place your `text.json` and `avg_role.json` equivalent files in `game/MonoBehaviour`
   - The file is assumed to be encoded in utf-8.
   - In order to avoid sudden crashes, the file will need to include rows containing all string ids used by Akatsuki-Towa scripts and menus. 
      - The string/text field can be left empty.
 - Edit the filename and key name variables in the "Translation" section of `CONFIG.rpy` to match your file (see examples in CONFIG.rpy for help)

### JSON notes
 - A .json file may have a different filename and key names, but loadinfo.rpy will still expect it to match the basic structure of the original script files (see example below)
 - Include a linebreak in a string with a newline character ("\\n") instead of pressing the "enter" key
 - Escape ALL double-quotes that are part of the string with a backslash ("\\"")
   - If your json file surrounds string values in single quotes, escape single quotes instead ('\\'')
 - Double all backslashes and left curly brace characters that are part of the string ("{{"), ("\\\\")
 - Double all left square brackets that are part of strings that show on the scene select menu ("[[")
   - This does not seem to be required for strings that are only shown as dialogue, but more experimenting may need to be done

#### Example JSON

```
{
    rowkey: [
        {
            idkey: 1,
            textkey: "TEXT1"
        },
        {
            idkey: 2,
            textkey: "TEXT2"
        }
    ]
}
```

### CSV notes
**These suggestions are for what the output file should look like.  You may need to do some testing to figure out how much of this your spreadsheet software is already handling automatically.**
 - It is recommended that the field containing the string is surrounded with double-quotes to make sure commas and linebreaks are included properly.
 - Add a linebreak to a string with the "enter" key, newline characters ("\\n") don't seem to work here.
 - Double-quotes that are a part of the string should be typed twice. (see example below)
 - Double all left curly brace characters that are part of the string ("{{") 
 - Double all left square brackets that are part of strings that show on the scene select menu ("[[")
   - This does not seem to be required for strings that are only shown as dialogue, but more experimenting may need to be done

#### Example CSV

```
idkey,textkey
1,"TEXT1"                           |displays as: TEXT1
2,"TEXT2"                           |displays as: TEXT2
3,Oh,no                             |displays as: Oh
4,"Oh, no!"                         |displays as: Oh, no!
5,"""Oh, no!"""                     |displays as: "Oh, no!"
6,"""Oh, no!,"" he exclaimed."      |displays as: "Oh, no!," he exclaimed.
7,"Oh,\nno!"                        |displays as: Oh,\nno!
8,"Oh,                              |displays as: Oh
no"                                 |             no
9,                                  |displays as: 
10,"{{Oh, no!}"                     |displays as: {Oh, no!}
11,"{Oh, no!}"                      |do not use - crashes Ren'Py
```

## Translation File Generation
You can now use `5_generate_TL_file.py`, found in the `generate_scripts` folder to create new translatable text files. (either .csv or .json)
This script will pull out all strings used in Akatsuki Towa's menus and cutscenes, keeping them in order, while adding a note about where it will be used, and whether it is a duplicate usage or not.
Translate text by editing the "_text" field.  You can either remove the "jptext" field when you're done, or leave it as it is.

(For now, you will still need to translate the extra strings in `CONFIG.rpy` separately.  For these instances, a note will be made in the generated translation file.)

(Please also note that the speaker is included as supplementary information only.  Each speaker's name only needs to be translated once, inside your `avg_role.json` file.)

**5_generate_TL_file.py required files**

in `generate_scripts\MonoBehaviour`:
 - `text.json`
 - `avg_role.json`
 - all "avg" cutcene json files (examples: `10001.json`, `1186.json`)

in `generate_scripts\Renpy_scripts`:
 - `episodelist.json`

---
## Mobile Version?
I believe that the menu buttons and text sizes and everything have been optimized for mobile devices.  Due to my unwillingness to supply game assets from this repository, and the unnecessary complications that would come from having to expect a regular user to unpack and then repack any "clean" APK file I could make, a prebuilt APK will not ever be provided here.

You can build your own copy, though. (just don't put ads in it or upload it to an app store please)
 1. Get the Ren'Py SDK: https://www.renpy.org/latest.html
 2. Download the Akatsuki Towa source code, and move the [Akatsuki_Towa](Akatsuki_Towa) folder to your Ren'Py projects folder.
 3. Add the original game asset files, as described in the [Setup](#Setup) section
 4. Then you should be able to proceed with the mobile build instructions from Ren'Py: 
   - [Android](https://www.renpy.org/doc/html/android.html#building-android-applications)
   - [iOS](https://www.renpy.org/doc/html/ios.html#packaging) (sorry, I am unable to test or help with any iOS stuff)

---
## Troubleshooting
**"Jumping" Menu Text:**
 - As of V3.0, under certain conditions, it is possible for button text to be shown in the wrong position at first, and then it will jump to where it was supposed to be after being hovered over with the mouse.  As far as I can tell, this seems to be an issue caused by Ren'Py caching older versions of the menu, and then not clearing or updating it completely after text has been changed.  Please try deleting Akatsuki Towa's `game/cache` and/or `game/saves` folders, and hopefully that should fix it.  If it does *not*, please open a new issue [here](https://github.com/Pkadon/Akatsuki-Towa/issues) and let me know.  Thanks!

---
# EXTRA-SPECIAL THANKS
[Callum521](https://www.youtube.com/@Callum5211) - For playtesting, stress testing, and helping to correct errors!

[Raymond Law](https://www.youtube.com/@ZeroXHK) - For their [full, unedited playthrough of Akatsuki!](https://www.youtube.com/playlist?list=PLQq2_C4tinm6aKxzIpMWCSM9PUvfHHsWF)

---
# **Ren'Py Disclaimer**
**This program contains free software licensed under a number of licenses,
including the GNU Lesser General Public License. A complete list of software
is available at http://www.renpy.org/doc/html/license.html.**
