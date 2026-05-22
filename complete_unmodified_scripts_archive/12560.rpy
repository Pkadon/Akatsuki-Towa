label avg12560:

$ play_music("ED6102.ogg")
scene avg_bg_023
$ update_narrator('c12321')
window show
with fade_in
c12321 '[convertstrid(1153117)]'
c12321 '[convertstrid(1153118)]'
c12321 '[convertstrid(1153119)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1153120)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 18', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch04_b.ogg"
c21 '[convertstrid(1153121)]'
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1153122)]'
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1153123)]'
hide p4
c12321 '[convertstrid(1153124)]'
c12321 '[convertstrid(1153125)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1153126)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1153127)]'
hide p4
c12321 '[convertstrid(1153128)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1153129)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1153130)]'
return