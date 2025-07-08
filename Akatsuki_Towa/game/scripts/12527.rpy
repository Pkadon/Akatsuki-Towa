label avg12527:
stop music

play music "ED6301.ogg"
scene placeholderbackground
window show
with fade_in
$ update_portrait('oc003_01 8', 'p3', [r_entrance(-6), light], 5)
play sfxvoice "avg_vocal_ro13.ogg"
c33 '[textdict[1151515]]'
hide p3
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[textdict[1151516]]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[textdict[1151517]]'
hide p3
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1151518]]'
hide p2
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1151519]]'
hide p16
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[textdict[1151520]]'
return