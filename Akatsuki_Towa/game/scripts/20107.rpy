label avg20107(trans=fade_in):

$ play_music("ED6103.ogg")
scene avg_bg_072
$ update_narrator('c11')
window show
with trans
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7047.ogg"
get_char('c11') '[convertstrid(1005213)]' (**arg(1, 1005213))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c6873') '[convertstrid(1005214)]' (**arg(2, 1005214))
hide p1
get_char('c0') '[convertstrid(1005215)]' (**arg(3, 1005215))
get_char('c6873') '[convertstrid(1005216)]' (**arg(4, 1005216))
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005217)]' (**arg(5, 1005217))
hide p1
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1005218)]' (**arg(6, 1005218))
$ update_portrait('sc039_01 5', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1005219)]' (**arg(7, 1005219))
$ update_portrait('sc039_01 5', 'p46', [l(-13), dark, flip], 5)
get_char('c6873') '[convertstrid(1005220)]' (**arg(8, 1005220))
hide p46
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005221)]' (**arg(9, 1005221))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
get_char('c6873') '[convertstrid(1005222)]' (**arg(10, 1005222))
get_char('c6873') '[convertstrid(1005223)]' (**arg(11, 1005223))
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
with fade
play sfxvoice "avg_vocal_ch19.ogg"
get_char('c21') '[convertstrid(1005224)]' (**arg(12, 1005224))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005225)]' (**arg(13, 1005225))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005226)]' (**arg(14, 1005226))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1005227)]' (**arg(15, 1005227))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1005229)]' (**arg(16, 1005229))
hide p1
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005230)]' (**arg(17, 1005230))
hide p15
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005231)]' (**arg(18, 1005231))
return "avg20107"