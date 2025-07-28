label avg20097:

play music "ed7104.ogg"
scene placeholderbackground
$ update_narrator('c461')
window show
with fade_in
$ update_portrait('sc039_01 5', 'p46', [l_entrance(-13), light, flip], 6)
play sfx2 "other_7017.ogg"
c461 '[convertstrid(1004824)]'
$ update_portrait('sc039_01 5', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1004825)]'
hide p46
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
c11 '[convertstrid(1004826)]'
hide p4
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc005_01 1', 'p5', [r(-6), light], 6)
c53 '[convertstrid(1004827)]'
hide p1
$ update_portrait('oc005_01 1', 'p5', [r(-6), dark], 5)
$ update_portrait('sc040_01 1', 'p47', [l(-9), light, flip], 6)
c471 '[convertstrid(1004828)]'
hide p5
$ update_portrait('sc040_01 1', 'p47', [l(-9), dark, flip], 5)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1004829)]'
hide p47
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
c461 '[convertstrid(1004830)]'
hide p2
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1004831)]'
hide p1
$ update_portrait('oc005_01 1', 'p5', [r(-6), light], 6)
c53 '[convertstrid(1004832)]'
hide p46
$ update_portrait('oc005_01 1', 'p5', [r(-6), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1004833)]'
return