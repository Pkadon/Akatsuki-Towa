label avg12471(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_007
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1143939)]' (**arg(1, 1143939))
get_char('c11663') '[convertstrid(1143940)]' (**arg(2, 1143940))
$ update_portrait('oc006_01 1', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1143941)]' (**arg(3, 1143941))
hide p6
play sfx2 "other_7024.ogg"
get_char('c0') '[convertstrid(1143942)]' (**arg(4, 1143942))
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1143943)]' (**arg(5, 1143943))
hide p6
play sfx2 "other_7024.ogg"
get_char('c0') '[convertstrid(1143944)]' (**arg(6, 1143944))
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1143945)]' (**arg(7, 1143945))
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1143946)]' (**arg(8, 1143946))
hide p6
get_char('c0') '[convertstrid(1143947)]' (**arg(9, 1143947))
$ play_music("ed7515.ogg")
scene avg_bg_078
show memoryoverlay zorder 2
$ update_narrator('c43')
with fade
get_char('c43') '[convertstrid(1143948)]' (**arg(10, 1143948))
get_char('c43') '[convertstrid(1143949)]' (**arg(11, 1143949))
scene avg_bg_065
show memoryoverlay zorder 2
$ update_narrator('c43')
with fade
get_char('c43') '[convertstrid(1143950)]' (**arg(12, 1143950))
get_char('c43') '[convertstrid(1143951)]' (**arg(13, 1143951))
scene avg_bg_049
show memoryoverlay zorder 2
$ update_narrator('c43')
with fade
get_char('c43') '[convertstrid(1143952)]' (**arg(14, 1143952))
scene avg_bg_007
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1143953)]' (**arg(15, 1143953))
get_char('c0') '[convertstrid(1143954)]' (**arg(16, 1143954))
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1143955)]' (**arg(17, 1143955))
hide p6
get_char('c0') '[convertstrid(1143956)]' (**arg(18, 1143956))
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1143957)]' (**arg(19, 1143957))
scene avg_bg_078
show memoryoverlay zorder 2
$ update_narrator('c5003')
with fade
get_char('c5003') '[convertstrid(1143958)]' (**arg(20, 1143958))
get_char('c5003') '[convertstrid(1143959)]' (**arg(21, 1143959))
get_char('c5003') '[convertstrid(1143960)]' (**arg(22, 1143960))
get_char('c5003') '[convertstrid(1143961)]' (**arg(23, 1143961))
scene avg_bg_007
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1143962)]' (**arg(24, 1143962))
stop music
play sfx2 "fight_6024.ogg"
get_char('c0') '[convertstrid(1143963)]' (**arg(25, 1143963))
$ play_music("ed7151.ogg")
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1143964)]' (**arg(26, 1143964))
scene avg_bg_070
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1143965)]' (**arg(27, 1143965))
get_char('c0') '[convertstrid(1143966)]' (**arg(28, 1143966))
return "avg12471"