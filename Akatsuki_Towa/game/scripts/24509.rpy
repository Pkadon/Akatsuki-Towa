label avg24509(trans=fade_in):

$ play_music("ed7200.ogg")
scene avg_bg_026
$ update_narrator('c23')
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
window show
with trans
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1206020)]' (**arg(1, 1206020))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1206021)]' (**arg(2, 1206021))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1206022)]' (**arg(3, 1206022))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1206046)]' (**arg(4, 1206046))
return "avg24509"