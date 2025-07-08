label avg25285:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1211087]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfx2 "other_7092.ogg"
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1211088]]'
hide p2
play sfx2 "other_7068.ogg"
c0 '[textdict[1211089]]'
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na24.ogg"
c13 '[textdict[1211090]]'
return