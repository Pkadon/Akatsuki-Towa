label avg20134:

$ play_music("ed7300.ogg")
scene avg_bg_071
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1006678)]' (**arg(1, 1006678))
$ update_portrait('sc052_01 4', 'p59', [l_entrance(-25), light, flip], 6)
play sfx2 "other_7050.ogg"
get_char('c591') '[convertstrid(1006679)]' (**arg(2, 1006679))
$ update_portrait('sc052_01 4', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('sc053_01 4', 'p60', [r(-32), light], 6)
get_char('c603') '[convertstrid(1006680)]' (**arg(3, 1006680))
$ update_portrait('sc053_01 4', 'p60', [r(-32), dark], 5)
$ update_portrait('sc052_01 2', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1006681)]' (**arg(4, 1006681))
$ update_portrait('sc052_01 2', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('sc053_01 1', 'p60', [r(-32), light], 6)
get_char('c603') '[convertstrid(1006682)]' (**arg(5, 1006682))
$ update_portrait('sc053_01 1', 'p60', [r(-32), dark], 5)
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1006683)]' (**arg(6, 1006683))
hide p60
$ update_portrait('sc052_01 1', 'p59', [l(-25), dark, flip], 5)
play sfx2 "elc_5005.ogg"
get_char('c6653') '[convertstrid(1006684)]' (**arg(7, 1006684))
hide p59
$ update_portrait('sc053_01 2', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1006685)]' (**arg(8, 1006685))
$ update_portrait('sc053_01 2', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('sc052_01 2', 'p59', [r(-25), light], 6)
get_char('c593') '[convertstrid(1006686)]' (**arg(9, 1006686))
$ update_portrait('sc052_01 2', 'p59', [r(-25), dark], 5)
$ update_portrait('sc053_01 4', 'p60', [l(-32), light, flip], 6)
play sfx2 "fight_6006.ogg"
get_char('c601') '[convertstrid(1006687)]' (**arg(10, 1006687))
$ update_portrait('sc053_01 4', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('sc052_01 4', 'p59', [r(-25), light], 6)
play sfx2 "fight_6018.ogg"
get_char('c593') '[convertstrid(1006688)]' (**arg(11, 1006688))
return