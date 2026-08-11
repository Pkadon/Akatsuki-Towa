label avg12037(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
window show
with trans
get_char('c561') '[convertstrid(1120243)]' (**arg(1, 1120243))
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120244)]' (**arg(2, 1120244))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120245)]' (**arg(3, 1120245))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1120246)]' (**arg(4, 1120246))
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1120247)]' (**arg(5, 1120247))
hide p1
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120248)]' (**arg(6, 1120248))
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1120249)]' (**arg(7, 1120249))
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c23') '[convertstrid(1120250)]' (**arg(8, 1120250))
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120251)]' (**arg(9, 1120251))
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
get_char('c561') '[convertstrid(1120252)]' (**arg(10, 1120252))
hide p1
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1120253)]' (**arg(11, 1120253))
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120254)]' (**arg(12, 1120254))
return "avg12037"