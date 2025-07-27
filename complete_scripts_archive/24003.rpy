label avg24003:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1200011)]'
hide p1
$ update_portrait('st044_01 1', 'p243', [mid(10), light], 5)
c2433 '[convertstrid(1200012)]'
hide p243
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1200013)]'
return