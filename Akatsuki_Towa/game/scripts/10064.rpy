label avg10064(trans=fade_in):

$ play_music("ED6103.ogg")
scene avg_bg_038
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
play sfx2 "common_menu.ogg"
get_char('c11') '[convertstrid(1005000)]' (**arg(1, 1005000))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1005001)]' (**arg(2, 1005001))
hide p15
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005002)]' (**arg(3, 1005002))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1005003)]' (**arg(4, 1005003))
hide p2
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1005004)]' (**arg(5, 1005004))
hide p4
$ update_portrait('sc039_01 5', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1005005)]' (**arg(6, 1005005))
$ update_portrait('sc039_01 5', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
get_char('c11') '[convertstrid(1005006)]' (**arg(7, 1005006))
hide p46
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1005007)]' (**arg(8, 1005007))
return "avg10064"