label avg20033(trans=fade_in):

$ play_music("ed7104.ogg")
scene avg_bg_023
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1002223)]' (**arg(1, 1002223))
get_char('c0') '[convertstrid(1002224)]' (**arg(2, 1002224))
get_char('c0') '[convertstrid(1002225)]' (**arg(3, 1002225))
get_char('c0') '[convertstrid(1002226)]' (**arg(4, 1002226))
get_char('c0') '[convertstrid(1002227)]' (**arg(5, 1002227))
get_char('c0') '[convertstrid(1002228)]' (**arg(6, 1002228))
get_char('c0') '[convertstrid(1002229)]' (**arg(7, 1002229))
get_char('c0') '[convertstrid(1002230)]' (**arg(8, 1002230))
get_char('c0') '[convertstrid(1002231)]' (**arg(9, 1002231))
get_char('c0') '[convertstrid(1002232)]' (**arg(10, 1002232))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1002233)]' (**arg(11, 1002233))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro03.ogg"
get_char('c31') '[convertstrid(1002234)]' (**arg(12, 1002234))
hide p3
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002235)]' (**arg(13, 1002235))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002236)]' (**arg(14, 1002236))
hide p2
hide p1
get_char('c0') '[convertstrid(1002237)]' (**arg(15, 1002237))
get_char('c0') '[convertstrid(1002238)]' (**arg(16, 1002238))
get_char('c0') '[convertstrid(1002239)]' (**arg(17, 1002239))
get_char('c0') '[convertstrid(1002240)]' (**arg(18, 1002240))
get_char('c0') '[convertstrid(1002241)]' (**arg(19, 1002241))
get_char('c0') '[convertstrid(1002242)]' (**arg(20, 1002242))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1002243)]' (**arg(21, 1002243))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002244)]' (**arg(22, 1002244))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1002245)]' (**arg(23, 1002245))
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1002246)]' (**arg(24, 1002246))
hide p1
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
get_char('c5613') '[convertstrid(1002247)]' (**arg(25, 1002247))
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c11') '[convertstrid(1002248)]' (**arg(26, 1002248))
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1002249)]' (**arg(27, 1002249))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1002250)]' (**arg(28, 1002250))
hide p2
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1002251)]' (**arg(29, 1002251))
hide p3
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
get_char('c5613') '[convertstrid(1002252)]' (**arg(30, 1002252))
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c11') '[convertstrid(1002253)]' (**arg(31, 1002253))
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
get_char('c5613') '[convertstrid(1002254)]' (**arg(32, 1002254))
return "avg20033"