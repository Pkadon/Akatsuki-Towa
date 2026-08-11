label avg10340(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_003
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1131007)]' (**arg(1, 1131007))
return "avg10340"