label avg12477:

$ play_music("ed7151.ogg")
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1144081)]' (**arg(1, 1144081))
get_char('c0') '[convertstrid(1144082)]' (**arg(2, 1144082))
$ update_portrait('oc006_01 1', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1144083)]' (**arg(3, 1144083))
$ update_portrait('oc006_01 3', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1144084)]' (**arg(4, 1144084))
scene avg_bg_070
show memoryoverlay zorder 2
$ update_portrait('oc004_01 15', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
with fade
get_char('c43') '[convertstrid(1144085)]' (**arg(5, 1144085))
$ update_portrait('oc004_01 15', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1144086)]' (**arg(6, 1144086))
scene placeholderbackground
$ update_narrator('c61')
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
with fade
$ update_portrait('oc006_01 4', 'p6', [l(-5), l_shake, light, flip], 6)
get_char('c61') '[convertstrid(1144087)]' (**arg(7, 1144087))
hide p6
get_char('c0') '[convertstrid(1144088)]' (**arg(8, 1144088))
get_char('c0') '[convertstrid(1144089)]' (**arg(9, 1144089))
$ update_portrait('oc006_01 4', 'p6', [l(-5), light, flip], 6)
get_char('c61') '[convertstrid(1144090)]' (**arg(10, 1144090))
$ update_portrait('oc006_01 3', 'p6', [l(-5), l_shake, light, flip], 6)
get_char('c61') '[convertstrid(1144091)]' (**arg(11, 1144091))
hide p6
get_char('c0') '[convertstrid(1144092)]' (**arg(12, 1144092))
return