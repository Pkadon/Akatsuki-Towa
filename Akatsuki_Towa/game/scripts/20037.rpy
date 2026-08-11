label avg20037(trans=fade_in):

$ play_music("ED6505.ogg")
scene avg_bg_027
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(1007684)]' (**arg(1, 1007684))
play sfx2 "other_7064.ogg"
get_char('c5671') '[convertstrid(1002305)]' (**arg(2, 1002305))
get_char('c5683') '[convertstrid(1002306)]' (**arg(3, 1002306))
get_char('c5683') '[convertstrid(1002307)]' (**arg(4, 1002307))
get_char('c5683') '[convertstrid(1002308)]' (**arg(5, 1002308))
get_char('c5683') '[convertstrid(1002309)]' (**arg(6, 1002309))
get_char('c5671') '[convertstrid(1002310)]' (**arg(7, 1002310))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1002311)]' (**arg(8, 1002311))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c21') '[convertstrid(1002312)]' (**arg(9, 1002312))
return "avg20037"