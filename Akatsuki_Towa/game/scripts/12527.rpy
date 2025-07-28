label avg12527:

play music "ED6301.ogg"
scene placeholderbackground
$ update_narrator('c33')
window show
with fade_in
$ update_portrait('oc003_01 8', 'p3', [r_entrance(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c33 '[convertstrid(1151515)]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1151516)]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1151517)]'
hide p3
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1151518)]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[convertstrid(1151519)]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1151520)]'
return