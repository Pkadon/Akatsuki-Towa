label avg10634:

play music "ed7105.ogg"
scene avg_bg_203
$ update_narrator('c13')
window show
with fade_in
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 6)
c13 '[convertstrid(1164064)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1164065)]'
hide p1
$ update_portrait('oc004_01 11', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1164066)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1164067)]'
hide p3
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1164068)]'
hide p4
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('sc010_01 1', 'p18', [l(-10), light, flip], 6)
c181 '[convertstrid(1164069)]'
$ update_portrait('sc010_01 1', 'p18', [l(-10), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1164070)]'
return