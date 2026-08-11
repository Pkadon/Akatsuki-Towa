label avg24096(trans=fade_in):

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
get_char('c21') '[convertstrid(1200340)]' (**arg(1, 1200340))
return "avg24096"