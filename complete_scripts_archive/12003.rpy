label avg12003:
stop music

play music "ed7150.ogg"
scene avg_bg_023
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
window show
with fade_in
c561 '[textdict[1007080]]'
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1007081]]'
hide p2
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1007082]]'
hide p56
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007083]]'
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1007084]]'
hide p56
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007085]]'
return