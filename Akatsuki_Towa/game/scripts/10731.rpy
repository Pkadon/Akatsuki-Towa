label avg10731:

play music "ED6105.ogg"
scene avg_bg_070
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7060.ogg"
c0 '[convertstrid(1172484)]'
c0 '[convertstrid(1172485)]'
scene avg_bg_203
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
c31 '[convertstrid(1172486)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1172487)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1172488)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1172489)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1172490)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1172491)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1172492)]'
hide p3
hide p1
c0 '[convertstrid(1172493)]'
$ update_portrait('st063_01 1', 'p1346', [l_entrance(-16), light, flip], 6)
c13461 '[convertstrid(1172494)]'
$ update_portrait('st063_01 1', 'p1346', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1172495)]'
return