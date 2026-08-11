label avg10721(trans=fade_in):

$ play_music("ed7564.ogg")
scene avg_bg_077
$ update_narrator('c13041')
window show
with trans
$ update_portrait('st061_01 4', 'p1304', [l_entrance(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1171121)]' (**arg(1, 1171121))
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1171122)]' (**arg(2, 1171122))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
get_char('c13041') '[convertstrid(1171123)]' (**arg(3, 1171123))
$ update_portrait('st061_01 2', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r_midback(-2), light], 6)
get_char('c13') '[convertstrid(1171124)]' (**arg(4, 1171124))
hide p1304
hide p1
play sfx2 "other_7007.ogg"
get_char('c0') '[convertstrid(1171125)]' (**arg(5, 1171125))
play sfx2 "fight_6022.ogg"
get_char('c0') '[convertstrid(1171126)]' (**arg(6, 1171126))
get_char('c5001') '[convertstrid(1171127)]' (**arg(7, 1171127))
get_char('c5001') '[convertstrid(1171128)]' (**arg(8, 1171128))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171129)]' (**arg(9, 1171129))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
get_char('c5001') '[convertstrid(1171130)]' (**arg(10, 1171130))
$ update_portrait('oc008_01 1', 'p8', [l_entrance(-5), light, flip], 6)
get_char('c81') '[convertstrid(1171131)]' (**arg(11, 1171131))
$ update_portrait('oc008_01 1', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1171132)]' (**arg(12, 1171132))
hide p8
hide p1
get_char('c0') '[convertstrid(1171133)]' (**arg(13, 1171133))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171134)]' (**arg(14, 1171134))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171135)]' (**arg(15, 1171135))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171136)]' (**arg(16, 1171136))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1171137)]' (**arg(17, 1171137))
$ update_portrait('oc008_01 1', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1171138)]' (**arg(18, 1171138))
$ update_portrait('oc008_01 1', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1171139)]' (**arg(19, 1171139))
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
$ update_portrait('oc008_01 4', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1171140)]' (**arg(20, 1171140))
$ update_portrait('oc008_01 1', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1171141)]' (**arg(21, 1171141))
$ update_portrait('oc008_01 1', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1171142)]' (**arg(22, 1171142))
$ play_music("ed7511.ogg")
$ update_portrait('oc008_01 4', 'p8', [l(-5), light, flip], 6)
play sfx2 "fight_6024.ogg"
get_char('c81') '[convertstrid(1171143)]' (**arg(23, 1171143))
$ update_portrait('oc008_01 4', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1171144)]' (**arg(24, 1171144))
hide p1
$ update_portrait('oc008_01 4', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('st061_01 3', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1171145)]' (**arg(25, 1171145))
$ update_portrait('st061_01 3', 'p1304', [r(-2), dark], 5)
$ update_portrait('oc008_01 1', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1171146)]' (**arg(26, 1171146))
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
get_char('c81') '[convertstrid(1171147)]' (**arg(27, 1171147))
hide p1304
$ update_portrait('oc008_01 5', 'p8', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
get_char('c13') '[convertstrid(1171148)]' (**arg(28, 1171148))
return "avg10721"