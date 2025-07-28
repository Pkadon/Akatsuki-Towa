label avg25262:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch19.ogg"
c23 '[convertstrid(1210976)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6025.ogg"
c13 '[convertstrid(1210977)]'
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210978)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6026.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1210979)]'
hide p2
play sfx2 "other_7068.ogg"
c0 '[convertstrid(1210980)]'
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na18.ogg"
c13 '[convertstrid(1210981)]'
return