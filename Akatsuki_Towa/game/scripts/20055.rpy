label avg20055(trans=fade_in):

$ play_music("ed7151.ogg")
scene avg_bg_034
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1002895)]' (**arg(1, 1002895))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002896)]' (**arg(2, 1002896))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002897)]' (**arg(3, 1002897))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "other_7062.ogg"
get_char('c21') '[convertstrid(1002898)]' (**arg(4, 1002898))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r_midback(-2), light], 6)
get_char('c13') '[convertstrid(1002899)]' (**arg(5, 1002899))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1002900)]' (**arg(6, 1002900))
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002901)]' (**arg(7, 1002901))
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002902)]' (**arg(8, 1002902))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c21') '[convertstrid(1002903)]' (**arg(9, 1002903))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1002904)]' (**arg(10, 1002904))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002905)]' (**arg(11, 1002905))
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1002906)]' (**arg(12, 1002906))
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 3', 'p3', [r(-6), r_shake, light], 6)
play sfxvoice "avg_vocal_ro15.ogg"
get_char('c33') '[convertstrid(1002907)]' (**arg(13, 1002907))
hide p4
$ update_portrait('oc003_01 3', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002908)]' (**arg(14, 1002908))
hide p3
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002909)]' (**arg(15, 1002909))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002910)]' (**arg(16, 1002910))
return "avg20055"