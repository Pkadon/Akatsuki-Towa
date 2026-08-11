label avg1022(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_023
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(2100434)]' (**arg(1, 2100434))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100435)]' (**arg(2, 2100435))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100436)]' (**arg(3, 2100436))
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100437)]' (**arg(4, 2100437))
hide p1
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c23') '[convertstrid(2100438)]' (**arg(5, 2100438))
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(2100439)]' (**arg(6, 2100439))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100440)]' (**arg(7, 2100440))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100441)]' (**arg(8, 2100441))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100442)]' (**arg(9, 2100442))
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100443)]' (**arg(10, 2100443))
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100444)]' (**arg(11, 2100444))
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100445)]' (**arg(12, 2100445))
hide p2
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100446)]' (**arg(13, 2100446))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100447)]' (**arg(14, 2100447))
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100448)]' (**arg(15, 2100448))
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100449)]' (**arg(16, 2100449))
hide p1
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100450)]' (**arg(17, 2100450))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100451)]' (**arg(18, 2100451))
return "avg1022"