label avg10645:

play music "ed9999.ogg"
scene avg_bg_050
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1164593)]'
$ update_portrait('oc005_01 1', 'p5', [l(-6), light, flip], 6)
c51 '[convertstrid(1164594)]'
$ update_portrait('oc005_01 1', 'p5', [l(-6), dark, flip], 5)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1164595)]'
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 5', 'p5', [l_exit(-6), light, flip], 6)
c51 '[convertstrid(1164596)]'
hide p5
$ update_portrait('oc004_01 1', 'p4', [l_entrance(-5), light, flip], 6)
c41 '[convertstrid(1164597)]'
hide p3
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1164598)]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1164599)]'
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1164600)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1164601)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1164602)]'
return