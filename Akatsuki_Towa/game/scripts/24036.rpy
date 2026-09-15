label avg24036(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_014
$ update_narrator('c7621')
window show
with trans
get_char('c7621') '[convertstrid(1200146)]' (**arg(1, 1200146))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200147)]' (**arg(2, 1200147))
return "avg24036"