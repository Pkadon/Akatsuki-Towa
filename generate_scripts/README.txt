#################################################################
scriptgen_renpy.py will generate renpy scripts from original cutscene files
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


################################################################
scriptgen_txt.py will generate readable .txt files from original cutscene files
requires the following files be places in the "MonoBehavior" folder:
-any avg (cutscene) data files to convert (they are named ######.json)
-text.json
-avg_role.json