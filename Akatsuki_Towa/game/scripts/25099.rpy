label avg25099:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210276]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1210277]]'
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
play sfx2 "fight_6025.ogg"
c13 '[textdict[1210278]]'
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210279]]'
return