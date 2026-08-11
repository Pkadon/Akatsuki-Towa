label avg22312(trans=fade_in):

$ play_music("ed7305.ogg")
scene avg_bg_051
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1133255)]' (**arg(1, 1133255))
return "avg22312"