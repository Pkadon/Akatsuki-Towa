label avg25270:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na13.ogg"
c13 '[convertstrid(1211012)]'
hide p1
play sfx2 "other_7079.ogg"
c20133 '[convertstrid(1211013)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1211014)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na10.ogg"
c13 '[convertstrid(1211015)]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1211016)]'
hide p2
play sfx2 "fight_6003.ogg"
c20133 '[convertstrid(1211017)]'
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1211018)]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1211019)]'
return