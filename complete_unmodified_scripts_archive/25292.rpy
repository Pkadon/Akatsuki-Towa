label avg25292:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1211109)]' (**arg(1, 1211109))
hide p1
get_char('c20233') '[convertstrid(1211110)]' (**arg(2, 1211110))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1211111)]' (**arg(3, 1211111))
hide p2
get_char('c20233') '[convertstrid(1211112)]' (**arg(4, 1211112))
play sfx2 "fight_6018.ogg"
get_char('c0') '[convertstrid(1211113)]' (**arg(5, 1211113))
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch17.ogg"
get_char('c23') '[convertstrid(1211114)]' (**arg(6, 1211114))
hide p2
play sfx2 "common_36rewardsp.ogg"
get_char('c20233') '[convertstrid(1211115)]' (**arg(7, 1211115))
return