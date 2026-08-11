label avg25262(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch19.ogg"
get_char('c23') '[convertstrid(1210976)]' (**arg(1, 1210976))
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6025.ogg"
get_char('c13') '[convertstrid(1210977)]' (**arg(2, 1210977))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210978)]' (**arg(3, 1210978))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6026.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210979)]' (**arg(4, 1210979))
hide p2
play sfx2 "other_7068.ogg"
get_char('c0') '[convertstrid(1210980)]' (**arg(5, 1210980))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na18.ogg"
get_char('c13') '[convertstrid(1210981)]' (**arg(6, 1210981))
return "avg25262"