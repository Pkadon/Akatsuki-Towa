label avg25213:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_select.ogg"
c13 '[textdict[1210739]]'
hide p1
c20233 '[textdict[1210740]]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[textdict[1210741]]'
return