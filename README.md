# Akatsuki-Towa
This is a Ren'Py project to recreate Akatsuki no Kiseki cutscenes from the original files  
  
To build into an .exe, download Ren'Py from here: https://www.renpy.org/  
place this folder in your Ren'Py projects folder  
BE SURE to place your "text.json" and "avg_role.json" in "game/json"  
and then build it from the "Build Distributions" menu within Ren'Py.  
  
or, you can just "Launch Project" from inside Ren'Py.  


### DOES NOT INCLUDE ANY GAME FILES
REQUIRES "**text.json**" and "**avg_role.json**" to be placed in the "game/json" folder in order to run or build properly.  
  
**All Audio files in the "game/audio" folder are placeholder files** to keep the program from crashing.  
Please replace them with the actual files.  
(Cutscenes are readable without replacing any audio filess.)  
  
**All Image files in the "game/images" folder are placeholder files** to keep the program from crashing.  
Pleace replace them with the actual files.  
(Cutscenes are readable without replacing any image files.)  
  
The .ico file in both the root folder, and "game/icon" is a placeholder file, please replace it with an icon of your choice.  
  
#########################################################  
  
Scripts are also provided to generate text files from cutscene files, or re-generate renpy scripts in the "generate_scripts" folder:  
  
**scriptgen_renpy.py** will generate renpy scripts from original cutscene files  
requires the following files be places in the "MonoBehavior" folder:  
-any avg (cutscene) data files to convert (they are named ######.json)  
-text.json  
-avg_role.json  
-bgm.json  
-sfx.json  
-voice.json  
  
PLEASE NOTE:  
Not all generated scripts will be accessible from Akatsuki Towa's in-game menu  
-Some scenes in the "Unused Scenes" section were combined into one script to reduce the number of menu items.  
-Some scenes have the same dialogue, but may have different presentation.  In these cases, the scene accessible from Akatsuki Towa is the version that was accessible from the Story Replay section of Akatsuki no Kiseki's Bracer Notebook.  

###  
**scriptgen_txt.py** will generate readable .txt files from original cutscene files  
requires the following files be places in the "MonoBehavior" folder:  
-any avg (cutscene) data files to convert (they are named ######.json)  
-text.json  
-avg_role.json  

  
#########################################################  
  
and because I have no idea what I'm doing, the Ren'Py license recommended including this part in a readme:  
  
This program contains free software licensed under a number of licenses,  
including the GNU Lesser General Public License. A complete list of software  
is available at http://www.renpy.org/doc/html/license.html.  
