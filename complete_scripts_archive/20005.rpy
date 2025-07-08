label avg20005:
stop music

play music "ed9997.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1000224]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
c23 '[textdict[1000225]]'
hide p2
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
c23 '[textdict[1000226]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1000227]]'
hide p1
$ update_portrait('oc002_01 20', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[textdict[1000228]]'
hide p2
play sfx2 "common_remind.ogg"
c0 '[textdict[1000229]]'
c0 '[textdict[1000230]]'
return