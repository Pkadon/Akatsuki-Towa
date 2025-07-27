label avg12861:

play music "ed6323.ogg"
scene avg_bg_219
$ update_portrait('oc003_01 20', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
c31 '[convertstrid(1188961)]'
hide p3
c0 '[convertstrid(1188962)]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1188963)]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 15', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1188964)]'
hide p2
hide p1
c0 '[convertstrid(1188965)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1188966)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 5)
c33 '[convertstrid(1188967)]'
scene avg_bg_070
$ update_narrator('c0')
with fade
c0 '[convertstrid(1188968)]'
c0 '[convertstrid(1188969)]'
c0 '[convertstrid(1188970)]'
return