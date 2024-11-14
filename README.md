# Akatsuki-Towa
### This is a Ren'Py project to recreate Akatsuki no Kiseki cutscenes

 - [Setup](https://github.com/Pkadon/Akatsuki-Towa#setup)
 - [Build](https://github.com/Pkadon/Akatsuki-Towa#build)
 - [Add Typewriter Sound Effect](https://github.com/Pkadon/Akatsuki-Towa#adding-typewriter-sound-effect-back-in)
 - [Accuracy](https://github.com/Pkadon/Akatsuki-Towa#accuracy)
 - [Translation](https://github.com/Pkadon/Akatsuki-Towa#translation)
   - [Translation File Generator](https://github.com/Pkadon/Akatsuki-Towa#translation-file-generation-experimental)

---
## Setup
**DOES NOT INCLUDE ANY GAME FILES**

Please export required assets from the original game's unity3D files

I recommend using AssetStudioMod (by aelurum)  <https://github.com/aelurum/AssetStudio>

**If using AssetStudioMod to export assets, you can:**
 1. **Drag-and-drop the folder containing all of your .unity3D asset files**
 2. **Select the "Asset List" tab at the top**
 3. **Change the search type in the dropdown to "Regex (Name)"**
 4. **Paste the following regex pattern into the search field to easily filter required files:**

		avg_(vocal|role|img)|bat_(arts_wt02_2|craft_wind_01|utility_(jump|landing))|bcv_(oc00(1|2|3|4_hurt_02|6_(com_01|hurt_01)|8_c0(1_01|3_02))|sc020_sc01_0(4|5))|common_|dun_obj005_01_01|ed7v|^[eE][dD]\d\d\d\d$|elc_5|fight_|mainsong|other_7|sys_utility_typewriter|^text$|(atlas_(journal|login$|loading))|(avg_(a1screen|bg))|image_001|loading00|\d\d_\d\d_avg|sc085_01_i256|startbackground
 5. **Export by selecting "Export"->"Filtered assets"**
 6. **Then the folders are named so that you should be able to take the folders created by AssetStudio after exporting, ("AudioClip", "MonoBehaviour", "Texture2D") and drag them into Akatsuki-Towa's `game` folder. (Replace files in the destination when prompted)**
---

REQUIRES the official `text.json` and `avg_role.json` to be placed in the `game/MonoBehaviour` folder in order to display text properly.

All Audio files in the `game/AudioClip` folder are placeholder files to keep the program from crashing.
Please replace them with the actual files.
(Cutscenes can be read without replacing any audio filess.)

All Image files in the `game/Texture2D` folder are placeholder files to keep the program from crashing.
Pleace replace them with the actual files.
(Cutscenes can be read without replacing any image files.)

The `.ico` file in both the root folder, and `game/icon` is a placeholder file, please replace it with an icon of your choice.

---
## Build

To build into an .exe:
 1. Download Ren'Py from here: https://www.renpy.org/
 2. Place this folder in your Ren'Py projects folder
     - then build it from the "Build Distributions" menu within Ren'Py.
     - or, you can just "Launch Project" from inside Ren'Py.

NOTE: if you get an error when launching that says Ren'Py can't find a file, it may be because the `game` folder is inside of too many other folders.  Try moving it out of the parent folder.

---

### Scripts are also provided to generate text files from cutscene files, or re-generate renpy scripts in the `generate_scripts` folder:

 - **`generate_scripts/extra_json` folder**: 
   - contains pre-sorted lists of cutscenes which didn't have an easy way to be sorted automatically
 - **`generate_scripts/MonoBehaviour` folder**:  
   - please export the following files from the original game files, then place them in this folder:
     - `avg_replay.json`
     - `avg_role.json`
     - `bgm.json` (not required to make .txt files)
     - `booktabs.json`
     - `quest.json`
     - `sfx.json` (not required to make .txt files)
     - `text.json`
     - `training_event.json`
     - `trigger.json`
     - `voice.json` (not required to make .txt files)
     - all "avg" json files (example: `10001.json`) found in the `data_avg_data_[##].unity3d` files
   - (see [Generate Scripts Requirements](generate_scripts/MonoBehaviour/REQUIREMENTS.md) for a little more information, and a regex pattern to use)
---
Then run the .py scripts in the following order (or use the .bat files):

 1. **`1_make_new_quest_json.py`:** 
   - uses `booktabs.json` in combination with `quest.json` to create a simpler questlog json file in the `generate_scripts/extra_json` folder called `new_quest.json` 

 2. **`2_make_new_story_json.py`:**
   - uses `avg_replay.json` to organize and label all cutscenes accessible from the "物語回想" section of the in-game Bracer Notebook
   - then uses the newly-made `generate_scripts/extra_json/new_quest.json` to match up quests with their questlog by matching string ID's
   - outputs `new_story.json` in the `generate_scripts/extra_json` folder

 3. **`3_make_new_training_json.py`:**
   - uses `quest.json`, `trigger.json`, and `training_event.json` to find "戦闘訓練" stages that trigger cutscenes, and creates `new_training.json` in the `generate_scripts/extra_json` folder

   - **NOTE for sorting Training Events:** 
     - This script by default will only sort the "訓練" section of Training, skipping over the "イベント" section, because not all "イベント" cutscenes are accessible from all `quest.json`+`training_event.json` combinations. (that's why there's `generate_scripts/extra_json/EX12_event.json`)

---

**Then those three created json files can be checked over and edited before continuing**

---

 - **`4_sort_avg.py`:**
   -  combines the json files in `generate_scripts/extra_json` into dictionaries
   -  creates readable text files from the avg json files in `generate_scripts/MonoBehaviour`, and uses the created dictionaries to place them in a similar folder structure
 
 - **`4_make_menus.py`:** 
   - combines the json files in `generate_scripts/extra_json` into dictionaries, and then uses that dictionary to build the `episodelist.json` menu file for Akatsuki Towa

 - **`5_generate_script.py`:**
   - uses `avg_role.json`, `bgm.json`, `sfx.json`, `voice.json`
   - reads the avg json files in the `generate_scripts/MonoBehaviour` folder to create .rpy scripts for Akatsuki Towa

**PLEASE NOTE:** Not all generated scripts will be accessible from Akatsuki Towa's in-game menu, but they can be manually played by using the "Jump" button on the left side of the "Scene Select" menu.

---
## Adding typewriter sound effect back in
**enabletypewritersound.rpy**

I originally had the "typewriter" sound that plays while displaying text working by using an audio recording of the real game.

That won't be included here, so the entire thing has been disabled by default.

But the hooks are all still there, and can be re-enabled by uncommenting the second half of `game/enabletypewritersound.rpy`

---

## Accuracy

Everything was done with the goal of being as accurate as possible, but nothing is 100% certain to be 100% accurate

 - **Scene menu placement**:
   - Story cutscenes are sorted using original files, so should be correctly labeled
   - Training:
     - "訓練" cutscenes are sorted using original files, so should be correctly labeled
     - "イベント" cutscenes were sorted by hand, and their current placement can be found inside `generate_scripts/extra_json/EX12_event.json`
       - most "イベント" scenes are not labeled with their original title, but instead defaulting to the overall event's title if it wasn't 100% sure
   - pretty much everything else was sorted by hand, and its current placement can be found inside one of the other json files in `generate_scripts/extra_json/`
     - Especially for unused scenes in `generate_scripts/extra_json/EX15_unused.json`, there is no documentation or video reference to use, and some scenes are numbered out of order, so take placement and scene titles with a grain of salt 

 - **Character Sprites**:
   - bodies:
     -  cropped from their original texture atlases, using the coordinates found in the original game files
     -  default placement on the screen was "eyeballed", so may be a few pixels off, but takes into account each individual sprite's "x-offset" value found in "avg_role.json"
   - faces:
     -  cropped from their original texture atlases, using the coordinates found in the original game files
     -  placement on the "body" sprite was done by hand. this can be verified by clicking the "Sprite" button on the left side of Akatsuki-Towa's Scene Select menu to go to "Sprite Test" mode
        - the first line of dialogue for when a sprite shows up ("oc000_01") is the default "body" sprite.
        - the second line of dialogue (oc000_01 1") shows the default "face" sprite overlayed on top of the body sprite

 - **Cutscene Accuracy**:
   - tried to use all values included in the cutscene files, but it's still being converted to a renpy script, and was "eyeballed" until everything looked right
   - music, sound effects should all play when they are supposed to
   - backgrounds should change when they are supposed to
     - some transitions are still slightly off (background/character sprite/text box appearing/disappearing in a different order from the original game)
   - animations don't use any values from game files and are "made up"
   - "memory" overlay was created with GIMP, and is not 100% accurate to the original game
   - "typewriter" sound effect is disabled by default. (see [enabletypewritersound.rpy](#enabletypewritersound.rpy)

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
**These suggestions are for what the output file should look like.  You may need to do some testing to figure out how much of this your spreadsheet software is already doing automatically.**
 - It is recommended that the field containing the string is surrounded with double-quotes to make sure commas and linebreaks are included properly.
 - Add a linebreak to a string with the "enter" key, newline characters ("\\n") don't seem to work here.
 - Double-quotes that are a part of the string should be typed twice. (see example below)
 - Double all left curly brace characters that are part of the string ("{{")

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

## Translation File Generation (*experimental*)
You can now use `5_generate_TL_file.py`, found in the `generate_scripts` folder to create a new translatable text file. (either .csv or .json)
This script will pull out all strings used in Akatsuki Towa's menus and cutscenes, keeping them in order, while adding a note about where it will be used, and whether it is a duplicate usage or not.
Translate text by editing the "_text" field.  You can either remove the "jptext" field when you're done, or leave it where it is.

(For now, you will still need to separately translate the extra strings in `CONFIG.rpy`.  For these instances, a note will be made in the generated translation file.)

(Please also note that the speaker is included as supplementary information only.  Each speaker's name only needs to be translated once, inside your `avg_role.json` file.)

**5_generate_TL_file.py required files**

in `generate_scripts\MonoBehaviour`:
 - `text.json`
 - `avg_role.json`
 - all "avg" cutcene json files (examples: `10001.json`, `1186.json`)

in `generate_scripts\Renpy_scripts`:
 - `episodelist.json`

---
# **Ren'Py Disclaimer**
**This program contains free software licensed under a number of licenses,
including the GNU Lesser General Public License. A complete list of software
is available at http://www.renpy.org/doc/html/license.html.**
