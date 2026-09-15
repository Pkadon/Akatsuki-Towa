label avg24005(trans=fade_in):

$ play_music("ed7304.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1200016)]' (**arg(1, 1200016))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r_midback(-3), light], 6)
get_char('c23') '[convertstrid(1200017)]' (**arg(2, 1200017))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200018)]' (**arg(3, 1200018))
return "avg24005"