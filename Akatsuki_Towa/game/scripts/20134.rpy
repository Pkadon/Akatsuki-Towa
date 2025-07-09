label avg20134:
stop music

scene placeholderbackground
window show
with fade_in
c0 '[textdict[1006678]]'
$ update_portrait('sc052_01 4', 'p59', [l_entrance(-25), light, flip], 6)
play sfx2 "other_7050.ogg"
c591 '[textdict[1006679]]'
$ update_portrait('sc052_01 4', 'p59', [l(-25), dark, flip], 6)
$ update_portrait('sc053_01 4', 'p60', [r(-32), light], 5)
c603 '[textdict[1006680]]'
$ update_portrait('sc053_01 4', 'p60', [r(-32), dark], 5)
$ update_portrait('sc052_01 2', 'p59', [l(-25), light, flip], 6)
c591 '[textdict[1006681]]'
$ update_portrait('sc052_01 2', 'p59', [l(-25), dark, flip], 6)
$ update_portrait('sc053_01 1', 'p60', [r(-32), light], 5)
c603 '[textdict[1006682]]'
$ update_portrait('sc053_01 1', 'p60', [r(-32), dark], 5)
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
c591 '[textdict[1006683]]'
hide p60
$ update_portrait('sc052_01 1', 'p59', [l(-25), dark, flip], 6)
play sfx2 "elc_5005.ogg"
c6653 '[textdict[1006684]]'
hide p59
$ update_portrait('sc053_01 2', 'p60', [l(-32), light, flip], 6)
c601 '[textdict[1006685]]'
$ update_portrait('sc053_01 2', 'p60', [l(-32), dark, flip], 6)
$ update_portrait('sc052_01 2', 'p59', [r(-25), light], 5)
c593 '[textdict[1006686]]'
$ update_portrait('sc052_01 2', 'p59', [r(-25), dark], 5)
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
play sfx2 "fight_6006.ogg"
c601 '[textdict[1006687]]'
$ update_portrait('sc053_01 4', 'p60', [l(-32), dark, flip], 6)
$ update_portrait('sc052_01 4', 'p59', [r(-25), light], 5)
play sfx2 "fight_6018.ogg"
c593 '[textdict[1006688]]'
return