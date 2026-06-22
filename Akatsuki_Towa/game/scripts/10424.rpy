label avg10424:

$ play_music("ed7101.ogg")
scene avg_bg_020
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1141200)]' (**arg(1, 1141200))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro02.ogg"
get_char('c31') '[convertstrid(1141201)]' (**arg(2, 1141201))
hide p1
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1141202)]' (**arg(3, 1141202))
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch19.ogg"
get_char('c23') '[convertstrid(1141203)]' (**arg(4, 1141203))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1141204)]' (**arg(5, 1141204))
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141205)]' (**arg(6, 1141205))
hide p3
hide p1
play sfx2 "other_7088.ogg"
get_char('c0') '[convertstrid(1141206)]' (**arg(7, 1141206))
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1141207)]' (**arg(8, 1141207))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na19.ogg"
get_char('c13') '[convertstrid(1141208)]' (**arg(9, 1141208))
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1141209)]' (**arg(10, 1141209))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1141210)]' (**arg(11, 1141210))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1141211)]' (**arg(12, 1141211))
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfx2 "other_7043.ogg"
get_char('c13') '[convertstrid(1141212)]' (**arg(13, 1141212))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141213)]' (**arg(14, 1141213))
hide p4
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1141214)]' (**arg(15, 1141214))
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1141215)]' (**arg(16, 1141215))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfx2 "other_7043.ogg"
play sfxvoice "avg_vocal_na11_b.ogg"
get_char('c13') '[convertstrid(1141216)]' (**arg(17, 1141216))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro14.ogg"
get_char('c31') '[convertstrid(1141217)]' (**arg(18, 1141217))
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141218)]' (**arg(19, 1141218))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro03.ogg"
get_char('c31') '[convertstrid(1141219)]' (**arg(20, 1141219))
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1141220)]' (**arg(21, 1141220))
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7045.ogg"
get_char('c31') '[convertstrid(1141221)]' (**arg(22, 1141221))
hide p3
hide p1
$ update_narrator('c0')
with fade
get_char('c0') '[convertstrid(1141222)]' (**arg(23, 1141222))
$ update_portrait('oc004_01 22', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li29.ogg"
get_char('c43') '[convertstrid(1141223)]' (**arg(24, 1141223))
$ update_portrait('oc004_01 22', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro04.ogg"
get_char('c31') '[convertstrid(1141224)]' (**arg(25, 1141224))
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1141225)]' (**arg(26, 1141225))
hide p3
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch17.ogg"
get_char('c21') '[convertstrid(1141226)]' (**arg(27, 1141226))
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1141227)]' (**arg(28, 1141227))
return