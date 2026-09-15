label avg24088(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_046
$ update_narrator('c10151')
window show
with trans
get_char('c10151') '[convertstrid(1200322)]' (**arg(1, 1200322))
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200323)]' (**arg(2, 1200323))
return "avg24088"