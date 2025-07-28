label avg12341:

play music "ed7105.ogg"
scene avg_bg_070
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
play sfx2 "other_7048.ogg"
c11 '[convertstrid(1133492)]'
scene avg_bg_022
$ update_portrait('st053_01 4', 'p1007', [r(-12), light], 6)
$ update_narrator('c10073')
with fade
c10073 '[convertstrid(1133493)]'
$ update_portrait('st053_01 3', 'p1007', [r(-12), light], 6)
c10073 '[convertstrid(1133494)]'
$ update_portrait('st053_01 3', 'p1007', [r(-12), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1133495)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st053_01 1', 'p1007', [r(-12), light], 6)
c10073 '[convertstrid(1133496)]'
$ update_portrait('st053_01 2', 'p1007', [r(-12), light], 6)
c10073 '[convertstrid(1133497)]'
hide p2
$ update_portrait('st053_01 2', 'p1007', [r(-12), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1133498)]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st053_01 4', 'p1007', [r(-12), light], 6)
c10073 '[convertstrid(1133499)]'
hide p3
$ update_portrait('st053_01 4', 'p1007', [r(-12), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1133500)]'
hide p1007
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1133501)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1133502)]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li19.ogg"
c43 '[convertstrid(1133503)]'
$ update_portrait('oc004_01 6', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1133504)]'
hide p3
$ update_portrait('oc004_01 6', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
c11 '[convertstrid(1133505)]'
return