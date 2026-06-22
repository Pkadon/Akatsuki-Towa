label avg12195:

$ play_music("ED6200.ogg")
scene avg_bg_027
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
play sfxvoice "avg_vocal_ch10.ogg"
get_char('c21') '[convertstrid(1120785)]' (**arg(1, 1120785))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120786)]' (**arg(2, 1120786))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120787)]' (**arg(3, 1120787))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1120788)]' (**arg(4, 1120788))
hide p2
hide p1
get_char('c0') '[convertstrid(1120789)]' (**arg(5, 1120789))
$ update_portrait('st017_01 5', 'p216', [r(-18), light], 6)
get_char('c2163') '[convertstrid(1120790)]' (**arg(6, 1120790))
$ update_portrait('st017_01 5', 'p216', [r(-18), dark], 5)
get_char('c9861') '[convertstrid(1120791)]' (**arg(7, 1120791))
hide p216
$ update_portrait('st018_01 4', 'p217', [r(-16), light], 6)
get_char('c2173') '[convertstrid(1120792)]' (**arg(8, 1120792))
hide p217
$ update_portrait('st019_01 2', 'p218', [r(-17), light], 6)
get_char('c2183') '[convertstrid(1120793)]' (**arg(9, 1120793))
$ update_portrait('st019_01 2', 'p218', [r(-17), dark], 5)
get_char('c9861') '[convertstrid(1120794)]' (**arg(10, 1120794))
hide p218
get_char('c9843') '[convertstrid(1120795)]' (**arg(11, 1120795))
$ update_portrait('st019_01 2', 'p218', [l(-17), light, flip], 6)
get_char('c2181') '[convertstrid(1120796)]' (**arg(12, 1120796))
hide p218
get_char('c0') '[convertstrid(1120797)]' (**arg(13, 1120797))
$ update_portrait('st018_01 2', 'p217', [l(-16), light, flip], 6)
get_char('c2171') '[convertstrid(1120798)]' (**arg(14, 1120798))
$ update_portrait('st018_01 2', 'p217', [l(-16), dark, flip], 5)
$ update_portrait('st016_01 4', 'p215', [r(-8), light], 6)
get_char('c2153') '[convertstrid(1120799)]' (**arg(15, 1120799))
hide p217
$ update_portrait('st016_01 4', 'p215', [r(-8), dark], 5)
$ update_portrait('st019_01 6', 'p218', [l(-17), light, flip], 6)
get_char('c2181') '[convertstrid(1120800)]' (**arg(16, 1120800))
hide p218
$ update_portrait('oc002_01 19', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120801)]' (**arg(17, 1120801))
$ update_portrait('oc002_01 19', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st016_01 2', 'p215', [r(-8), light], 6)
get_char('c2153') '[convertstrid(1120802)]' (**arg(18, 1120802))
$ update_portrait('st016_01 2', 'p215', [r(-8), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1120803)]' (**arg(19, 1120803))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st016_01 4', 'p215', [r(-8), light], 6)
get_char('c2153') '[convertstrid(1120804)]' (**arg(20, 1120804))
hide p215
get_char('c9833') '[convertstrid(1120805)]' (**arg(21, 1120805))
return