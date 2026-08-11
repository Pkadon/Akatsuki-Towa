label avg20015(trans=fade_in):

$ play_music("ED6518.ogg")
scene placeholderbackground
$ update_narrator('c5173')
window show
with trans
play sfx2 "common_select.ogg"
get_char('c5173') '[convertstrid(1000948)]' (**arg(1, 1000948))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1000949)]' (**arg(2, 1000949))
return "avg20015"