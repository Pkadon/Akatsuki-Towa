label avg25143:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_cancel.ogg"
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1210454)]' (**arg(1, 1210454))
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c23') '[convertstrid(1210455)]' (**arg(2, 1210455))
return