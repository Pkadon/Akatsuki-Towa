#######################
# Game Name
#######################
### A human-readable name of the game. This is used to set the default window
### title, and shows up in the interface and error reports.
define config.name = ("Akatsuki_Towa")

######################
# Build Name
######################
## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.
define build.name = "Akatsuki_Towa"

#################################################
# Make sure to credit yourself!
#################################################
### Text that is placed on the game's about screen.
define gui.about = _p("""
This is a fan project!  All Characters, Scripts, Assets, etc. belong to Nihon Falcom Corporation (www.falcom.co.jp) and/or USERJOY JAPAN (www.ujj.co.jp)\n
Cutscenes recreated by Pikadon using Ren'Py
""")

##########
# Icon
##########
### The icon displayed on the taskbar or dock.
define config.window_icon = "icon/FormIcon.jpg"

#################################################################
# Default text scroll speed.
# May need to be modified or disabled to accomodate English character count.
#################################################################
### The default, 0, is infinite, while any other number is the number of characters per second to type out.
default preferences.text_cps = 20

init python early:
#################################################################
# Dialogue Window
#################################################################
### The size of normal dialogue text.
    gui.text_size = 20 # Normal
    small_text_size = 23 # For "small" screen variants

### The placement of dialogue relative to the textbox. These can be a whole number
### of pixels relative to the left or top side of the textbox.
    gui.dialogue_xpos = 20 # Normal
    small_dialogue_xpos = 20 # For "small" screen variants

    gui.dialogue_ypos = 25 # Normal
    small_dialogue_ypos = 25 # For "small" screen variants

### The number of padding pixels inbetween lines of dialogue
    gui.dialogue_line_spacing = 0 # Normal
    small_dialogue_line_spacing = -5 # For "small" screen variants

### The size of character speaker names.
    gui.name_text_size = 22 # Normal
    small_name_text_size = 25 # For "small" screen variants

### The dialogue box's height (starting from the bottom)
    gui.textbox_height = 113 # Normal
    small_textbox_height = 113 # For "small" screen variants

#################################################################
# Silver and gold "booktab" buttons used in all Scene Select menus
#################################################################
### Width of all silver and gold buttons (in pixels):
    tabwidth = 330
### Text size for all silver and gold buttons:
    tabtextsize = 20

####################################################
# "bookpage" buttons that play cutscenes when clicked
####################################################
### Height of all book page buttons (in pixels):
    pageheight = 80
### Text size for all book page buttons:
    pagetextsize = 18

################################################################
# The questlog window that appears when you click a "Log" button
################################################################
### Text size for all questlogs:
    logtextsize = 16

#################################
# Choice Menu
#################################
### Text size for all choice menu buttons:
    gui.choice_button_text_size = 18
    choice_button_text_size_large = 25 # used with "small" screen variant

#################################
# Screen Variant misc.
#################################
### With 1.0 as "full size", this sets the size of portraits in renpy "touch" variants (mobile)
### (mainly to account for the added buttons at the top)
    touch_portrait_scale = .95

#=======================================================================================
#===================================TRANSLATION=========================================
#=======================================================================================
#=================================================================================================
# SCRIPT FILE (text.json)
# place file in game/MonoBehaviour folder
#=================================================================================================
### text.json file structure:

### {
###     textrowkey: [
###         {
###             textidkey: 1,
###             textkey: "TEXT1"
###         },
###         {
###             textidkey: 2,
###             textkey: "TEXT2"
###         }
###     ]
### }
#=================================================================================================
### CSV example file:

### textidkey,textkey
### 1,"TEXT1"
### 2,"TEXT2"
#=================================================================================================

### The name of the file containing the game's script
### The file may be a .json file or a .csv file
    textfilename = "text.json"

### The encoding (may also be called "character set") used for the script file
    textencode = "utf-8"

### The key used to access the list of rows in text.json
### (skip this if using a csv file)
    textrowkey = "_rows"

### The key used to access the id value in text.json 
### (for a csv file, use the header at the top of the column instead)
    textidkey = "_id"

### The key used to access the string value in text.json 
### (for a csv file, use the header at the top of the column instead)
    textkey = "_text"



#=================================================================================================
# AVG ROLE FILE (avg_role.json)
# place file in game/MonoBehaviour folder
#=================================================================================================
### avg_role.json file structure:
### {
###     namerowkey: [
###         {
###             nameidkey: 1,
###             namekey: "Nacht",
###             "_folderName": "",    # unused, can be omitted
###             "_scale": 0,          # unused
###             "_xPostion": 0        # unused
###         },
###         {
###             nameidkey: 2,
###             namekey: "Chloe"
###         }
###     ]
### }
#=================================================================================================
### CSV example file:
###
### nameidkey,namekey
### 1,"Nacht"
### 2,"Chloe"
#=================================================================================================

### The name of the file containing character names
### The file may be a .json file or a .csv file
    namefilename = "avg_role.json"

### The encoding (may also be called "character set") used for the character name file
    nameencode = "utf-8"

### The key used to access the list of rows in avg_role.json
### (skip this if using a csv file)
    namerowkey = "_rows"

### The key used to access the id value in avg_role.json 
### (for a csv file, use the header at the top of the column instead)
    nameidkey = "_id"

### The key used to access the roleName string value in avg_role.json
### (for a csv file, use the header at the top of the column instead)
    namekey = "_roleName"


###############
# EXTRA STRINGS
###############

# Menu Buttons
#==========================================
### Back button text
    backtext = "Back"
### Jump button text
    jumptext = "Jump"
### Sprite test button text
    spritetext = "Sprite"
### Log button text
    logtext = "Log"

# Quest Log
#==========================================
### The tags put before the quest name to denote whether is is a main quest or a side quest
    logmain = "【メイン】"
    logsub = "【サブ】"
    logdaily = "【毎日】"
### The headers used in the questlog menu before each field
    loglevel = "【推奨レベル】"
    logclient = "【依頼人】"
    logdetails = "【内容】"
    logbullet = "●"

# Quick Menu
#==========================================
### The buttons at the bottom of the screen during cutscenes (top of screen on mobile)
### (they're kind of camouflaged on PC, but are much more prominent on mobile (touch) variants)
    quickmenutext = "Menu" # Not included in PC
    quickskiptext = "Skip"
    quickautotext = "Auto"
    quickhistorytext = "History" # Not included in mobile

# Menu Strings
# Almost all other text used throughout the menus, that could not be sourced from the original script file
    extextdict = {
    "ex_1": "Optional Dialogue",
    "ex_2": "Extra Dialogue",
    "ex_3": "Extra/Unused",
    "ex_4": "exact timing unknown",
    "ex_5": "Unused Tio Version",
    "ex_6": "Unused Tita Version",
    "ex_7": "Unused Alt Version",
    "ex_8": "Unused Ending",
    "ex_9": "(2 questions correct)",
    "ex_10": "(1 or no questions correct)",
    "ex_11": "Conditional Dialogue",
    "ex_12": "Quest Complete",
    "ex_13": "Quest Complete (Unused)",
    "ex_14": "Unused",
    "ex_15": "Conditional Dialogue (Unused)",
    "ex_16": "Unused Scenes",
    "ex_17": "Fishing",
    "ex_18": "Fishing Unlock Scene",
    "ex_19": "(Prologue)",
    "ex_20": "Fisherman's Guild",
    "ex_21": "(Grancel, Chapter 1)",
    "ex_100": "受付嬢トリア",
    "ex_101": "スラッシュ",
    "ex_102": "キャンベル議員",
    "ex_103": "フェルナンド",
    "ex_104": "スラッシュ/ヒューイ",
    "ex_105": "リン/エオリア",
    "ex_106": "ティータ",
    "ex_107": "カルノー/プロメテ",
    "ex_108": "マードック工房長",
    "ex_109": "ウォン/グンドルフ",
    "ex_110": "ジリアン/ロナード",
    "ex_200": "中央工房の盗難事件(2) 3/7",
    "ex_201": "準遊撃士・ナハトの奮闘記",
    "ex_202": "Vol.1-エオリア編",
    "ex_203": "Vol.1-ヴェンツェル編",
    "ex_204": "Vol.1-スコット編",
    "ex_205": "Vol.1-リン編",
    "ex_206": "Vol.2 アネラス編",
    "ex_207": "Vol.3 ノエル編",
    "ex_208": "Vol.4 ティータ編",
    "ex_209": "Vol.5 ミレイユ編",
    "ex_210": "Vol.6 ヨシュア編",
    "ex_211": "Vol.7 エリィ編",
    "ex_212": "Vol.8 エステル編",
    "ex_213": "Vol.9 ティオ編",
    "ex_214": "Vol.10 ランディ編",
    "ex_215": "Vol.11 ロイド編",
    "ex_216": "Vol.12 レン編",
    "ex_217": "Vol.13 カシウス編",
    "ex_218": "Vol.14 ユリア編",
    "ex_219": "Vol.15 アガット編",
    "ex_220": "Vol.16 グラッツ編",
    "ex_221": "Vol.17 シェラザード編",
    "ex_222": "Vol.18 クローゼ編",
    "ex_223": "Vol.19 ギルバート編",
    "ex_224": "Vol.20 クルツ編",
    "ex_225": "Vol.21 カルナ編",
    "ex_226": "Vol.22 ダドリー編",
    "ex_227": "Vol.23 アリオス編",
    "ex_228": "Vol.24 リシャール編",
    "ex_229": "Vol.25 キール編",
    "ex_230": "Vol.26 ジョゼット編",
    "ex_231": "Vol.27 ドルン編",
    "ex_232": "Vol.28 ミシェル編",
    "ex_233": "EX.1 リース編",
    "ex_234": "EX.2 ケビン編",
    "ex_235": "ミシェル先生の特別レッスン",
    "ex_236": "歩んでいく道の途中で",
    "ex_237": "試験班の夏休み",
    "ex_238": "第１回《ハロウィンフェス》",
    "ex_240": "作者：藤７８\n(2017.12 グランプリ受賞作品)",
    "ex_241": "作者：トム6W\n(2017.12 準グランプリ受賞作品)",
    "ex_242": "作者：月紅\n(2017.12 ブレイサー賞受賞作品)",
    "ex_243": "新米遊撃士のクリスマス",
    "ex_244": "Heroes War！",
    "ex_300": "毎日討伐",
    "ex_301": "ダルモア商会の依頼",
    "ex_302": "ラッセル博士の依頼",
    "ex_303": "リラの依頼",
    "ex_304": "マオ婆さんの依頼",
    "ex_305": "メイベルの依頼",
    "ex_306": "ホテル《ローエンバウム》の依頼",
    "ex_307": "クロスベル警察学校の依頼",
    "ex_308": "イメルダ夫人の依頼",
    "ex_309": "ウルスラ病院の依頼",
    "ex_310": "《リジョンフード》の依頼",
    "ex_311": "アルモリカ村の依頼",
    "ex_312": "《ホテル・ミレニアム》の依頼",
    "ex_313": "マイヤの依頼",
    "ex_314": "マルクの依頼",
    "ex_315": "ドナートの依頼",
    "ex_116": "カヌートの依頼",
    "ex_117": "セナの依頼",
    "ex_118": "クリントの依頼",
    "ex_119": "ルーシーの依頼",
    "ex_120": "モーリスの依頼"
}

########################################################

# Image Definitions (not a part of the python block)
########################################################

### The game logo.  Appears on the splash screen, and the bottom-right corner of the main menu.
image splash_akatsukilogo:
    Crop((0,331,502,178), "atlas_loading.png")
python early:
### Splash Screen logo properties:
    splash_logo_anchor = (0, 0) 
    splash_logo_pos = (390, 175) 
    splash_logo_zoom = .85 

image main_akatsukilogo:
    Crop((0,331,502,178), "atlas_loading.png")
python early:
    show_logo = True # change to False to hide logo from Main Menu
### Main Menu logo properties:
    main_logo_anchor = (1.0, 1.0)
    main_logo_pos = (.99, .97)
    main_logo_zoom = .85

### The よ永久に joke text, can be changed to anything you want to fade-in over top of the logo
### or you can define a totally different animation here.
image logooverlay:
    "images_free/towani2.png"
    pause 1.0
    "images_free/towani.png" with Dissolve(1.0, alpha=True)
python early:
    show_logooverlay = True # change to False to hide overlay image from Main Menu
### Main Menu overlay image properties:
    main_overlay_anchor = (1.0, 1.0)
    main_overlay_pos = (.97, .97)
    main_overlay_zoom = 1.0

### The Towa head that pops up in the bottom-right corner of the main menu.
### Change to who or whatever you prefer.
image popup:
    "sc085_01_i256.png"
    anchor (.5,.5)
    pos (0.68, 1.5)
    zoom 1.5
    rotate -20
    pause 1.0
    ease 1.0 ypos .925 
python early:
    show_popup = True # change to False to hide popup character from Main Menu