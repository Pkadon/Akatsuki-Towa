label avg12226(trans=fade_in):

$ play_music("ed7569.ogg")
scene avg_bg_036
$ update_portrait('uc004_02 2', 'p990', [l(-6), light, flip], 6)
$ update_narrator('c9901')
window show
with trans
play sfx2 "other_7018.ogg"
get_char('c9901') '[convertstrid(1121038)]' (**arg(1, 1121038))
$ update_portrait('uc004_02 2', 'p990', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 17', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1121039)]' (**arg(2, 1121039))
hide p990
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121040)]' (**arg(3, 1121040))
hide p1
$ update_portrait('uc004_02 2', 'p990', [l(-6), light, flip], 6)
get_char('c9901') '[convertstrid(1121492)]' (**arg(4, 1121492))
hide p2
$ update_portrait('uc004_02 2', 'p990', [l(-6), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1121041)]' (**arg(5, 1121041))
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('uc004_02 2', 'p990', [l(-6), light, flip], 6)
get_char('c9901') '[convertstrid(1121042)]' (**arg(6, 1121042))
hide p46
$ update_portrait('uc004_02 2', 'p990', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121493)]' (**arg(7, 1121493))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('uc004_02 2', 'p990', [l(-6), light, flip], 6)
get_char('c9901') '[convertstrid(1121043)]' (**arg(8, 1121043))
hide p2
$ update_portrait('uc004_02 2', 'p990', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r_midback(-2), light], 6)
play sfx2 "other_7002.ogg"
get_char('c13') '[convertstrid(1121044)]' (**arg(9, 1121044))
hide p1
$ update_portrait('oc002_01 11', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1121045)]' (**arg(10, 1121045))
$ update_portrait('oc002_01 11', 'p2', [r(-3), dark], 5)
$ update_portrait('uc004_02 2', 'p990', [l(-6), light, flip], 6)
get_char('c9901') '[convertstrid(1121046)]' (**arg(11, 1121046))
hide p2
$ update_portrait('uc004_02 2', 'p990', [l(-6), dark, flip], 5)
$ update_portrait('sc039_01 1', 'p46', [r(-13), light], 6)
get_char('c463') '[convertstrid(1121047)]' (**arg(12, 1121047))
hide p990
$ update_portrait('sc039_01 1', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121494)]' (**arg(13, 1121494))
return "avg12226"