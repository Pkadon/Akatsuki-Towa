label avg12620(trans=fade_in):

$ play_music("ed9999.ogg")
scene avg_bg_050
$ update_portrait('oc003_01 7', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with trans
get_char('c31') '[convertstrid(1161828)]' (**arg(1, 1161828))
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li19.ogg"
get_char('c43') '[convertstrid(1161829)]' (**arg(2, 1161829))
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro12.ogg"
get_char('c31') '[convertstrid(1161830)]' (**arg(3, 1161830))
$ update_portrait('oc003_01 18', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1161831)]' (**arg(4, 1161831))
hide p4
$ update_portrait('oc003_01 18', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161832)]' (**arg(5, 1161832))
hide p1
$ update_portrait('oc002_01 21', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1161833)]' (**arg(6, 1161833))
$ update_portrait('oc002_01 21', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1161834)]' (**arg(7, 1161834))
hide p2
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1161835)]' (**arg(8, 1161835))
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161836)]' (**arg(9, 1161836))
hide p4
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161837)]' (**arg(10, 1161837))
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1161838)]' (**arg(11, 1161838))
$ update_portrait('oc003_01 18', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1161839)]' (**arg(12, 1161839))
hide p1
$ update_portrait('oc003_01 18', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1161840)]' (**arg(13, 1161840))
$ update_portrait('oc004_01 7', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1161841)]' (**arg(14, 1161841))
hide p3
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1161842)]' (**arg(15, 1161842))
hide p4
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
get_char('c13') '[convertstrid(1161843)]' (**arg(16, 1161843))
scene avg_bg_070
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
get_char('c13') '[convertstrid(1161844)]' (**arg(17, 1161844))
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161845)]' (**arg(18, 1161845))
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161846)]' (**arg(19, 1161846))
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1161847)]' (**arg(20, 1161847))
return "avg12620"