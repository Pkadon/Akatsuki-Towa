label avg12613:

$ play_music("ed7201.ogg")
scene avg_bg_010
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1161494)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1161495)]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1161496)]'
hide p4
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 13', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1161497)]'
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1161498)]'
hide p3
hide p2
play sfx2 "other_7004.ogg"
c0 '[convertstrid(1161499)]'
$ update_portrait('oc004_01 12', 'p4', [l(-5), l_shake, light, flip], 6)
c41 '[convertstrid(1161500)]'
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1161501)]'
hide p4
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro04.ogg"
c31 '[convertstrid(1161502)]'
hide p2
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1161503)]'
hide p3
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1161504)]'
hide p1
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1161505)]'
return