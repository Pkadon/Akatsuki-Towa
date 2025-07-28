label avg10764:

play music "ed6323.ogg"
scene avg_bg_206
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1175153)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1175154)]'
$ update_portrait('st061_01 2', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1175155)]'
$ update_portrait('st061_01 2', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1175156)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1175157)]'
hide p1304
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1175158)]'
play music "ed7511.ogg"
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1175159)]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1175160)]'
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1175161)]'
hide p2
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1175162)]'
hide p4
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1175163)]'
return