label avg10310(trans=fade_in):

$ play_music("ed7124.ogg")
scene avg_bg_059
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "common_cancel.ogg"
get_char('c13') '[convertstrid(1130291)]' (**arg(1, 1130291))
hide p1
get_char('c10063') '[convertstrid(1130292)]' (**arg(2, 1130292))
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li18.ogg"
get_char('c41') '[convertstrid(1130293)]' (**arg(3, 1130293))
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1130294)]' (**arg(4, 1130294))
return "avg10310"