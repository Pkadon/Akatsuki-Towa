label avg24002(trans=fade_in):

$ play_music("ED6301.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with trans
get_char('c23') '[convertstrid(1200006)]' (**arg(1, 1200006))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200007)]' (**arg(2, 1200007))
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200008)]' (**arg(3, 1200008))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1200009)]' (**arg(4, 1200009))
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200010)]' (**arg(5, 1200010))
return "avg24002"