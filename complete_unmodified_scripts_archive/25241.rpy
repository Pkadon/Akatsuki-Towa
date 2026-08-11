label avg25241(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_atk_01.ogg"
get_char('c13') '[convertstrid(1210869)]' (**arg(1, 1210869))
hide p1
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_hurt_01.ogg"
get_char('c23') '[convertstrid(1210870)]' (**arg(2, 1210870))
hide p2
get_char('c20143') '[convertstrid(1210871)]' (**arg(3, 1210871))
$ update_portrait('oc002_01 15', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch16.ogg"
get_char('c23') '[convertstrid(1210872)]' (**arg(4, 1210872))
hide p2
play sfx2 "other_7075.ogg"
get_char('c20143') '[convertstrid(1210873)]' (**arg(5, 1210873))
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1210874)]' (**arg(6, 1210874))
hide p1
get_char('c20143') '[convertstrid(1210875)]' (**arg(7, 1210875))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210876)]' (**arg(8, 1210876))
hide p2
get_char('c20143') '[convertstrid(1210877)]' (**arg(9, 1210877))
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1210878)]' (**arg(10, 1210878))
return "avg25241"