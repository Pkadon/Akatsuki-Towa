label avg12220:

play music "ed7569.ogg"
scene avg_bg_036
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7018.ogg"
c0 '[convertstrid(1121571)]'
$ update_portrait('oc002_01 12', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[convertstrid(1120948)]'
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1120949)]'
$ update_portrait('oc002_01 13', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1120950)]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1120951)]'
hide p1
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('sc040_01 8', 'p47', [r(-9), light], 6)
c473 '[convertstrid(1120952)]'
hide p4
$ update_portrait('sc040_01 8', 'p47', [r(-9), dark], 5)
$ update_portrait('sc039_01 2', 'p46', [l(-13), light, flip], 6)
c461 '[convertstrid(1120953)]'
hide p46
hide p47
$ update_portrait('uc004_02 2', 'p991', [r(-6), light], 6)
$ update_narrator('c9913')
with fade
c9913 '[convertstrid(1120954)]'
$ update_portrait('uc004_02 2', 'p991', [r(-6), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
c11 '[convertstrid(1120955)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('uc004_02 1', 'p991', [r(-6), light], 6)
c9913 '[convertstrid(1120956)]'
hide p1
$ update_portrait('uc004_02 1', 'p991', [r(-6), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1120957)]'
hide p991
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 15', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1120958)]'
hide p2
$ update_portrait('oc004_01 15', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1121572)]'
return