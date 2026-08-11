label avg20070(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_018
$ update_narrator('c13')
window show
with trans
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7064.ogg"
get_char('c13') '[convertstrid(1003886)]' (**arg(1, 1003886))
hide p1
get_char('c6483') '[convertstrid(1003887)]' (**arg(2, 1003887))
get_char('c6491') '[convertstrid(1003888)]' (**arg(3, 1003888))
get_char('c6503') '[convertstrid(1003889)]' (**arg(4, 1003889))
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1003890)]' (**arg(5, 1003890))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li17.ogg"
get_char('c41') '[convertstrid(1003891)]' (**arg(6, 1003891))
hide p4
hide p1
$ update_narrator('c0')
with fade
play sfx2 "other_7021.ogg"
get_char('c0') '[convertstrid(1003892)]' (**arg(7, 1003892))
play sfx2 "other_7004.ogg"
get_char('c6491') '[convertstrid(1003893)]' (**arg(8, 1003893))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003894)]' (**arg(9, 1003894))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c6491') '[convertstrid(1003895)]' (**arg(10, 1003895))
get_char('c6491') '[convertstrid(1003896)]' (**arg(11, 1003896))
get_char('c6491') '[convertstrid(1003897)]' (**arg(12, 1003897))
hide p1
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1003898)]' (**arg(13, 1003898))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
play sfx2 "other_7021.ogg"
get_char('c6511') '[convertstrid(1003899)]' (**arg(14, 1003899))
get_char('c6511') '[convertstrid(1003900)]' (**arg(15, 1003900))
get_char('c6511') '[convertstrid(1003901)]' (**arg(16, 1003901))
get_char('c6491') '[convertstrid(1003902)]' (**arg(17, 1003902))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003903)]' (**arg(18, 1003903))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1003904)]' (**arg(19, 1003904))
return "avg20070"