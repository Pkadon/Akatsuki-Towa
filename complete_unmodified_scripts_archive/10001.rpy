label avg10001(trans=fade_in):

$ play_music("ED6516.ogg")
scene avg_bg_070
show memoryoverlay zorder 2
$ update_narrator('c5001')
window show
with trans
play sfx2 "other_7085.ogg"
play sfxvoice "avg_vocal_roi01.ogg"
get_char('c5001') '[convertstrid(1002967)]' (**arg(1, 1002967, size=(1.5))) with shake
scene avg_bg_004
show memoryoverlay zorder 2
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfxvoice "bcv_oc001_hurt_01.ogg"
get_char('c13') '[convertstrid(1000001)]' (**arg(2, 1000001))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000002)]' (**arg(3, 1000002))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000003)]' (**arg(4, 1000003))
$ update_portrait('oc001_01 14', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na08.ogg"
get_char('c13') '[convertstrid(1000004)]' (**arg(5, 1000004))
$ update_portrait('oc001_01 3', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1000005)]' (**arg(6, 1000005))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000006)]' (**arg(7, 1000006))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000007)]' (**arg(8, 1000007))
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000008)]' (**arg(9, 1000008))
$ update_portrait('oc001_01 15', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1000009)]' (**arg(10, 1000009))
$ update_portrait('oc001_01 14', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na07.ogg"
get_char('c13') '[convertstrid(1000010)]' (**arg(11, 1000010)) with shake
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000011)]' (**arg(12, 1000011))
$ update_portrait('oc001_01 13', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1000012)]' (**arg(13, 1000012))
$ play_music("ed7511.ogg")
$ update_portrait('oc001_01 13', 'p1', [r(-2), dark], 5)
play sfx2 "other_7079.ogg"
get_char('c5291') '[convertstrid(1100035)]' (**arg(14, 1100035))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1100036)]' (**arg(15, 1100036))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1100037)]' (**arg(16, 1100037))
$ update_portrait('oc001_01 15', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "fight_6029.ogg"
play sfxvoice "avg_vocal_na24.ogg"
get_char('c13') '[convertstrid(1100038)]' (**arg(17, 1100038))
$ update_portrait('oc001_01 15', 'p1', [r(-2), dark], 5)
play sfx2 "other_7076.ogg"
get_char('c5291') '[convertstrid(1100039)]' (**arg(18, 1100039))
$ update_portrait('oc001_01 9', 'p1', [r_midback(-2), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "avg_vocal_na12.ogg"
get_char('c13') '[convertstrid(1100040)]' (**arg(19, 1100040))
return "avg10001"