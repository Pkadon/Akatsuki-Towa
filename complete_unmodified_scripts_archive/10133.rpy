label avg10133(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_015
$ update_portrait('oc001_01 22', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
play sfx2 "other_7072.ogg"
get_char('c11') '[convertstrid(1007347)]' (**arg(1, 1007347))
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007348)]' (**arg(2, 1007348))
$ update_portrait('oc001_01 11', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007349)]' (**arg(3, 1007349))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c11') '[convertstrid(1007350)]' (**arg(4, 1007350))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1007351)]' (**arg(5, 1007351))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7073.ogg"
play sfxvoice "avg_vocal_na06.ogg"
get_char('c11') '[convertstrid(1007352)]' (**arg(6, 1007352))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r_midback(-3), light], 6)
get_char('c23') '[convertstrid(1007353)]' (**arg(7, 1007353))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7020.ogg"
get_char('c11') '[convertstrid(1007354)]' (**arg(8, 1007354))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007355)]' (**arg(9, 1007355))
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007356)]' (**arg(10, 1007356))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch09.ogg"
get_char('c23') '[convertstrid(1007357)]' (**arg(11, 1007357))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007358)]' (**arg(12, 1007358))
return "avg10133"