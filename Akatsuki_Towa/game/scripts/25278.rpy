label avg25278:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1211053]]'
hide p1
c20153 '[textdict[1211054]]'
$ update_portrait('oc001_01 21', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na16.ogg"
c13 '[textdict[1211055]]'
hide p1
c20153 '[textdict[1211056]]'
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch18.ogg"
c23 '[textdict[1211057]]'
hide p2
c20153 '[textdict[1211058]]'
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
c13 '[textdict[1211059]]'
return