label avg12780:

play music "ed7120.ogg"
scene avg_bg_209
$ update_portrait('st064_01 1', 'p1469', [l(-2), light, flip], 6)
$ update_narrator('c14691')
window show
with fade_in
c14691 '[convertstrid(1176279)]'
$ update_portrait('st064_01 1', 'p1469', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1176280)]'
hide p1469
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1176281)]'
hide p3
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1176282)]'
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1176283)]'
hide p4
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('st064_01 2', 'p1469', [l(-2), light, flip], 6)
c14691 '[convertstrid(1176284)]'
hide p3
$ update_portrait('st064_01 2', 'p1469', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1176285)]'
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('st064_01 1', 'p1469', [l(-2), light, flip], 6)
c14691 '[convertstrid(1176286)]'
return