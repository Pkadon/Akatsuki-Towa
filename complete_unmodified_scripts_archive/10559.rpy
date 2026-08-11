label avg10559(trans=fade_in):

$ play_music("ed7151.ogg")
scene avg_bg_105
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
$ update_narrator('c33')
window show
with trans
get_char('c33') '[convertstrid(1154009)]' (**arg(1, 1154009))
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc031_01 2', 'p39', [l_entrance(-14), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c391') '[convertstrid(1154010)]' (**arg(2, 1154010))
hide p3
$ update_portrait('sc031_01 2', 'p39', [l(-14), dark, flip], 5)
$ update_portrait('sc008_01 4', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1154011)]' (**arg(3, 1154011))
hide p39
$ update_portrait('sc008_01 4', 'p16', [r(-18), dark], 5)
$ update_portrait('sc030_01 2', 'p38', [l(-12), l_shake, light, flip], 6)
get_char('c381') '[convertstrid(1154012)]' (**arg(4, 1154012))
hide p38
$ update_portrait('sc031_01 5', 'p39', [l(-14), light, flip], 6)
get_char('c391') '[convertstrid(1154013)]' (**arg(5, 1154013))
$ update_portrait('sc031_01 5', 'p39', [l(-14), dark, flip], 5)
$ update_portrait('sc008_01 4', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1154014)]' (**arg(6, 1154014))
hide p39
$ update_portrait('sc008_01 4', 'p16', [r(-18), dark], 5)
$ update_portrait('sc032_01 4', 'p40', [l(-17), l_shake, light, flip], 6)
get_char('c401') '[convertstrid(1154015)]' (**arg(7, 1154015))
$ update_portrait('sc032_01 4', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('sc008_01 2', 'p16', [r(-18), light], 6)
get_char('c163') '[convertstrid(1154016)]' (**arg(8, 1154016))
$ update_portrait('sc008_01 2', 'p16', [r(-18), dark], 5)
$ update_portrait('sc032_01 5', 'p40', [l(-17), light, flip], 6)
get_char('c401') '[convertstrid(1154017)]' (**arg(9, 1154017))
$ update_portrait('sc032_01 5', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('sc008_01 4', 'p16', [r(-18), r_shake, light], 6)
get_char('c163') '[convertstrid(1154018)]' (**arg(10, 1154018))
hide p40
$ update_portrait('sc008_01 4', 'p16', [r(-18), dark], 5)
$ update_portrait('sc030_01 4', 'p38', [l(-12), light, flip], 6)
get_char('c381') '[convertstrid(1154019)]' (**arg(11, 1154019))
hide p16
$ update_portrait('sc030_01 4', 'p38', [l(-12), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), r_shake, light], 6)
get_char('c33') '[convertstrid(1154020)]' (**arg(12, 1154020))
hide p38
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('sc031_01 4', 'p39', [l(-14), light, flip], 6)
get_char('c391') '[convertstrid(1154021)]' (**arg(13, 1154021))
hide p39
$ update_portrait('sc032_01 4', 'p40', [l(-17), light, flip], 6)
get_char('c401') '[convertstrid(1154022)]' (**arg(14, 1154022))
$ update_portrait('sc032_01 4', 'p40', [l(-17), dark, flip], 5)
$ update_portrait('oc003_01 10', 'p3', [r(-6), light], 6)
get_char('c33') '[convertstrid(1154023)]' (**arg(15, 1154023))
hide p40
$ update_portrait('oc003_01 10', 'p3', [r(-6), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154024)]' (**arg(16, 1154024))
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1154025)]' (**arg(17, 1154025))
return "avg10559"