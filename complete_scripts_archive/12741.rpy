label avg12741:

play music "ed7105.ogg"
scene avg_bg_203
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1172905)]'
c0 '[convertstrid(1172906)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1172907)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1172908)]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1172909)]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1172910)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1172911)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1172912)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
c13 '[convertstrid(1172913)]' with shake
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6025.ogg"
c31 '[convertstrid(1172914)]'
return