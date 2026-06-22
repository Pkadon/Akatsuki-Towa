label avg25078:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1210235)]' (**arg(1, 1210235))
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210236)]' (**arg(2, 1210236))
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na19.ogg"
get_char('c13') '[convertstrid(1210237)]' (**arg(3, 1210237))
return