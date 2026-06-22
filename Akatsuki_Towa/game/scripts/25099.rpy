label avg25099:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c23') '[convertstrid(1210276)]' (**arg(1, 1210276))
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1210277)]' (**arg(2, 1210277))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6025.ogg"
get_char('c13') '[convertstrid(1210278)]' (**arg(3, 1210278))
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210279)]' (**arg(4, 1210279))
return