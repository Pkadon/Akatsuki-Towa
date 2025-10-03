label avg12505:

$ play_music("ed7150.ogg")
scene avg_bg_014
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7071.ogg"
c13 '[convertstrid(1150847)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
play sfx2 "other_7072.ogg"
c5241 '[convertstrid(1150848)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1150849)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
c5241 '[convertstrid(1150850)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1150851)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c5241 '[convertstrid(1150852)]'
c5241 '[convertstrid(1150853)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1150854)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c5241 '[convertstrid(1150855)]'
c5241 '[convertstrid(1150856)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1150857)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
play sfx2 "other_7073.ogg"
c21 '[convertstrid(1150858)]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1150859)]'
return