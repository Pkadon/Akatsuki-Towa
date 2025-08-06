label avg22130:

play music "ed7511.ogg"
scene avg_bg_036
$ update_narrator('c33')
$ update_portrait('oc003_01 9', 'p3', [r(-6), light], 6)
window show
with fade_in
$ update_portrait('oc003_01 9', 'p3', [r(-6), l_shake, light], 6)
play sfxvoice "avg_vocal_ro15.ogg"
c33 '[convertstrid(1128262)]'
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1128263)]'
hide p2
$ update_portrait('oc001_01 3', 'p1', [l(-2), r_shake, light, flip], 6)
c11 '[convertstrid(1128264)]'
$ update_portrait('oc001_01 3', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 10', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1128265)]'
$ update_portrait('oc003_01 10', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 20', 'p1', [l(-2), light, flip], 6)
play sfx2 "fight_6024.ogg"
c11 '[convertstrid(1128266)]'
return