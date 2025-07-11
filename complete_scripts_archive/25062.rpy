label avg25062:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "common_select.ogg"
c13 '[textdict[1210181]]'
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1210182]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210183]]'
return