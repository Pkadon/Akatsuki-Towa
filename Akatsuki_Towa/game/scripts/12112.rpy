label avg12112:

$ play_music("ed7117.ogg")
scene avg_bg_017
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1128142)]' (**arg(1, 1128142))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na08.ogg"
get_char('c13') '[convertstrid(1128143)]' (**arg(2, 1128143))
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('sc067_01 2', 'p956', [l(-38), light, flip], 6)
play sfx2 "other_7021.ogg"
get_char('c9561') '[convertstrid(1128144)]' (**arg(3, 1128144))
hide p1
$ update_portrait('sc067_01 2', 'p956', [l(-38), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1128145)]' (**arg(4, 1128145))
hide p3
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128146)]' (**arg(5, 1128146))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128147)]' (**arg(6, 1128147))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('sc067_01 1', 'p956', [l(-38), light, flip], 6)
get_char('c9561') '[convertstrid(1128148)]' (**arg(7, 1128148))
hide p1
$ update_portrait('sc067_01 1', 'p956', [l(-38), dark, flip], 5)
$ update_portrait('oc003_01 7', 'p3', [r(-6), light], 6)
play sfx2 "other_7004.ogg"
get_char('c33') '[convertstrid(1128149)]' (**arg(8, 1128149))
hide p956
hide p3
get_char('c0') '[convertstrid(1128150)]' (**arg(9, 1128150))
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1128151)]' (**arg(10, 1128151))
get_char('c0') '[convertstrid(1128152)]' (**arg(11, 1128152))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1128153)]' (**arg(12, 1128153, size=(1.2)))
hide p1
$ update_portrait('oc003_01 14', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1128154)]' (**arg(13, 1128154))
$ update_portrait('oc003_01 14', 'p3', [r(-6), dark], 5)
$ update_portrait('sc067_01 1', 'p71', [l(-38), light, flip], 6)
get_char('c711') '[convertstrid(1128155)]' (**arg(14, 1128155))
$ update_portrait('sc067_01 2', 'p71', [l(-38), light, flip], 6)
get_char('c711') '[convertstrid(1128156)]' (**arg(15, 1128156))
hide p3
$ update_portrait('sc067_01 2', 'p71', [l(-38), dark, flip], 5)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128157)]' (**arg(16, 1128157))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128158)]' (**arg(17, 1128158, size=(1.2))) with shake
$ update_portrait('oc001_01 15', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128159)]' (**arg(18, 1128159))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128160)]' (**arg(19, 1128160))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128161)]' (**arg(20, 1128161))
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('sc067_01 4', 'p71', [l(-38), light, flip], 6)
get_char('c711') '[convertstrid(1128162)]' (**arg(21, 1128162))
$ update_portrait('sc067_01 5', 'p71', [l(-38), light, flip], 6)
get_char('c711') '[convertstrid(1128163)]' (**arg(22, 1128163))
stop music
scene avg_bg_070
$ update_portrait('oc001_01 14', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfx2 "other_7057.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1128164)]' (**arg(23, 1128164)) with shake
$ play_music("ed7117.ogg")
scene avg_bg_017
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfx2 "other_7088.ogg"
get_char('c21') '[convertstrid(1128165)]' (**arg(24, 1128165))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1128166)]' (**arg(25, 1128166))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128167)]' (**arg(26, 1128167))
hide p2
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128168)]' (**arg(27, 1128168))
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 24', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1128169)]' (**arg(28, 1128169))
$ update_portrait('oc001_01 24', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128170)]' (**arg(29, 1128170))
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128171)]' (**arg(30, 1128171))
$ update_portrait('oc003_01 13', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128172)]' (**arg(31, 1128172))
hide p3
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128173)]' (**arg(32, 1128173))
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1128174)]' (**arg(33, 1128174))
$ update_portrait('oc002_01 13', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128175)]' (**arg(34, 1128175))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1128176)]' (**arg(35, 1128176))
hide p3
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c21') '[convertstrid(1128177)]' (**arg(36, 1128177))
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c21') '[convertstrid(1128178)]' (**arg(37, 1128178))
hide p2
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro04.ogg"
get_char('c31') '[convertstrid(1128179)]' (**arg(38, 1128179))
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1128180)]' (**arg(39, 1128180))
return