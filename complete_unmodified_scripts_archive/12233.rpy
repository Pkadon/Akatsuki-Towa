label avg12233:

stop music
scene avg_bg_023
$ update_narrator('c6891')
window show
with fade_in
get_char('c6891') '[convertstrid(1121120)]' (**arg(1, 1121120))
$ play_music("ed7519.ogg")
$ update_portrait('sc032_01 3', 'p40', [l(-17), light, flip], 6)
get_char('c401') '[convertstrid(1121121)]' (**arg(2, 1121121))
$ update_portrait('sc032_01 3', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c13') '[convertstrid(1121122)]' (**arg(3, 1121122))
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121123)]' (**arg(4, 1121123))
hide p40
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc031_01 5', 'p39', [l(-14), light, flip], 6)
get_char('c391') '[convertstrid(1121124)]' (**arg(5, 1121124))
hide p39
$ update_portrait('sc030_01 2', 'p38', [l(-12), light, flip], 6)
get_char('c381') '[convertstrid(1121125)]' (**arg(6, 1121125))
$ update_portrait('sc030_01 2', 'p38', [l(-12), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1121126)]' (**arg(7, 1121126))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc030_01 1', 'p38', [l(-12), light, flip], 6)
get_char('c381') '[convertstrid(1121127)]' (**arg(8, 1121127))
hide p38
$ update_portrait('sc032_01 2', 'p40', [l(-17), light, flip], 6)
get_char('c401') '[convertstrid(1121128)]' (**arg(9, 1121128))
$ update_portrait('sc032_01 2', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch28.ogg"
get_char('c23') '[convertstrid(1121129)]' (**arg(10, 1121129))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_c04_01.ogg"
get_char('c13') '[convertstrid(1121130)]' (**arg(11, 1121130))
hide p40
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc030_01 3', 'p38', [l(-12), light, flip], 6)
get_char('c381') '[convertstrid(1121131)]' (**arg(12, 1121131))
hide p1
$ update_portrait('sc030_01 3', 'p38', [l(-12), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121132)]' (**arg(13, 1121132))
hide p38
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
get_char('c6891') '[convertstrid(1121133)]' (**arg(14, 1121133))
$ update_portrait('sc030_01 4', 'p38', [l(-12), light, flip], 6)
get_char('c381') '[convertstrid(1121134)]' (**arg(15, 1121134))
hide p38
get_char('c6891') '[convertstrid(1121135)]' (**arg(16, 1121135))
return