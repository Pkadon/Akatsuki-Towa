label avg1034:

play music "ed7201.ogg"
scene avg_bg_010
$ update_narrator('c23')
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
window show
with fade_in
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(2100577)]'
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc053_01 4', 'p60', [l_entrance(-32), light, flip], 6)
c601 '[convertstrid(2100578)]'
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
c601 '[convertstrid(2100579)]'
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
c601 '[convertstrid(2100580)]'
$ update_portrait('sc053_01 4', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(2100581)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2100582)]'
return