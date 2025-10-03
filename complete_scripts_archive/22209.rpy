label avg22209:

$ play_music("ED6105.ogg")
scene avg_bg_036
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
c11 '[convertstrid(1128680)]'
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1128681)]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc039_01 2', 'p46', [l(-13), light, flip], 6)
c461 '[convertstrid(1128682)]'
hide p2
$ update_portrait('sc039_01 2', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('sc007_01 2', 'p15', [r(-17), light], 6)
c153 '[convertstrid(1128683)]'
hide p46
$ update_portrait('sc007_01 2', 'p15', [r(-17), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128685)]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128686)]'
hide p15
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st026_01 1', 'p225', [r(-14), light], 6)
c2253 '[convertstrid(1128687)]'
$ update_portrait('st026_01 1', 'p225', [r(-14), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
c11 '[convertstrid(1128688)]'
return