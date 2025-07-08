label avg1003:
stop music

play music "ed7106.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
c21 '[textdict[2100038]]'
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[2100039]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7037.ogg"
c561 '[textdict[2100040]]'
hide p56
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100041]]'
hide p56
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100042]]'
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[2100043]]'
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[2100044]]'
hide p56
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch21.ogg"
c21 '[textdict[2100045]]'
hide p1
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[2100046]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100047]]'
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[2100048]]'
hide p56
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100049]]'
hide p1
$ update_portrait('sc049_01 10', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[2100050]]'
return