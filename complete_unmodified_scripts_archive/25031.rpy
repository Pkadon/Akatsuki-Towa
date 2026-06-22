label avg25031:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1210076)]' (**arg(1, 1210076))
hide p2
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
play sfx2 "other_7079.ogg"
play sfxvoice "avg_vocal_na23.ogg"
get_char('c13') '[convertstrid(1210077)]' (**arg(2, 1210077))
return