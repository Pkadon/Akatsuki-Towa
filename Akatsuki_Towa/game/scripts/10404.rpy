label avg10404(trans=fade_in):

$ play_music("ED6518.ogg")
scene avg_bg_001
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_select.ogg"
get_char('c13') '[convertstrid(1140286)]' (**arg(1, 1140286))
return "avg10404"