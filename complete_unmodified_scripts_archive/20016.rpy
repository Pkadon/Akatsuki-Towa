label avg20016(trans=fade_in):

$ play_music("ED6518.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfx2 "common_cancel.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
get_char('c23') '[convertstrid(1000950)]' (**arg(1, 1000950))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1000951)]' (**arg(2, 1000951))
return "avg20016"