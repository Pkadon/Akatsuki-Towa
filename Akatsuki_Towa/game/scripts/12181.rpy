label avg12181:

play music "ED6104.ogg"
scene avg_bg_010
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1007707)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1120600)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1120601)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1120602)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1120603)]'
hide p2
hide p1
$ update_portrait('sc022_01 2', 'p500', [l(-9), light, flip], 6)
$ update_narrator('c5001')
with fade
c5001 '[convertstrid(1120604)]'
$ update_portrait('sc022_01 2', 'p500', [l(-9), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[convertstrid(1120605)]'
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1120606)]'
hide p500
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc022_01 1', 'p30', [l(-9), l_shake, light, flip], 6)
c301 '[convertstrid(1120607)]'
$ update_portrait('sc022_01 1', 'p30', [l(-9), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1120608)]'
hide p30
hide p2
c0 '[convertstrid(1120609)]'
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
c301 '[convertstrid(1120610)]'
$ update_portrait('sc022_01 1', 'p30', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r_exit(-2), light], 6)
c13 '[convertstrid(1120611)]'
hide p1
$ update_portrait('sc022_01 4', 'p30', [l(-9), light, flip], 6)
c301 '[convertstrid(1120612)]'
hide p30
play sfx2 "other_7004.ogg"
c0 '[convertstrid(1120613)]'
$ update_portrait('sc022_01 4', 'p30', [l(-9), light, flip], 6)
c301 '[convertstrid(1120614)]'
$ update_portrait('sc022_01 4', 'p30', [l(-9), light, flip], 6)
c301 '[convertstrid(1120615)]'
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
c301 '[convertstrid(1120616)]'
return