label avg10045:

play music "ed7150.ogg"
scene avg_bg_014
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7064.ogg"
c13 '[convertstrid(1003854)]'
scene avg_bg_070
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
c31 '[convertstrid(1003855)]'
scene avg_bg_014
$ update_narrator('c11')
with fade
$ update_portrait('oc001_01 1', 'p1', [l_entrance(-2), light, flip], 6)
c11 '[convertstrid(1003856)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
c6453 '[convertstrid(1003857)]'
c5343 '[convertstrid(1003858)]'
c6453 '[convertstrid(1003859)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1003860)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
c5343 '[convertstrid(1003861)]'
hide p2
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1003862)]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
c6473 '[convertstrid(1003863)]'
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1003864)]'
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 5)
c6473 '[convertstrid(1003865)]'
c6473 '[convertstrid(1003866)]'
hide p4
c5341 '[convertstrid(1003867)]'
c6473 '[convertstrid(1003868)]'
c6473 '[convertstrid(1003869)]'
c6451 '[convertstrid(1003870)]'
scene avg_bg_070
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
c13 '[convertstrid(1003871)]'
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1003872)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1003873)]'
scene avg_bg_014
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
c13 '[convertstrid(1003874)]'
return