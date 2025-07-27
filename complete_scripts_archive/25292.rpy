label avg25292:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1211109)]'
hide p1
c20233 '[convertstrid(1211110)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1211111)]'
hide p2
c20233 '[convertstrid(1211112)]'
play sfx2 "fight_6018.ogg"
c0 '[convertstrid(1211113)]'
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch17.ogg"
c23 '[convertstrid(1211114)]'
hide p2
play sfx2 "common_36rewardsp.ogg"
c20233 '[convertstrid(1211115)]'
return