label avg12249:

$ play_music("ed7111.ogg")
scene avg_bg_012
$ update_narrator('c7091')
window show
with fade_in
$ update_portrait('st051_01 2', 'p709', [l_entrance(-9), light, flip], 6)
play sfx2 "other_7042.ogg"
get_char('c7091') '[convertstrid(1121350)]' (**arg(1, 1121350))
$ update_portrait('st051_01 2', 'p709', [l(-9), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1121351)]' (**arg(2, 1121351))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('st051_01 1', 'p709', [l(-9), light, flip], 6)
play sfx2 "other_7022.ogg"
get_char('c7091') '[convertstrid(1121352)]' (**arg(3, 1121352))
$ update_portrait('st051_01 1', 'p709', [l(-9), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1121353)]' (**arg(4, 1121353))
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('st051_01 2', 'p709', [l(-9), light, flip], 6)
get_char('c7091') '[convertstrid(1121354)]' (**arg(5, 1121354))
return