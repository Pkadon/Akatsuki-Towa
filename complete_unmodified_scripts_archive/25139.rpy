label avg25139:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1210432)]' (**arg(1, 1210432))
hide p1
play sfx2 "other_7004.ogg"
get_char('c0') '[convertstrid(1210433)]' (**arg(2, 1210433))
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1210434)]' (**arg(3, 1210434))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
get_char('c13') '[convertstrid(1210435)]' (**arg(4, 1210435))
return