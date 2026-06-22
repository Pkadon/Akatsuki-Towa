label avg22156:

stop music
scene placeholderbackground
$ update_portrait('oc003_01 2', 'p3', [mid(-6), light], 6)
$ update_narrator('c33')
window show
with fade_in
play sfxvoice "avg_vocal_ro09.ogg"
get_char('c33') '[convertstrid(1128404)]' (**arg(1, 1128404))
hide p3
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1128405)]' (**arg(2, 1128405))
return