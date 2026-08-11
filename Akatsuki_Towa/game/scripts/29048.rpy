label avg29048(trans=fade_in):

$ play_music("ed9999.ogg")
scene avg_bg_050
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1100045)]' (**arg(1, 1100045))
return "avg29048"