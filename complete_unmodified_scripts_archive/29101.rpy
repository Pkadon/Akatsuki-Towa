label avg29101:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1218008)]' (**arg(1, 1218008))
hide p1
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
get_char('c93') '[convertstrid(1218009)]' (**arg(2, 1218009))
$ update_portrait('sc001_01 2', 'p9', [mid(-11), light], 6)
get_char('c93') '[convertstrid(1218010)]' (**arg(3, 1218010))
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
get_char('c93') '[convertstrid(1218011)]' (**arg(4, 1218011))
hide p9
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1218012)]' (**arg(5, 1218012))
return