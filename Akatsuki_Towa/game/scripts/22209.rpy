label avg22209(trans=fade_in):

$ play_music("ED6105.ogg")
scene avg_bg_036
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1128680)]' (**arg(1, 1128680))
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128681)]' (**arg(2, 1128681))
hide p1
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc039_01 2', 'p46', [l(-13), light, flip], 6)
get_char('c461') '[convertstrid(1128682)]' (**arg(3, 1128682))
hide p2
$ update_portrait('sc039_01 2', 'p46', [l(-13), dark, flip], 5)
$ update_portrait('sc007_01 2', 'p15', [r(-17), light], 6)
get_char('c153') '[convertstrid(1128683)]' (**arg(4, 1128683))
hide p46
$ update_portrait('sc007_01 2', 'p15', [r(-17), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128685)]' (**arg(5, 1128685))
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128686)]' (**arg(6, 1128686))
hide p15
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st026_01 1', 'p225', [r(-14), light], 6)
get_char('c2253') '[convertstrid(1128687)]' (**arg(7, 1128687))
$ update_portrait('st026_01 1', 'p225', [r(-14), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
get_char('c11') '[convertstrid(1128688)]' (**arg(8, 1128688))
return "avg22209"