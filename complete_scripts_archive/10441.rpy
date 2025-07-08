label avg10441:
stop music

play music "ed7162.ogg"
scene avg_bg_078
window show
with fade_in
c0 '[textdict[1141749]]'
c0 '[textdict[1141750]]'
c0 '[textdict[1141751]]'
$ update_portrait('sc071_01 1', 'p611', [r(-20), light], 5)
c6113 '[textdict[1141752]]'
hide p611
$ update_portrait('sc071_01 4', 'p611', [r(-20), light], 5)
c6113 '[textdict[1141753]]'
stop music
hide p611
$ update_portrait('uc004_01 4', 'p1022', [r(-25), light], 5)
c10223 '[textdict[1141754]]'
play music "ed7544.ogg"
hide p1022
$ update_portrait('uc004_01 4', 'p1022', [r(-25), dark], 5)
$ update_portrait('st037_01 1', 'p236', [l(-10), light, flip], 6)
c2361 '[textdict[1141755]]'
hide p1022
hide p236
$ update_portrait('st037_01 1', 'p236', [l(-10), dark, flip], 6)
$ update_portrait('uc004_01 4', 'p1022', [r(-25), light], 5)
c10223 '[textdict[1141756]]'
hide p236
hide p1022
$ update_portrait('uc004_01 4', 'p1022', [r(-25), dark], 5)
$ update_portrait('st037_01 4', 'p236', [l(-10), light, flip], 6)
c2361 '[textdict[1141757]]'
return