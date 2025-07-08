label avg25109:
stop music

scene placeholderbackground
window show
with fade_in
play sfx2 "other_7092.ogg"
c0 '[textdict[1210322]]'
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1210323]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na22.ogg"
c13 '[textdict[1210324]]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1210325]]'
return