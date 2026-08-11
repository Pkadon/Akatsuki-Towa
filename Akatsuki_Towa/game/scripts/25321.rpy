label avg25321(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7051.ogg"
play sfxvoice "avg_vocal_na10.ogg"
get_char('c13') '[convertstrid(1211241)]' (**arg(1, 1211241))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch07.ogg"
get_char('c23') '[convertstrid(1211242)]' (**arg(2, 1211242))
return "avg25321"