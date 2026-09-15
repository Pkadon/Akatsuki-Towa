label avg24011(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_039
$ update_portrait('st026_01 1', 'p225', [l(-14), light, flip], 6)
$ update_narrator('c2251')
window show
with trans
get_char('c2251') '[convertstrid(1200039)]' (**arg(1, 1200039))
$ update_portrait('st026_01 1', 'p225', [l(-14), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200040)]' (**arg(2, 1200040))
return "avg24011"