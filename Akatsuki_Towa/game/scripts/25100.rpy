label avg25100:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1210280)]' (**arg(1, 1210280))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6025.ogg"
get_char('c13') '[convertstrid(1210281)]' (**arg(2, 1210281))
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1210282)]' (**arg(3, 1210282))
hide p2
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210283)]' (**arg(4, 1210283))
return