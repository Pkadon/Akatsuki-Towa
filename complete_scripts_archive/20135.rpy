label avg20135:

stop music
scene placeholderbackground
window show
with fade_in
$ update_portrait('sc038_01 4', 'p45', [l_entrance(-1), light, flip], 6)
c451 '[textdict[1006689]]'
$ update_portrait('sc038_01 4', 'p45', [l(-1), dark, flip], 6)
$ update_portrait('sc040_01 4', 'p47', [r(-9), light], 5)
play sfx2 "elc_5002.ogg"
c473 '[textdict[1006690]]'
hide p45
$ update_portrait('sc040_01 4', 'p47', [r(-9), dark], 5)
$ update_portrait('sc039_01 4', 'p46', [l(-13), light, flip], 6)
c461 '[textdict[1006691]]'
hide p47
$ update_portrait('sc039_01 4', 'p46', [l(-13), dark, flip], 6)
$ update_portrait('sc041_01 4', 'p48', [r(-9), light], 5)
c483 '[textdict[1006692]]'
hide p46
$ update_portrait('sc041_01 4', 'p48', [r(-9), dark], 5)
play sfx2 "elc_5005.ogg"
c6651 '[textdict[1006693]]'
play sfx2 "elc_5005.ogg"
c6651 '[textdict[1006693]]'
play sfx2 "elc_5005.ogg"
c6651 '[textdict[1006693]]'
hide p48
$ update_portrait('sc060_01 1', 'p65', [r(-16), light], 5)
c653 '[textdict[1006696]]'
$ update_portrait('sc060_01 1', 'p65', [r(-16), dark], 5)
$ update_portrait('sc045_01 4', 'p52', [l(-11), light, flip], 6)
c521 '[textdict[1006697]]'
hide p65
$ update_portrait('sc045_01 4', 'p52', [l(-11), dark, flip], 6)
$ update_portrait('sc038_01 4', 'p45', [r(-1), light], 5)
c453 '[textdict[1006698]]'
$ update_portrait('sc038_01 3', 'p45', [r(-1), light], 5)
play sfx2 "fight_6023.ogg"
c453 '[textdict[1006699]]'
return