label avg10501:

$ play_music("ed7150.ogg")
scene avg_bg_070
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1150002)]' (**arg(1, 1150002))
get_char('c0') '[convertstrid(1150003)]' (**arg(2, 1150003))
get_char('c0') '[convertstrid(1150004)]' (**arg(3, 1150004))
scene avg_bg_022
$ update_narrator('c21')
with fade
$ update_portrait('oc002_01 9', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "other_7085.ogg"
get_char('c21') '[convertstrid(1150005)]' (**arg(4, 1150005))
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r_entrance(-2), light], 6)
play sfx2 "other_7085.ogg"
get_char('c13') '[convertstrid(1150006)]' (**arg(5, 1150006))
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
get_char('c12011') '[convertstrid(1150007)]' (**arg(6, 1150007)) with shake
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1150008)]' (**arg(7, 1150008))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150009)]' (**arg(8, 1150009))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch15.ogg"
get_char('c21') '[convertstrid(1150010)]' (**arg(9, 1150010))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150011)]' (**arg(10, 1150011))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(1150012)]' (**arg(11, 1150012))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150013)]' (**arg(12, 1150013))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150014)]' (**arg(13, 1150014))
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1150015)]' (**arg(14, 1150015))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1150016)]' (**arg(15, 1150016))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150017)]' (**arg(16, 1150017))
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150018)]' (**arg(17, 1150018))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150019)]' (**arg(18, 1150019))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150020)]' (**arg(19, 1150020))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150021)]' (**arg(20, 1150021))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150022)]' (**arg(21, 1150022))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150023)]' (**arg(22, 1150023))
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150024)]' (**arg(23, 1150024))
$ update_portrait('oc002_01 18', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150025)]' (**arg(24, 1150025))
$ update_portrait('oc002_01 8', 'p2', [l_exit(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150026)]' (**arg(25, 1150026))
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfx2 "other_7085.ogg"
get_char('c13') '[convertstrid(1150027)]' (**arg(26, 1150027))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150028)]' (**arg(27, 1150028))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150029)]' (**arg(28, 1150029))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150030)]' (**arg(29, 1150030))
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150031)]' (**arg(30, 1150031))
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150032)]' (**arg(31, 1150032))
$ play_music("ed6565.ogg")
scene avg_bg_042
show memoryoverlay zorder 2
$ update_narrator('c2201')
with fade
$ update_portrait('st021_01 2', 'p220', [l_entrance(-17), light, flip], 6)
get_char('c2201') '[convertstrid(1150033)]' (**arg(32, 1150033))
$ update_portrait('st021_01 1', 'p220', [l(-17), light, flip], 6)
get_char('c2201') '[convertstrid(1150034)]' (**arg(33, 1150034))
$ update_portrait('st021_01 4', 'p220', [l(-17), light, flip], 6)
get_char('c2201') '[convertstrid(1150035)]' (**arg(34, 1150035))
scene avg_bg_070
$ update_narrator('c21')
with fade
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1150036)]' (**arg(35, 1150036))
$ play_music("ed7150.ogg")
scene avg_bg_022
$ update_narrator('c13')
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
with fade
$ update_portrait('oc001_01 10', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1150037)]' (**arg(36, 1150037))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150038)]' (**arg(37, 1150038))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1150039)]' (**arg(38, 1150039))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1150040)]' (**arg(39, 1150040))
return