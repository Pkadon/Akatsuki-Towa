label avg10713:

$ play_music("ed7151.ogg")
scene avg_bg_207
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1170876)]' (**arg(1, 1170876))
get_char('c0') '[convertstrid(1170877)]' (**arg(2, 1170877))
$ update_portrait('oc002_01 3', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(1170878)]' (**arg(3, 1170878))
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc008_01 1', 'p8', [r(-5), light], 6)
get_char('c83') '[convertstrid(1170879)]' (**arg(4, 1170879))
$ update_portrait('oc008_01 2', 'p8', [r(-5), light], 6)
get_char('c83') '[convertstrid(1170880)]' (**arg(5, 1170880))
hide p2
hide p8
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1170881)]' (**arg(6, 1170881))
$ update_portrait('oc008_01 5', 'p8', [r(-5), light], 6)
get_char('c83') '[convertstrid(1170882)]' (**arg(7, 1170882))
$ update_portrait('oc008_01 5', 'p8', [r(-5), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1170883)]' (**arg(8, 1170883))
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1170884)]' (**arg(9, 1170884))
$ update_portrait('oc002_01 21', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc008_01 2', 'p8', [r(-5), light], 6)
get_char('c83') '[convertstrid(1170885)]' (**arg(10, 1170885))
$ update_portrait('oc008_01 6', 'p8', [r(-5), light], 6)
get_char('c83') '[convertstrid(1170886)]' (**arg(11, 1170886))
$ update_portrait('oc008_01 6', 'p8', [r(-5), dark], 5)
$ update_portrait('oc002_01 19', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1170887)]' (**arg(12, 1170887)) with shake
$ update_portrait('oc002_01 19', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc008_01 1', 'p8', [r(-5), light], 6)
get_char('c83') '[convertstrid(1170888)]' (**arg(13, 1170888))
$ update_portrait('oc008_01 5', 'p8', [r(-5), light], 6)
get_char('c83') '[convertstrid(1170889)]' (**arg(14, 1170889))
$ update_portrait('oc008_01 5', 'p8', [r(-5), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1170890)]' (**arg(15, 1170890))
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc008_01 6', 'p8', [r_exit(-5), light], 6)
get_char('c83') '[convertstrid(1170891)]' (**arg(16, 1170891))
hide p8
hide p2
get_char('c0') '[convertstrid(1170892)]' (**arg(17, 1170892))
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1170893)]' (**arg(18, 1170893))
return