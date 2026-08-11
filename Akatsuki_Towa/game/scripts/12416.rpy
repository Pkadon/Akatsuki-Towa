label avg12416(trans=fade_in):

$ play_music("ed6564.ogg")
scene avg_bg_004
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with trans
play sfxvoice "avg_vocal_li03.ogg"
get_char('c41') '[convertstrid(1142756)]' (**arg(1, 1142756))
return "avg12416"