label avg25220:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 20', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfx2 "fight_6016.ogg"
play sfxvoice "avg_vocal_ch27.ogg"
c23 '[textdict[1210762]]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210763]]'
hide p1
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch16.ogg"
c23 '[textdict[1210764]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfx2 "elc_5002.ogg"
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1210765]]'
return