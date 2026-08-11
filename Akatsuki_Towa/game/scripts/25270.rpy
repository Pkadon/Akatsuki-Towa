label avg25270(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na13.ogg"
get_char('c13') '[convertstrid(1211012)]' (**arg(1, 1211012))
hide p1
play sfx2 "other_7079.ogg"
get_char('c20133') '[convertstrid(1211013)]' (**arg(2, 1211013))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1211014)]' (**arg(3, 1211014))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na10.ogg"
get_char('c13') '[convertstrid(1211015)]' (**arg(4, 1211015))
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1211016)]' (**arg(5, 1211016))
hide p2
play sfx2 "fight_6003.ogg"
get_char('c20133') '[convertstrid(1211017)]' (**arg(6, 1211017))
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1211018)]' (**arg(7, 1211018))
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na15.ogg"
get_char('c13') '[convertstrid(1211019)]' (**arg(8, 1211019))
return "avg25270"