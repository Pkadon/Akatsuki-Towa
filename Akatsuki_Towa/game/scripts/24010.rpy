label avg24010(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_039
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200032)]' (**arg(1, 1200032))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('st026_01 2', 'p225', [l(-14), light, flip], 6)
get_char('c2251') '[convertstrid(1200033)]' (**arg(2, 1200033))
$ update_portrait('st026_01 2', 'p225', [l(-14), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200034)]' (**arg(3, 1200034))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200035)]' (**arg(4, 1200035))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('st026_01 1', 'p225', [l(-14), light, flip], 6)
get_char('c2251') '[convertstrid(1200036)]' (**arg(5, 1200036))
$ update_portrait('st026_01 5', 'p225', [l(-14), light, flip], 6)
get_char('c2251') '[convertstrid(1200037)]' (**arg(6, 1200037))
hide p1
$ update_portrait('st026_01 5', 'p225', [l(-14), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200038)]' (**arg(7, 1200038))
return "avg24010"