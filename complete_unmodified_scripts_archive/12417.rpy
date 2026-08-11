label avg12417(trans=fade_in):

$ play_music("ed6564.ogg")
scene avg_bg_004
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with trans
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c21') '[convertstrid(1142758)]' (**arg(1, 1142758))
return "avg12417"