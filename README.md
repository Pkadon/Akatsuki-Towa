### This is a Ren'Py project to recreate Akatsuki no Kiseki cutscenes

---

### DOES NOT INCLUDE ANY GAME FILES

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


To build into an .exe:
 1. Download Ren'Py from here: https://www.renpy.org/
 2. Place this folder in your Ren'Py projects folder
     - then build it from the "Build Distributions" menu within Ren'Py.
     - or, you can just "Launch Project" from inside Ren'Py.


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
   - combines the json files in `generate_scripts/extra_json` into dictionaries, and then uses that dictionary to build the `episodelist.rpy` and `questlog.rpy` menu files for Akatsuki Towa

 - **`5_generate_script.py`:**
   - uses `avg_role.json`, `bgm.json`, `sfx.json`, `voice.json`
   - reads the avg json files in the `generate_scripts/MonoBehaviour` folder to create .rpy scripts for Akatsuki Towa

**PLEASE NOTE:** Not all generated scripts will be accessible from Akatsuki Towa's in-game menu, but they can be manually played by using the "Jump" button on the left side of the "Scene Select" menu.

---

### enabletypewritersound.rpy

I originally had the "typewriter" sound that plays while displaying text working by using an audio recording of the real game.

That won't be included here, so the entire thing has been disabled by default.

But the hooks are all still there, and can be re-enabled by uncommenting the second half of `game/enabletypewritersound.rpy`

---

### ACCURACY

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
     -  placement on the "body" sprite was done by hand. this can be verified by clicking the "Extra" button on the left side of Akatsuki-Towa's Scene Select menu to go to "Sprite Test" mode
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

### Translation:

If someone were to attempt to translate Akatsuki's script and have it play from within Akatsui-Towa, for the most part, you would only need to create edited/translated copies of `text.json` and `avg_role.json`, and replace the files in `game/MonoBehaviour` with your newly created files, but there are some special circumstances to note:
 - Text may not fit, and either the frame or the text itself may need to be resized
   - for dialogue/character names, change the default text size in `game/gui.rpy`
   - for menus/buttons, the easiest way may be to edit `generate_scripts/4_make_menus.py`, then re-generate and replace the renpy menus
 - Some button labels are hard-coded into the extra json files found in `generate_scripts\extra_json`:
   - these buttons have their `strID` value set to `null`
   - edit the button's `name` value directly, then re-generate and replace the renpy menus
 - "【推奨レベル】", "【依頼人】", "【内容】" labels are hard-coded into the questlog menus
   - in `generate_scripts/4_make_menus.py` translate those 3 strings toward the bottom under `#build log`, then re-generate and replace the renpy menus

---

**Ren'Py Disclaimer**:  
This program contains free software licensed under a number of licenses,
including the GNU Lesser General Public License. A complete list of software
is available at http://www.renpy.org/doc/html/license.html.
