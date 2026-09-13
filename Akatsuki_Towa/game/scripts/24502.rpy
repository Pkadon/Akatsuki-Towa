label avg24502(trans=fade_in):

$ play_music("ED6200.ogg")
scene avg_bg_010
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1206003)]' (**arg(1, 1206003))
return "avg24502"