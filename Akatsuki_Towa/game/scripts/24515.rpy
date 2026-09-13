label avg24515(trans=fade_in):

$ play_music("ED6301.ogg")
scene placeholderbackground
$ update_narrator('c11')
$ update_portrait('oc001_01 13', 'p1', [l(-2), light, flip], 6)
window show
with trans
$ update_portrait('oc001_01 13', 'p1', [l(-2), l_shake, light, flip], 6)
get_char('c11') '[convertstrid(1206039)]' (**arg(1, 1206039))
$ update_portrait('oc001_01 13', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1206040)]' (**arg(2, 1206040))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1206041)]' (**arg(3, 1206041))
return "avg24515"