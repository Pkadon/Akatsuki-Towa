label avg25243:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "common_select.ogg"
c13 '[textdict[1210881]]'
hide p1
c20243 '[textdict[1210882]]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[textdict[1210883]]'
hide p2
c20243 '[textdict[1210884]]'
return