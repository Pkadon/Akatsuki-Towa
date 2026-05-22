label avg12538:

$ play_music("ED6100.ogg")
scene avg_bg_023
$ update_narrator('c12021')
window show
with fade_in
c12021 '[convertstrid(1152887)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1152888)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c12021 '[convertstrid(1152889)]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1152890)]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
c12021 '[convertstrid(1152891)]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1152892)]'
hide p2
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
with fade
c43 '[convertstrid(1152893)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1152894)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1152895)]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1152896)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1152897)]'
hide p4
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1152898)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c12021 '[convertstrid(1152899)]'
return