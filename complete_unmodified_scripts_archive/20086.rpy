label avg20086(trans=fade_in):

$ play_music("ed7106.ogg")
scene avg_bg_013
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
get_char('c21') '[convertstrid(1004469)]' (**arg(1, 1004469))
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('sc052_01 1', 'p59', [r_entrance(-25), light], 6)
get_char('c593') '[convertstrid(1004470)]' (**arg(2, 1004470))
$ update_portrait('sc052_01 1', 'p59', [r(-25), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c21') '[convertstrid(1004471)]' (**arg(3, 1004471))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004472)]' (**arg(4, 1004472))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004473)]' (**arg(5, 1004473))
hide p59
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc053_01 1', 'p60', [r(-32), light], 6)
get_char('c603') '[convertstrid(1004474)]' (**arg(6, 1004474))
hide p60
$ update_portrait('sc052_01 1', 'p59', [r(-25), light], 6)
get_char('c593') '[convertstrid(1004475)]' (**arg(7, 1004475))
$ update_portrait('sc052_01 1', 'p59', [r(-25), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c11') '[convertstrid(1004476)]' (**arg(8, 1004476))
hide p59
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc053_01 5', 'p60', [r(-32), light], 6)
get_char('c603') '[convertstrid(1004477)]' (**arg(9, 1004477))
$ update_portrait('sc053_01 5', 'p60', [r(-32), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1004478)]' (**arg(10, 1004478))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc053_01 4', 'p60', [r(-32), light], 6)
get_char('c603') '[convertstrid(1004479)]' (**arg(11, 1004479))
hide p1
$ update_portrait('sc053_01 4', 'p60', [r(-32), dark], 5)
$ update_portrait('sc052_01 4', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1004480)]' (**arg(12, 1004480))
hide p60
$ update_portrait('sc052_01 4', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1004481)]' (**arg(13, 1004481))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc052_01 4', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1004482)]' (**arg(14, 1004482))
$ update_portrait('sc052_01 4', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1004483)]' (**arg(15, 1004483))
hide p2
$ update_portrait('sc052_01 4', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1004484)]' (**arg(16, 1004484))
return "avg20086"