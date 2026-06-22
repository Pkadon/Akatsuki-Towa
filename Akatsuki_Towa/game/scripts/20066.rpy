label avg20066:

$ play_music("ED6104.ogg")
scene avg_bg_070
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1003452)]' (**arg(1, 1003452))
get_char('c0') '[convertstrid(1003453)]' (**arg(2, 1003453))
get_char('c0') '[convertstrid(1003454)]' (**arg(3, 1003454))
get_char('c0') '[convertstrid(1003455)]' (**arg(4, 1003455))
scene avg_bg_027
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c21') '[convertstrid(1003456)]' (**arg(5, 1003456))
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1003457)]' (**arg(6, 1003457))
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1003458)]' (**arg(7, 1003458))
hide p3
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1003459)]' (**arg(8, 1003459))
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1003460)]' (**arg(9, 1003460))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1003461)]' (**arg(10, 1003461))
hide p1
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003462)]' (**arg(11, 1003462))
$ update_portrait('oc002_01 14', 'p2', [l_exit(-3), light, flip], 6)
get_char('c21') '[convertstrid(1003463)]' (**arg(12, 1003463))
hide p2
$ update_portrait('oc001_01 7', 'p1', [l_exit(-2), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c11') '[convertstrid(1003464)]' (**arg(13, 1003464))
hide p1
return