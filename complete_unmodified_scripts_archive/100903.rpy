label avg100903(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1218015)]' (**arg(1, 1218015))
hide p1
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
get_char('c93') '[convertstrid(1218016)]' (**arg(2, 1218016))
$ update_portrait('sc001_01 2', 'p9', [mid(-11), light], 6)
get_char('c93') '[convertstrid(1218017)]' (**arg(3, 1218017))
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
get_char('c93') '[convertstrid(1218018)]' (**arg(4, 1218018))
hide p9
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c13') '[convertstrid(1218019)]' (**arg(5, 1218019))
return "avg100903"