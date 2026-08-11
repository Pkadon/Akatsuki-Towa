label avg12104(trans=fade_in):

$ play_music("ed7111.ogg")
scene avg_bg_047
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
play sfx2 "common_select.ogg"
get_char('c11') '[convertstrid(1128019)]' (**arg(1, 1128019))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc005_01 5', 'p5', [r(-6), light], 6)
play sfxvoice "avg_vocal_ji11.ogg"
get_char('c53') '[convertstrid(1128020)]' (**arg(2, 1128020))
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1128021)]' (**arg(3, 1128021))
$ update_portrait('oc005_01 10', 'p5', [r(-6), light], 6)
get_char('c53') '[convertstrid(1128022)]' (**arg(4, 1128022))
$ update_portrait('oc005_01 10', 'p5', [r(-6), dark], 5)
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128023)]' (**arg(5, 1128023))
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc005_01 1', 'p5', [r(-6), light], 6)
play sfx2 "common_quest.ogg"
get_char('c53') '[convertstrid(1128024)]' (**arg(6, 1128024))
return "avg12104"