### This is a Ren'Py project to recreate Akatsuki no Kiseki cutscenes

To build into an .exe, download Ren'Py from here: https://www.renpy.org/
place this folder in your Ren'Py projects folder and then build it from the "Build Distributions" menu within Ren'Py.
or, you can just "Launch Project" from inside Ren'Py.

---

DOES NOT INCLUDE ANY GAME FILES

Please export required assets from the original game's Unity files using AssetStudio: <https://github.com/Perfare/AssetStudio>

If using AssetStudio to export assets, change the search type in the dropdown to "Regex (Name)", and paste the following regex pattern into the field to easily filter required files:

	avg_(vocal|role|img)|bat_(arts_wt02_2|craft_wind_01|utility_(jump|landing))|bcv_(oc00(1|2|3|4_hurt_02|6_(com_01|hurt_01)|8_c0(1_01|3_02))|sc020_sc01_0(4|5))|common_|dun_obj005_01_01|ed7v|^[eE][dD]\d\d\d\d$|elc_5|fight_|mainsong|other_7|sys_utility_typewriter|^text$|(atlas_(journal|login$|loading))|(avg_(a1screen|bg))|image_001|loading00|\d\d_\d\d_avg|sc085_01_i256|startbackground

---

REQUIRES the official "text.json" and "avg_role.json" to be placed in the "game/json" folder in order to display text properly.

All Audio files in the "game/audio" folder are placeholder files to keep the program from crashing.
Please replace them with the actual files.
(Cutscenes can be read without replacing any audio filess.)

All Image files in the "game/images" folder are placeholder files to keep the program from crashing.
Pleace replace them with the actual files.
(Cutscenes can be read without replacing any image files.)

The .ico file in both the root folder, and "game/icon" is a placeholder file, please replace it with an icon of your choice.

---

### Scripts are also provided to generate text files from cutscene files, or re-generate renpy scripts in the "generate_scripts" folder:

#### "extra json" folder: 
contains pre-sorted lists of cutscenes which I couldn't find an easy way to sort automatically

#### "MonoBehaviour" folder:  
please use AssetStudio to export the following files, then place them in this folder:

 "avg_replay.json"

 "avg_role.json"

 "bgm.json" (not required to make .txt files)

 "booktabs.json"

 "quest.json"

 "sfx.json" (not required to make .txt files)

 "text.json"

 "training_event.json"

 "trigger.json"

 "voice.json" (not required to make .txt files)


 all "AVG" json files found in the "data_avg_data_[##].unity3d" files

### (see [Generate Scripts Requirements](generate_scripts/MonoBehaviour/REQUIREMENTS.md) for a little more information)

---
Then run the .py scripts in the following order (or use the .bat files):

#### "1_make_new_quest_json.py":  
converts "quest.json" into "extra_json/new_quest.json" 

#### "2_make_new_story_json.py":  
converts "avg_replay.json" into "extra_json/new_story.json", using "new_quest.json" to match up scenes with their quest ID's

#### "3_make_new_training_json.py":  
uses "quest.json", "trigger.json", and "training_event.json" to find Training Events that show cutscenes, and converts it into "extra_json/new_training.json"

**NOTE for sorting Training Events:** This script by default will only sort the "訓練" section, and will skip over the "イベント" section, because not all events ae accessible from all "quest.json"+"training_event.json" combinations (that's why there's "EX12_event.json")

---

Then those three created json files can be checked over and edited before continuing

---

#### "4_sort_avg.py":  
uses the json files in "extra_json", and the AVG json files in "MonoBehaviour" to create a folder of sorted cutscene txt files

#### "4_make_menus.py":  
uses the json files in "extra_json" to build the "episodelist" and "questlog" menu files for Akatsuki Towa

#### "5_generate_script.py":  
converts the AVG files into the .rp Ren'Py scripts used by Akatsuki Towa

**PLEASE NOTE:** Not all generated scripts will be accessible from Akatsuki Towa's in-game menu, but they can be manually played by using the "Jump" button on the left side of the "Scene Select" menu.

---

Ren'Py Disclaimer:  
This program contains free software licensed under a number of licenses,
including the GNU Lesser General Public License. A complete list of software
is available at http://www.renpy.org/doc/html/license.html.
